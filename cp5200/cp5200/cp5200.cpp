/* 
 * File:   cp5200.cpp
 * Author: Misi
 * 
 * Created on 2017. február 3., 9:38
 * V2.0 2017-06-15 mihint
 * V2.1 Rebuild 2020-10-09
 * V2.5 Rebuild on bookworm 2025-02-26
 * V3.0 Include brightness query and set 2025-03-13
 */

#include "cp5200.h"

// <editor-fold desc="network common header">
string ncid = "FFFFFFFF";           // network controller id    4 bytes
string ndal = "D300";               // network data length      2 bytes
int ndali = 0;
string resv = "0000";               // reserved (const)         2 bytes
string pact = "68";                 // packet type (const)      1 byte
string cart = "32";                 // card type (const)        1 byte
string caid = "01";                 // card ID                  1 byte
string prco = "7B";                 // protocol code (const)    1 byte
string adin = "01";                 // additional info (const)  1 byte
string pdal = "C800";               // packed data length       2 bytes
int pdali = 0;
string pano = "00";                 // packet number first=0    1 byte
int panoi = 0;
string lpno = "00";                 // total number of pkg-1    1 byte
int lpnoi = 0;
string pada = "";                   // packet data (varlen)     n bytes
string chsu = "0000";               // two bytes checksum       2 bytes
// </editor-fold>

// <editor-fold desc="RS232 common begin-end">
string sbeg = "A5";                 // serial begin (const)     1 bytes
// from pact 
// to chsu is same network common header
string sveg = "AE";                 // serial end               1 bytes  
// </editor-fold>

int _ip_port = 5200;
const char *_ip_address = "192.168.000.000";
tcflag_t _rs232_baud = B115200;
int _rs232_baud_int = 115200;
const char *_rs232_serport = "/dev/ttyAMA0";

int uart0_filestream = -1;

int _cp5200_debug = 0;
int _cp5200_send_mode = 0;          // 0: TCP-IP, 1: RS232, 2: RS485
int _cp5200_brightness = 0;         // 0..31: manual, 255: auto

bool __get_fexist (const string& name) 
{
  struct stat buffer;   
  return (stat (name.c_str(), &buffer) == 0); 
}

// <editor-fold desc="external set functions">
extern "C" void _get_cp5200_version()
{
    cout << "cp5200 GNU library V" << cplibmv << "." << cplibsv << endl;
}

extern "C" void _set_cp5200_debug()
{
    _cp5200_debug = 1;
}

extern "C" void _set_cp5200_send_mode(int sm)
{
    _cp5200_send_mode = sm;
}

extern "C" void _set_cp5200_ipcomm(char *ipcim, int ippor)
{
    _ip_address = ipcim;
    _ip_port = ippor;
}

extern "C" void _set_cp5200_rs232comm(char *serpor, int sbaud)
{
    _rs232_serport = serpor;
    _rs232_baud_int = sbaud;
    switch (_rs232_baud_int)
    {
        case 9600:
        {
            _rs232_baud = B9600;
            break;
        }
        default:
        {
            break;
        }
    }
}
// </editor-fold>

// <editor-fold desc="character conversion">
void __replaceAll(std::string& str, const std::string& from, const std::string& to) 
{
    if(from.empty())
        return;
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) 
    {
        if (start_pos % 2 == 0)
        {
            str.replace(start_pos, from.length(), to);
            WLOG("replaced, start position:" + to_string(start_pos));
            start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
        }
        start_pos +=2;
    }
}

string _addesc(string src) // encode esape seqences before send to RS-232/485
{
    string ret = "";
    string mia = src;
    transform(mia.begin(), mia.end(), mia.begin(), ::toupper);
    __replaceAll(mia, "AA", "AA0A");
    __replaceAll(mia, "A5", "AA05");
    __replaceAll(mia, "AE", "AA0E");
    ret = mia;
    return ret;
}

char *revesc(char *src) // decode esape seqences after receive from RS-232/485
{
    // Simple implementation - return the input string as-is
    // This function appears to be incomplete in the original source
    return src;
}

