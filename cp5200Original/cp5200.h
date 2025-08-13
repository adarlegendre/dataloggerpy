/* 
 * File:   cp5200.h
 * Author: Misi
 *
 * Created on 2017. február 3., 9:38
 * V2.0 2017-06-15 mihint
 * V2.1 Rebuild 2020-10-09
 * V2.5 Rebuild on bookworm 2025-02-26
 * V3.0 Include brightness query and set 2025-03-13
 */

#ifndef CP5200_H
#define CP5200_H

#include <iostream>
#include <fstream>
#include <sys/types.h>   
#include <netinet/in.h>  
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>       
#include <math.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <cctype>
#include <iomanip>
#include <vector>
#include <unistd.h>
#include <pthread.h>
#include <errno.h>
#include <cstdlib>
#include <ctime>
#include <cwchar>
#include <bitset>
// file
#include <sys/stat.h>
#include <sys/mount.h>
// serial
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <termios.h>
// konvert
#include <iconv.h>
// egyeb
#include <algorithm>

using namespace std;

#define WLOG(val) if (_cp5200_debug > 0) cout << __FUNCTION__ << " >> " << val << endl
#define cplibmv 3
#define cplibsv 1

extern "C" void _get_cp5200_version();
extern "C" void _set_cp5200_debug();
extern "C" void _set_cp5200_send_mode(int sm);
extern "C" void _set_cp5200_ipcomm(char *ipcim, int ippor);
extern "C" void _set_cp5200_rs232comm(char *serpor, int sbaud);
extern "C" int SyncTime();
extern "C" int BrightnessControl(int GetSet, int Bri);
extern "C" int SplitWindow(int nWndNo, int nWinC[], int nWinCS);
extern "C" int SendText(int nWndNo, char * pText, int nColor, int nFontSize, int nSpeed, int nEffect, int nStayTime, int nAlign);
extern "C" int SendPicture(int nWndNo, int nPosX, int nPosY, char * pPictureFile, int nSpeed, int nEffect, int nStayTime);
extern "C" int SendClock(int nWndNo, int nStayTime, int nCalType, int nFormat[], int nCont[], char * pText, int nColor[], int nFontSize);
#endif /* CP5200_H */
