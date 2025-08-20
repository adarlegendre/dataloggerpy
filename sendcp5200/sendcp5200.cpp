/* 
 * File:   void sendcp5200.cpp
 * Author: Misi
 *
 * Created on 2017. február 17., 8:43
 * V2.0 2017-06-15 mihint
 * V2.5 Rebuild on bookworm 2025-02-26
 * V3.0 Include brightness query and set 2025-03-13
 */

#include <cstdlib>
// kétindítás ellen
#include <sys/file.h>
#include <errno.h>
// cp5200 eljáráskünyvtár
#include <cp5200.h>

using namespace std;

/*
 * 
 */
int func0(char * filename) // send binary file
{
    int ret = 0; //SendBinaryFile(filename);
    return ret;
}

int func1(int wszam, int winpar[], int wpars) // split window
{
    int ret = SplitWindow(wszam, winpar, wpars);
    return ret;
}

int func2(int wszam, char * ptext, int col, int fs, int sp, int eff, int stay, int ali) // ssend text
{
    int ret = SendText(wszam, ptext, col, fs, sp, eff, stay, ali);
    return ret;
}

int func3(int wszam, int posx, int posy, char * pfile, int sp, int eff, int stay) // send GIF
{
    int ret = SendPicture(wszam, posx, posy, pfile, sp, eff, stay);
    return ret;
}

int func5(int wszam, int stay, int calt, int cform[], int ccont[], char * ptext, int szint[], int fs)
{
    int ret = SendClock(wszam, stay, calt, cform, ccont, ptext, szint, fs);
    return ret;
}

int func100() // synchronize datetime
{
    int ret = SyncTime();
    return ret;
}

int func200(int getset, int bri)
{
    int ret = BrightnessControl(getset, bri);
    return ret;
}