char *convert(const char *from, const char *to, char *src) 
{
    if (!from || !to || !src) {
        return NULL;
    }
    
    iconv_t cd;
    cd = iconv_open(to, from);
    if(cd == (iconv_t)-1)
        return NULL;

    size_t len = strlen(src);
    if(!len) {
        iconv_close(cd);
        return NULL;
    }

    // Allocate target buffer
    size_t target_len = len * 2; // UTF-8 can expand to 2x
    char *target = (char *)calloc(target_len, 1);
    if (!target) {
        iconv_close(cd);
        return NULL;
    }
    
    // Create a mutable copy of src for iconv
    char *src_mutable = strdup(src);
    if (!src_mutable) {
        free(target);
        iconv_close(cd);
        return NULL;
    }
    
    size_t src_len = len;
    char *target_start = target; // Save the start position
    
    // Perform conversion
    size_t iconv_value = iconv(cd, &src_mutable, &src_len, &target, &target_len);
    
    // Clean up
    free(src_mutable);
    iconv_close(cd);
    
    if(iconv_value == (size_t)-1) {
        free(target_start);
        return NULL;
    }
    
    // Return the start of the converted string
    return target_start;
}

char *convertUTF8ToEASCII(string str) 
{
    if (str.empty()) {
        return NULL;
    }
    
    // For simple ASCII text, just return a copy
    // This avoids the complex iconv conversion that's causing issues
    char *res = strdup(str.c_str());
    
    if (res == NULL) {
        WLOG("Warning: Memory allocation failed");
        return NULL;
    }
    
    WLOG("convertUTF8ToEASCII: '" + str + "' -> allocated " + to_string(str.length()) + " bytes");
    return res;
}
// </editor-fold>

// <editor-fold desc="int to hex string conversion">
string __cint2bytes_lofo(int i, int byno)
{
    string vissza = "";
    stringstream stream;
    stream << setfill('0') << setw(byno) << hex << i;
    vissza = stream.str();
    if (byno == 4)
    {
        string bufi = vissza.substr(0,2) + vissza.substr(2,2);
        vissza = bufi;
    }
    return vissza;
}

string __cint2bytes(int i, int byno)
{
    string vissza = "";
    stringstream stream;
    stream << setfill('0') << setw(byno) << hex << i;
    vissza = stream.str();
    if (byno == 4)
    {
        string bufi = vissza.substr(2,2) + vissza.substr(0,2);
        vissza = bufi;
    }
    return vissza;
}
// </editor-fold>

// <editor-fold desc="create simple 16bit checksum for cp-packet, low-former">
string _getCRC16(string mibol, int offset)
{
    string ret = "0000";
    int szam = 0;
    int marad = 0;
    //int offset = 16: net, 2: rs232;
    stringstream convertStream;
    while (offset < mibol.length()) 
    {
        unsigned int buffer;
        convertStream << hex << mibol.substr(offset, 2);         
        convertStream >> hex >> buffer;
        offset += 2;
        szam += buffer;
        marad = szam - 65536;
        if (marad >= 0)
            szam = marad;
        // empty the stringstream
        convertStream.str(string());
        convertStream.clear();
    }
    ret = __cint2bytes(szam, 4);
    return ret;
}
// </editor-fold>

// <editor-fold desc="send and receive socket">
int _MessageSend_net(char * mess, int meret)
{
    WLOG("entry point...");
    WLOG("IP address: " + string(_ip_address));
    WLOG("IP port: " + to_string(_ip_port));
    int sd;
    struct sockaddr_in server;

    sd = socket(AF_INET,SOCK_STREAM,0);
    server.sin_family = AF_INET;
    inet_pton(PF_INET, _ip_address, &(server.sin_addr));
    server.sin_port = htons(_ip_port);
    // küldés
    WLOG("create socket and connecting...");
    int ret = connect(sd, (const sockaddr *)&server, sizeof(server));
    if (ret == -1)
    {
        WLOG("connecting to controller error.");
        return ret;
    }
    WLOG("send staring...");
    ret = send(sd, mess, meret, 0);
    if (ret != meret)
    {
        WLOG("send error: " + to_string(ret));
        close(sd);
        return ret;
    }
    WLOG("send completed, create receive buffer and recv starting...");
    // vétel
    unsigned char *buf = (unsigned char*)malloc(sizeof(unsigned char)*200);
    int vett = recv(sd, buf, 200, 0);
    if (_cp5200_debug > 0)
    {
        for (int i=0; i<vett; i++)
        {
            cout << __cint2bytes(buf[i], 2) << " ";
        }
        cout << endl;
    }
    WLOG("receive completed, received bytes number: " + to_string(vett) + ", calculate starting...");
    if (vett >= 13)
    {
        string vala = __cint2bytes(buf[12], 2);
        ret = stoi(vala);
        if (ret != 0)
        {
            WLOG("receive error from controller: " + to_string(ret));
        }
    }
    else
    {
        WLOG("receive error: " + to_string(vett) + "bytes not eonugh.");
        free(buf);
        close(sd);
        return 10;
    }
    WLOG("result: " + to_string(ret));
    free(buf);
    close(sd);
    WLOG("endpoint, return:" + to_string(ret));
    return ret;
}

int _MessageSend_rs232(char * mess, int meret)
{
    WLOG("entry point...");
    WLOG("RS232 port: " + string(_rs232_serport));
    WLOG("RS232 baud rate: " + to_string(_rs232_baud_int));
    int ret = -1;
    uart0_filestream = open(_rs232_serport, O_RDWR | O_NOCTTY | O_NDELAY);		//Open in non blocking read/write mode
    if (uart0_filestream == -1)
    {
	//ERROR - CAN'T OPEN SERIAL PORT
	WLOG("Error - Unable to open UART.  Ensure it is not in use by another application.");
        return ret;
    }
    struct termios options;
    tcgetattr(uart0_filestream, &options);
    options.c_cflag = _rs232_baud | CS8 | CLOCAL | CREAD;		//<Set baud rate
    options.c_iflag = IGNPAR;
    options.c_oflag = 0;
    options.c_lflag = 0;
    tcflush(uart0_filestream, TCIFLUSH);
    tcsetattr(uart0_filestream, TCSANOW, &options);
    // küldés
    WLOG("send staring...");
    ret = write(uart0_filestream, mess, meret);
    if (ret != meret)
    {
        WLOG("send error: " + to_string(ret));
        return ret;
    }
    WLOG("send completed.");
    close(uart0_filestream);
    WLOG("endpoint, return:" + to_string(ret));
    return ret;
}

int _MessageSend(string hexik, int kuldo)
{
    WLOG("entry point...");
    int ret = -1;
    string hexi = "";
    string chksum = _getCRC16(hexik, 0);
    int netpack = hexik.length() / 2;
    netpack += 2;    // checksum miatt
// <editor-fold desc="add different header-end to hex, and transcoding for rs232">
    if (_cp5200_send_mode == 0) // netes csomageleje és vége
    {
        hexi =  ncid +
                __cint2bytes(netpack, 4) +
                resv + hexik + chksum;
    }
    else                        // soros csomageleje és vége
    {
        hexi = sbeg + _addesc(hexik + chksum) + sveg;
        //hexi = sbeg + hexik + chksum + sveg;
    }
// </editor-fold>
    WLOG("packed sendable hex: " + hexi);
// <editor-fold desc="convert hex string to buffer">
    int fullhossz = hexi.length();
    stringstream convertStream;
    char *answer = (char*)malloc(sizeof(char)*fullhossz);
    int offset = 0, i = 0;      
    while (offset < hexi.length()) 
    {
        unsigned int buffer;
        convertStream << hex << hexi.substr(offset, 2);         
        convertStream >> hex >> buffer;
        answer[i] = static_cast<char>(buffer);
        offset += 2;
        i++;
        // empty the stringstream
        convertStream.str(string());
        convertStream.clear();
    }    
// </editor-fold>
// <editor-fold desc="send buffer different modes">
    switch (_cp5200_send_mode)
    {
        case 0:
        {
            ret = _MessageSend_net(answer, fullhossz);
            break;
        }
        case 1:
        {
            ret = _MessageSend_rs232(answer, fullhossz);
            break;
        }
    }
    free(answer);
// </editor-fold>
    WLOG("endpoint, return: " + to_string(ret));
    return ret;
}
// </editor-fold>

// <editor-fold desc="Syncing date and time from host with specified controller">
// <editor-fold desc="Sending time synchronization packet to specified controller">
// pakk[0] = second
// pakk[1] = minute
// pakk[2] = hour
// pakk[3] = dayofweek
// pakk[4] = day
// pakk[5] = month
// pakk[6] = year-2000
int _generate_sync_time(unsigned int pakk[7])
{
    WLOG("entry point...");
    //string hexi = "FFFFFFFF0F000000683201470100";
    string hexi = "683201470100";
    for (int i = 0; i < 7; i++)
    {
        hexi += __cint2bytes(pakk[i], 2);
    }
    WLOG("sendable hex: " + hexi);
    int ret = _MessageSend(hexi, 100);
    WLOG("endpoint");
    return ret;
}
// </editor-fold>