int main(int argc, char** argv) 
{
    int pid_file = open("/var/run/sendcp5200.pid", O_CREAT | O_RDWR, 0666);
    int rc = flock(pid_file, LOCK_EX | LOCK_NB);
    if(rc) 
    {
        if(EWOULDBLOCK == errno)
        {
            cout << "Another instance of sendcp5200 is running, program exit." << endl;
            return 1;
        }
    }
    int _debou = 0;
    int _debi = 0;
    int _comi = 0;
    string _hogyan = "via TCP-IP";
    // debug
    // end debug
    int _err = -1;
    if (argc > 4)
    {
        _debou = atoi(argv[1]);     // debug + output: 0: nodebug+net, 1: debug+net, 2: nodebug+rs232, 3: debug+rs232
        char * _ipa = argv[2];      // ip address OR COM port e.g. /dev/ttyAMA0, /dev/ttyUSB1, etc.
        int _port = atoi(argv[3]);  // port number OR baud rate - only standard!
        int _func = atoi(argv[4]);  // function number
        switch (_debou)
        {
            case 1:
            {
                _debi = 1;
                _comi = 0;
                break;
            }
            case 2:
            {
                _debi = 0;
                _comi = 1;
                break;
            }
            case 3:
            {
                _debi = 1;
                _comi = 1;
                break;
            }
        }
        if (_comi > 0)
        {
            _set_cp5200_send_mode(_comi);
            _set_cp5200_rs232comm(_ipa, _port);
            _hogyan = "via RS232";
        }
        else
        {
            _set_cp5200_ipcomm(_ipa, _port);
        }
        if (_debi > 0)      // if debug + output >0, parse values
        {
            cout << "Sending data " << _hogyan << " to the CP5200 controller (sendcp5200) program started." << endl;
            _get_cp5200_version();
            cout << "Argument list:" << endl;
            for (int i =0; i < argc; i++)
            {
                cout << i << ": " << argv[i] << endl;
            }
            _set_cp5200_debug();
        }
        string _funame = "";
        switch (_func)      // case and check function params, and execute if good
        {
            case 0:         // send binary file
            {
                _funame = "SendBinaryFile";
                if (argc != 6)
                {
                    _err = 100;
                    break;
                }
                _err = func0(argv[5]);
                break;
            }
            case 1:         // split window(s)
            {
                _funame = "SplitWindow";
                // parse windows data
                int wino = atoi(argv[5]);   // windows count
                int wipars = argc - 6;      // count of params
                int wipa[wipars];           // load params
                for (int i=6; i<argc; i++)  // array
                    wipa[i-6] = atoi(argv[i]);
                _err = func1(wino, wipa, wipars);
                break;
            }
            case 2:         // send text
            {
                _funame = "SendText";
                if (argc != 13)
                {
                    _err = 100;
                    break;
                }
                int wno = atoi(argv[5]);
                int col = atoi(argv[7]);
                int fs = atoi(argv[8]);
                int sp = atoi(argv[9]);
                int eff = atoi(argv[10]);
                int stay = atoi(argv[11]);
                int ali = atoi(argv[12]);
                //func2(char * ipa, int port, int wszam, char * ptext, int col, int fs, int sp, int eff, int stay, int ali)
                _err = func2(wno, argv[6], col, fs, sp, eff, stay, ali);
                break;
            }
            case 3:         // send GIF
            {
                _funame = "SendPicture";
                if (argc != 12)
                {
                    _err = 100;
                    break;
                }
                int wno = atoi(argv[5]);
                int posx = atoi(argv[6]);
                int posy = atoi(argv[7]);
                int sp = atoi(argv[9]);
                int eff = atoi(argv[10]);
                int stay = atoi(argv[11]);
                //func3(char * ipa, int port, int pach, int wszam, int posx, int posy char * pfile, int sp, int eff, int stay)
                _err = func3(wno, posx, posy, argv[8], sp, eff, stay);
                break;
            }
            case 5:         // send clock
            {
                _funame = "SendClock";
                if (argc != 29)
                {
                    _err = 100;
                    break;
                }
                int wno = atoi(argv[5]);    // window number
                int stay = atoi(argv[6]);   // stay time
                int calt = atoi(argv[7]);   // calendar type
                int cform[8];               // load calendar format
                for (int i=8; i<=15; i++)   // 
                    cform[i-8] = atoi(argv[i]);
                int ccont[8];               // load calendar content
                for (int i=16; i<=23; i++)  // 
                    ccont[i-16] = atoi(argv[i]);
                int fs = atoi(argv[24]);     // text size
                // 25: duma
                int szint[3];               // load RGB
                for (int i=26; i<=28; i++)  // 
                    szint[i-26] = atoi(argv[i]);
                _err = func5(wno, stay, calt, cform, ccont, argv[25], szint, fs);
                break;
            }
            case 100:       // synchronize date and time from host to controller
            {
                _funame = "SyncTime";
                if (argc != 5)
                {
                    _err = 100;
                    break;
                }
                _err = func100();
                break;
            }
            case 200:       // Get or set brightness same all for 24h the specified controller
            {
                _funame = "BrightnessControl";
                if (argc != 7)
                {
                    _err = 200;
                    break;
                }
                int getset = atoi(argv[5]); // 0: set
                int bri = atoi(argv[6]); // -1: auto, 0..31: set value
                _err = func200(getset, bri);
                break;
            }
            default:
            {
                cout << "Bad function argument!" << endl;
                break;
            }
        }
        switch (_err)
        {
            case -1:
            {
                cout << "Fatal error, return code: " << _err << endl;
                break;
            }
            case 0:
            {
                cout << _funame << " completed." << endl;
                break;
            }
            case 1:
            {
                if (_func == 100)
                    cout << _funame << " completed, because ###TimeSync return 1 if no error###." << endl;
                if (_func == 200)
                    cout << _funame << " completed, because ###Setbrightness return 1 if no error###." << endl;
                else
                    cout << _funame << " library error, return code: " << _err << endl;
                break;
            }
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
            case 13:
            {
                cout << _funame << " library error, return code: " << _err << endl;
                break;
            }
            case 100:
            {
                cout << _funame << " argument error, return code: " << _err << endl;
                break;
            }
            case 200:
            {
                cout << _funame << " argument error, return code: " << _err << endl;
                break;
            }
            default:
            {
                if (_comi > 0)
                    cout << "Sended byte number: " << _err << endl;
                else
                    cout << "Unknown error, return code: " << _err << endl;
                break;
            }
        }
    }
    else
    {
        //double miez = mean(2,3);
        //cout << "Középérték(2, 3): " << miez << endl;
        //getBinaryFile(111);
        cout << "sendcp5200 program do not run without (or too less) parameters." << endl << endl;
        cout << "All parameters basic structure:" << endl;
        cout << "sendcp5200 [debug+com] [IP address/comport] [port/baud] [data type] [type dep. params]" << endl << endl;
        cout << "Data type and params:" << endl << endl;
        cout << "Type 0: send binary file directly to controller" << endl;
        cout << "[full path name of binary file in quotation marks e.g. \"/home/user/data.bin\"]" << endl << endl;
        cout << "Type 1: split windows display" << endl;
        cout << "[amount of created windows, only integer number]" << endl;
        cout << "[created windows top left X coordinate only integer number]" << endl;
    }
    if (_debi > 0)
    {
        cout << "Sending data " << _hogyan << " to the CP5200 controller (sendcp5200) program end." << endl;
    }
    return 0;
}