extern "C" int SyncTime()
{
    WLOG("entry point...");
    WLOG("get host datetime...");
    unsigned int ipaki[7] = {0,0,0,0,0,0,0};
    // get local time
    time_t rawtime;
    tm * timeinfo;
    time(&rawtime);
    timeinfo=localtime(&rawtime);
    ipaki[0] = timeinfo->tm_sec;
    ipaki[1] = timeinfo->tm_min;
    ipaki[2] = timeinfo->tm_hour;
    ipaki[3] = timeinfo->tm_wday;
    ipaki[4] = timeinfo->tm_mday;
    ipaki[5] = timeinfo->tm_mon + 1;
    ipaki[6] = timeinfo->tm_year - 100;
    if (_cp5200_debug > 0)
    {
        WLOG("datetime params:");
        cout << "0 seconds: " << ipaki[0] << endl;
        cout << "1 minutes: " << ipaki[1] << endl;
        cout << "2 hours: " << ipaki[2] << endl;
        cout << "3 weekday: " << ipaki[3] << endl;
        cout << "4 monthday: " << ipaki[4] << endl;
        cout << "5 month: " << ipaki[5] << endl;
        cout << "6 year: " << ipaki[6] << endl;
    }
    int ret = _generate_sync_time(ipaki);
    WLOG("endpoint");
    return ret;
}
// </editor-fold>

// <editor-fold desc="Get or set brightness same all for 24h the specified controller">
int _generate_set_brightness(unsigned int brigi)
{
    WLOG("entry point...");
    //string hexi = "683201470100";
    string hexi = "6832FF460100";
    for (int i = 0; i < 24; i++)
    {
        hexi += __cint2bytes(brigi, 2);
    }
    WLOG("sendable hex: " + hexi);
    int ret = _MessageSend(hexi, 200);
    WLOG("endpoint");
    return ret;
}

int _generate_get_brightness()
{
    int ret = 0;
    return ret;
}

extern "C" int BrightnessControl(int GetSet, int Bri)
{
    int ret = 0;
    
    if ((Bri < 0) || (Bri > 31)) // ha a fényerő kisebb, mint nulla vagy nagyobb, mint 31 akkor auto
    {
        Bri = 255;
    }
    if (GetSet == 0) //set brightness
    {
        unsigned int brigi = (unsigned int)Bri;
        ret = _generate_set_brightness(brigi);
    }
    else // get brightness
    {
        
    }
    return ret;
}
// </editor-fold>

// <editor-fold desc="Sending pure binary file to specified controller">
/*extern "C" int SendBinaryFile(char * pFilename)
{
    //HOST = ipaddress;
    //PORT = ipport;
    char * fn = pFilename;
    if (!__get_fexist(fn))
    {
        if (_cp5200_debug > 0)
        {
            cout << "SendBinaryFile >> Specified file '" << fn << "' does not exists!" << endl;
        }
        return 10;
    }
    FILE *img = fopen(fn, "rb");
    if (img==NULL) 
    {
        if (_cp5200_debug > 0)
        {
            cout << "File open error!" << endl;
        }
        //fputs ("File error",stderr); 
        return 11;
    }
    fseek(img, 0, SEEK_END);
    unsigned long filesize = ftell(img);
    char *buffer = (char*)malloc(sizeof(char)*filesize);
    if (buffer == NULL) 
    {
        if (_cp5200_debug > 0)
        {
            cout << "Memory allocation error!" << endl;
        }
        //fputs ("Memory error",stderr); 
        return 12;
    }
    rewind(img);
    size_t result = fread(buffer, sizeof(char), filesize, img);
    if (result != filesize) 
    {
        if (_cp5200_debug > 0)
        {
            cout << "File reading error!" << endl;
        }
        //fputs ("Reading error",stderr); 
        return 13;
    }
    fclose(img);
    int ret = 0; //_MessageSend(buffer, filesize);
    free(buffer);
    return ret;
}*/
// </editor-fold>

// <editor-fold desc="Splitting display area to window(s) to specified controller">
extern "C" int SplitWindow(int nWndNo, int nWinC[], int nWinCS)
{
    WLOG("entry point...");
    // window validate
    int tmeret = nWinCS;
    double wn = (double)nWndNo;
    double es = (double)(tmeret/4);
    if (wn != es)
    {
        WLOG("bad window parameters, window number: " + to_string(wn) + ", array size/4: " + to_string(es));
        return 1;
    }
    if (_cp5200_debug > 0)
    {
        WLOG("window(s) number: " + to_string(wn) + ", window(s) parameters: ");
        for (size_t i=0; i<static_cast<size_t>(tmeret); i++)
            cout << i << ": " << nWinC[i] << endl;
    }
    int pack = 2 + (tmeret * 2);
    string hexi = "";
    hexi =  pact + cart + caid + prco + adin +          // always this
            __cint2bytes(pack, 4) +                     // packet data length
            "000001" +                                  // packet number 00, last packet number 00, text CC=01
            __cint2bytes(nWndNo, 2);                    // count of windows
    for (size_t i = 0; i < static_cast<size_t>(tmeret); i++)
    {
        hexi += __cint2bytes_lofo(nWinC[i], 4);
    }
    WLOG("sendable hex: " + hexi);
    int ret = _MessageSend(hexi, 1);
    WLOG("endpoint");
    return ret;
}
// </editor-fold>

// <editor-fold desc="Sending normal text to specified controller and window">
extern "C" int SendText(int nWndNo, char * pText, int nColor, int nFontSize, int nSpeed, int nEffect, int nStayTime, int nAlign)
{
    WLOG("entry point...");
    
    // Validate input parameters
    if (pText == NULL) {
        WLOG("Error: pText is NULL");
        return -1;
    }
    
    // Use original text directly - no conversion needed for ASCII
    string szoveg = "";
    if (pText[0] != 0)
    {
        szoveg = string(pText);
    }
    
    // Ensure text is not empty
    if (szoveg.empty()) {
        WLOG("Warning: Empty text, using default");
        szoveg = " ";
    }
    
    WLOG("Text to send: '" + szoveg + "'");
    
// <editor-fold desc="fő paraméterek kiszámolása">
    int szhossz = (int)(szoveg.length()*3);     // text length
    int pack = 7 + szhossz + 3;                 // text-packet length with subheader
    // color és font összerakása
    int fonts = nFontSize;
    int color = nColor;
    int fontcol = 10*color + fonts;
    
    // Convert fontcol to proper hex format
    string fc = __cint2bytes(fontcol, 2);
    WLOG("Font/Color: " + to_string(fontcol) + " -> " + fc);
// </editor-fold>
// <editor-fold desc="csomag összerakása">
    string hexi = "";
    hexi =  pact + cart + caid + prco + adin +  // always this
            __cint2bytes(pack, 4) +             // packet data length
            "000002" +                          // packet number 00, last packet number 00, text CC=02
            __cint2bytes(nWndNo, 2) +           // target window nomber
            __cint2bytes(nEffect, 2) +          // effect code
            __cint2bytes(nAlign, 2) +           // text align
            __cint2bytes(nSpeed, 2) +           // effect speed
            __cint2bytes_lofo(nStayTime, 4);    // stay time
    
    WLOG("Base packet: " + hexi);
    
    for (size_t i = 0; i < szoveg.length(); i++)   // create packet
    {
        string char_hex = __cint2bytes((unsigned char)szoveg[i], 2);
        hexi += fc + "00" + char_hex;
        WLOG("Char '" + string(1, szoveg[i]) + "' -> " + char_hex);
    }
    hexi += "000000";           // vége: 3byte 00
    WLOG("Final sendable hex: " + hexi);
    WLOG("Packet length: " + to_string(pack) + ", Total hex length: " + to_string(hexi.length()));
    
    // elküldjük
    int ret = _MessageSend(hexi, 2);
    WLOG("MessageSend returned: " + to_string(ret));
// </editor-fold>
    WLOG("endpoint");
    return ret;
}
// </editor-fold>

// <editor-fold desc="NEW Sending GIF picture to specified controller, packetlenght and window">
extern "C" int SendPicture(int nWndNo, int nPosX, int nPosY, char * pPictureFile, int nSpeed, int nEffect, int nStayTime)
{
    WLOG("entry point...");
// <editor-fold desc="check file exists">
    char * fn = pPictureFile;
    if (!__get_fexist(fn))
    {
        WLOG("Specified file '" + string(fn) + "' does not exists!");
        return 10;
    }
// </editor-fold>
// <editor-fold desc="file read">
    FILE *img;
    img = fopen(fn, "rb");
    if (img==NULL) 
    {
        WLOG("File open error!");
        return 11;
    }
    fseek(img, 0, SEEK_END);
    unsigned long filesize = ftell(img);
    char *gbuffer = (char*)malloc(sizeof(char)*filesize);
    if (gbuffer == NULL) 
    {
        WLOG("File memory allocation error!");
        return 12;
    }
    rewind(img);
    // store read data into buffer
    size_t result = fread(gbuffer, sizeof(char), filesize, img);
    if (result != filesize) 
    {
        WLOG("File reading error!");
        return 13;
    }
    fclose(img);
// </editor-fold>
// <editor-fold desc="fő paraméterek kiszámolása">
    int pbyteno = 200;      // one packet size
    int pack = 0;           // one packet size with subheader, if need
    int gpack = 0;          // one packet gif-data
    string hexi = "";       // work string
    vector <string> hexit;  // work string array
    int fileoffs = 0;       // actual offset of GIF file
    int reto = 0;           // summarized return value
    int tnop = 8;           // offset for total number of packages
    if (_cp5200_send_mode == 0) // net tnop
        tnop +=8;
    else
        tnop +=1;
    
    int firstpack = pbyteno - 11; // first img pack size = 189, utána n*pbyteno(200), remains last 
    
    int packno = 0;
    int tpackno = ((filesize - firstpack)/pbyteno) + 2; // total number of package

// </editor-fold>
// <editor-fold desc="make work string array">    
    stringstream convertStream;
    while (static_cast<unsigned long>(fileoffs) < filesize)
    {
        if (packno == 0)    // first pack
        {
            string header = "";
            if ((filesize + 11) <= firstpack)
            {
                pack = filesize + 11;
                gpack = filesize;
                tpackno = 1;
            }
            else
            {
                pack = pbyteno;
                gpack = firstpack;
            }
            header =  pact + cart + caid + prco + adin +        // always same
                    __cint2bytes(pack, 4) +                     // packed data length = GIF méret + 8
                    __cint2bytes(packno, 2) +                   // packet number
                    __cint2bytes(tpackno -1, 2);                         // last packet number
            string subheader = "";
            subheader = "03" +                                      // CC: image
                        __cint2bytes(nWndNo, 2) +                   // target window number
                        __cint2bytes(nEffect, 2) +                  // effect code, "00" draw (mode)
                        __cint2bytes(nSpeed, 2) +                   // speed
                        __cint2bytes_lofo(nStayTime, 4) +           // stay time
                        "01" +                                      // image format: GIF
                        __cint2bytes_lofo(nPosX, 4) +               // display X
                        __cint2bytes_lofo(nPosY, 4);                // display Y
            string gifh = "";
            for (int p = 0; p < gpack; p++)
            {
                convertStream << setfill('0') << setw(2) << hex << (int)static_cast<char>(gbuffer[p]);
                gifh += convertStream.str();
                convertStream.str(string());
                convertStream.clear();
            }
            hexi = header + subheader + gifh;
            hexit.push_back(move(hexi));
            
            fileoffs = firstpack;
            WLOG(to_string(fileoffs));
        }
        else                // többi csomag
        {
                         if ((filesize - static_cast<unsigned long>(fileoffs)) > 200)   // intermediate packs
            {
                string header = "";
                pack = pbyteno;
                gpack = pbyteno;
                header =  pact + cart + caid + prco + adin +        // always same
                        __cint2bytes(pack, 4) +                     // packed data length = GIF méret + 8
                        __cint2bytes(packno, 2) +                   // packet number
                        __cint2bytes(tpackno -1, 2);                         // last packet number
                string gifh = "";
                for (int p = 0; p < gpack; p++)
                {
                    convertStream << setfill('0') << setw(2) << hex << (int)static_cast<char>(gbuffer[p + static_cast<int>(fileoffs)]);
                    gifh += convertStream.str();
                    convertStream.str(string());
                    convertStream.clear();
                }
                hexi = header + gifh;
                hexit.push_back(move(hexi));

                fileoffs +=200;
                WLOG(to_string(fileoffs));
            }
            else                                // last pack
            {
                string header = "";
                                 pack = static_cast<int>(filesize - static_cast<unsigned long>(fileoffs));
                 gpack = static_cast<int>(filesize - static_cast<unsigned long>(fileoffs));
                header =  pact + cart + caid + prco + adin +        // always same
                        __cint2bytes(pack, 4) +                     // packed data length = GIF méret + 8
                        __cint2bytes(packno, 2) +                   // packet number
                        __cint2bytes(tpackno-1, 2);                         // last packet number
                string gifh = "";
                for (int p = 0; p < gpack; p++)
                {
                    convertStream << setfill('0') << setw(2) << hex << (int)static_cast<char>(gbuffer[p + static_cast<int>(fileoffs)]);
                    gifh += convertStream.str();
                    convertStream.str(string());
                    convertStream.clear();
                }
                hexi = header + gifh;
                hexit.push_back(move(hexi));

                fileoffs = filesize;
                WLOG(to_string(fileoffs));
            }
        }
        packno++;
        WLOG(to_string(packno));
    }
    WLOG("total package number: " + to_string(tpackno));
// </editor-fold>
// <editor-fold desc="send work string array">    
    for(string n : hexit) 
    {
        WLOG("sendable hex: " + n);
        reto += _MessageSend(n, 3);
    }
// </editor-fold>
    free(gbuffer);
    WLOG("endpoint");
    return reto;
}
// </editor-fold>

// <editor-fold desc="Send datetime visual placeholder to specified controller and window">
extern "C" int SendClock(int nWndNo, int nStayTime, int nCalType, int nFormat[], int nCont[], char * pText, int nColor[], int nFontSize)
{
    WLOG("entry point...");
    // Skip the problematic conversion entirely - use original text directly
    string szoveg = "";
    if (pText[0] != 0)
    {
        szoveg = string(pText);
    }
// <editor-fold desc="create main params">
    int tmeret = (int)(szoveg.length());    // text length
    int pack = 1 + 11 + tmeret;             // packet length: textlength+00+subheader length
    int netpack = pack + 11;                // netpacket length: pack+11 constant
    int fullhossz = netpack + 8;            // full length: netpacket+8 constant
    string formatb = "";
    for (int i = 0; i < 8; i++)                // create format, 2.bit branch 0: one line 1: multiline
    {
        formatb += to_string(nFormat[i]);
    }
    bitset<8> formatbs(formatb);
    unsigned long format = formatbs.to_ulong();
    string contenb = "";                  // create content
    for (int i = 0; i < 8; i++)
    {
        contenb += to_string(nCont[i]);
    }
    bitset<8> contenbs(contenb);
    unsigned long conten = contenbs.to_ulong();
    if (_cp5200_debug > 0)
    {
        cout << "SendClock >> formatb formatbs format: " << formatb << " " << formatbs << " " << format << endl;
        cout << "SendClock >> contenb contenbs conten: " << contenb << " " << contenbs << " " << conten << endl;
    }
// </editor-fold>
// <editor-fold desc="csomag összerakása">
    // packet hexa string elkészítése
    string hexi = "";
    hexi =  pact + cart + caid + prco + adin +          // always same
            __cint2bytes(pack, 4) +                     // packet data length
            "000005" +                                  // packet number 00, last packet number 00, clock CC=05
            __cint2bytes(nWndNo, 2) +                   // target window number
            __cint2bytes_lofo(nStayTime, 4) +           // stay time
            __cint2bytes(nCalType, 2) +                 // calendar type 0: gregorian(def) 1: moon 2: chinese moon 3: moon and sun
            __cint2bytes(format, 2) +                   // format
            __cint2bytes(conten, 2) +                   // content
            __cint2bytes(nFontSize, 2) +                // text size
            __cint2bytes(nColor[0], 2) +                // R
            __cint2bytes(nColor[1], 2) +                // G
            __cint2bytes(nColor[2], 2);                 // B
    for (size_t i = 0; i < static_cast<size_t>(tmeret); i++)            // make text content
    {
        hexi += __cint2bytes(szoveg[i], 2);
    }
    hexi += "00";                            // end: 1byte 00
    WLOG("sendable hex:" + hexi);
// </editor-fold>
    // küldés
    int ret = _MessageSend(hexi, 5);
    WLOG("endpoint");
    return ret;
}
// </editor-fold>

