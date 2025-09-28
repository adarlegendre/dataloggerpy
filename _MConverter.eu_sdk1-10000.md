C-Power5200 SDK API Manual

> Version: V1.6
>
> 2015.05.28

Recension Log:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 56%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Version</p>
</blockquote></th>
<th><blockquote>
<p>Changes</p>
</blockquote></th>
<th><blockquote>
<p>Executor</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2009-8-11</p>
</blockquote></td>
<td><blockquote>
<p>V1.0</p>
</blockquote></td>
<td><blockquote>
<p>The first version</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2010-1-28</p>
</blockquote></td>
<td><blockquote>
<p>V1.1</p>
</blockquote></td>
<td><ol type="1">
<li><p>Add multi-window protocol data packing API</p></li>
<li><p>Add multi-window protocol serial and network simple use
API</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2010-5-22</p>
</blockquote></td>
<td><blockquote>
<p>V1.2</p>
</blockquote></td>
<td><p>Increase the following functions:：</p>
<ol type="1">
<li><p>CP5200_Program_AddLafPict</p></li>
<li><p>CP5200_Program_AddLafVideo</p></li>
<li><p>CP5200_Program_AddVariable</p></li>
<li><p>CP5200_MakeGetTypeInfoData</p></li>
<li><p>CP5200_ParseGetTypeInfoRet</p></li>
<li><p>CP5200_MakeGetTempHumiData</p></li>
<li><p>CP5200_ParseGetTempHumiRet</p></li>
<li><p>CP5200_MakeReadConfigData</p></li>
<li><p>CP5200_ParseReadConfigRet</p></li>
<li><p>CP5200_MakeWriteConfigData</p></li>
<li><p>CP5200_ParseWriteConfigRet</p></li>
<li><p>CP5200_RS232_GetTemperature</p></li>
<li><p>CP5200_RS232_GetTypeInfo</p></li>
<li><p>CP5200_Net_GetTemperature</p></li>
<li><p>CP5200_Net_GetTypeInfo</p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2011-02-24</p>
</blockquote></td>
<td><blockquote>
<p>V1.3</p>
</blockquote></td>
<td><blockquote>
<p>Increase the following functions:</p>
</blockquote>
<ol type="1">
<li><p>CP5200_MakeReadHWSettingData</p></li>
<li><p>CP5200_ParseReadHWSettingRet</p></li>
<li><p>CP5200_MakeWriteHWSettingData</p></li>
<li><p>CP5200_ParseWriteHWSettingRet</p></li>
<li><p>CP5200_RS232_ReadHWSetting</p></li>
<li><p>CP5200_RS232_WriteHWSetting</p></li>
<li><p>CP5200_Net_ReadHWSetting</p></li>
<li><p>CP5200_Net_WriteHWSetting</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2012-03-16</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Increase the following functions:</p>
</blockquote>
<ol type="1">
<li><p>CP5200_RS232_RemoveFile</p></li>
<li><p>CP5200_Net_RemoveFile</p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2012.08.04</p>
</blockquote></td>
<td><blockquote>
<p>V1.4</p>
</blockquote></td>
<td><blockquote>
<p>1. Increase the following functions:</p>
<p>CP5200_CommData_SetParam</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 56%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><p>CP5200_MakeReadRunningInfoData</p>
<p>CP5200_ParseReadRunningInfoRet</p>
<p>CP5200_MakeScreenTestData</p>
<p>CP5200_ParseScreenTestRet</p>
<p>CP5200_MakeInstantMessageData1</p>
<p>CP5200_MakeOpenFileData</p>
<p>CP5200_ParseOpenFileRet</p>
<p>CP5200_MakeGetDirentryData CP5200_ParseGetDirentryRet</p>
<p>CP5200_MakeReadFileNoData</p>
<p>CP5200_ParseReadFileNoRet</p>
<p>CP5200_MakeCloseFileNoData CP5200_ParseCloseFileNoRet</p>
<p>CP5200_CmmPacket_SetParam</p>
<p>CP5200_MakePlaySelectedPrgData1</p>
<p>CP5200_MakeSetZoneAndVariableData</p>
<p>CP5200_ParseSetZoneAndVariableRet</p>
<p>CP5200_MakeSendPureTextData</p>
<p>CP5200_ParseSendPureTextRet</p>
<p>CP5200_RS232_SetZoneAndVariable</p>
<p>CP5200_RS232_SendPureText</p>
<p>CP5200_Net_SetZoneAndVariable</p>
<p>CP5200_Net_SendPureText</p>
<p>CPowerBox_MakeSendClockOrTemperatureData</p>
<p>CPowerBox_ParseSendClockOrTemperatureRet</p>
<p>CPowerBox_MakeSetAloneProgramData</p>
<p>CPowerBox_ParseSetAloneProgramRet</p>
<p>CPowerBox_MakeQueryProgramData CPowerBox_ParseQueryProgramRet
CPowerBox_MakeSetScheduleData</p>
<p>CPowerBox_ParseSetScheduleRet</p>
<p>CPowerBox_MakeDeleteScheduleData</p>
<p>CPowerBox_ParseDeleteScheduleRet</p>
<p>CPowerBox_MakeGetScheduleData</p>
<p>CPowerBox_ParseGetScheduleRet</p>
<p>CPowerBox_RS232_SendClockOrTemperature</p>
<p>CPowerBox_RS232_SetAloneProgram</p>
<p>CPowerBox_RS232_QueryProgram</p>
<p>CPowerBox_RS232_SetSchedule</p>
<p>CPowerBox_RS232_DeleteSchedule</p>
<p>CPowerBox_RS232_GetSchedule</p>
<p>CPowerBox_Net_SendClockOrTemperature</p>
<p>CPowerBox_Net_SetAloneProgram CPowerBox_Net_QueryProgram</p></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 56%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>CPowerBox_Net_SetSchedule</p>
<p>CPowerBox_Net_DeleteSchedule</p>
<p>CPowerBox_Net_GetSchedule</p>
<p>CP5200_Net_SetBindParam</p>
<p>2. Perfect interface parameters</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2012-05-08</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_Program_AddFormattedText</p>
<p>CP5200_Program_AddFormattedTextW</p>
<p>CP5200_TextToImage</p>
<p>CP5200_TextToImageW</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2013/8/5</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_MakeReadSoftwareSwitchInfoData</p>
<p>CP5200_ParseReadSoftwareSwitchInfoRet</p>
<p>CP5200_MakeWriteSoftwareSwitchInfoData</p>
<p>CP5200_ParseWriteSoftwareSwitchInfoRet</p>
<p>CP5200_RS232_ReadSoftwareSwitchInfo</p>
<p>CP5200_RS232_WriteSoftwareSwitchInfo</p>
<p>CP5200_Net_ReadSoftwareSwitchInfo</p>
<p>CP5200_Net_WriteSoftwareSwitchInfo</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2014/1/23</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_Program_AddFormattedTextEx</p>
<p>CP5200_TextToImageEx</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2015/3/17</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_MakeQueryControllerInfo</p>
<p>CP5200_ParseQueryControllerInfoRet</p>
<p>CP5200_Net_QueryControllerInfo</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2015/4/1</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_RS232_ReadNetworkParam</p>
<p>CP5200_RS232_WriteNetworkParam CP5200_RS232_Upgrade</p>
<p>CP5200_Net_ReadNetworkParam</p>
<p>CP5200_Net_WriteNetworkParam</p>
<p>CP5200_Net_Upgrade</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2015/5/18</p>
</blockquote></td>
<td></td>
<td><p>Increase the following functions:</p>
<blockquote>
<p>CP5200_MakeSendMultiProtocol</p>
<p>CP5200_ParseSendMultiProtocoltRet</p>
<p>CP5200_Net_SendMultiProtocol</p>
<p>CP5200_RS232_SendMultiProtocol</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2015/5/27</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Modify the following functions:</p>
<p>CP5200_MakeSendPictureData</p>
<p>CP5200_RS232_SendPicture</p>
<p>CP5200_Net_SendPicture</p>
<p>Increase the following functions: CP5200_MakeSendSimpleImageData</p>
<p>CP5200_ParseSendSimpleImageRet</p>
<p>CP5200_RS232_SendSimpleImageData</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>CP5200_Net_SendSimpleImageData</td>
<td></td>
</tr>
</tbody>
</table>

# Basic definition  {#basic-definition}

1.1. Data type

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 24%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Data Type</p>
</blockquote></th>
<th><blockquote>
<p>Definition</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Object Handle</p>
</blockquote></td>
<td><blockquote>
<p>HOBJECT</p>
</blockquote></td>
<td>void*</td>
</tr>
</tbody>
</table>

1.2. Classification of API function

>  Creating program file API function
>
>  Create playbill file API function
>
>  Communication data API function

1.3. Common operating steps

1.  Create program file

2.  Create playbill file

3.  Use communication data API to generate command data, then send the
    data to controller and receive return data, also use communication
    data API to parse the return data and get the result。

> Note: control card only search program files "playbill.lpp" when it
> starts, if the generated is saved as other file name, when the program
> single-file(".lpp") sent to the card ,you need to change
>
> the file name "playbill.lpp".

1.4. Communication protocol

C-Power5200 controller support RS232/485 and network communication

> mode.

1.4.1. RS232/485

> Communication start code is 0xA5, end code is 0xAE。Between start code
> and end code, if there is 0xA5, 0xAA or 0xAE, it should be converted
> to two code。
>
> When PC send data to controller, convert one code to two code:
>
> 0xA5  0xAA 0x05
>
> 0xAA  0xAA 0x0A
>
> 0xAE  0xAA 0x0E
>
> When PC receive data from controller, convert two code to one code:
>
> 0xAA 0x05  0xA5
>
> 0xAA 0x0A  0xAA
>
> 0xAA 0xAE  0xAE

1.4.2. Network

> Need 4 bytes controller network ID code at the beginning of data
>
> to be sent to controller.

1.5. Special effect for text and picture

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th><blockquote>
<p>Effect</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td><blockquote>
<p>Draw</p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>Open from left</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>Open from right</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>Open from center(Horizontal)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>Open from center(Vertical)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Shutter(vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>Move to left</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>7</th>
<th><blockquote>
<p>Move to right</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>Move up</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>Move down</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>Scroll up</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11</td>
<td><blockquote>
<p>Scroll to left</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12</td>
<td><blockquote>
<p>Scroll to right</p>
</blockquote></td>
</tr>
<tr class="even">
<td>13</td>
<td><blockquote>
<p>Flicker</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14</td>
<td><blockquote>
<p>Continuous scroll to left</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15</td>
<td><blockquote>
<p>Continuous scroll to right</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16</td>
<td><blockquote>
<p>Shutter(horizontal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>17</td>
<td><blockquote>
<p>Clockwise open out</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>18</td>
<td><blockquote>
<p>Anticlockwise open out</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>Windmill</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>20</td>
<td><blockquote>
<p>Windmill（anticlockwise）</p>
</blockquote></td>
</tr>
<tr class="even">
<td>21</td>
<td><blockquote>
<p>Rectangle forth</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>22</td>
<td><blockquote>
<p>Rectangle entad</p>
</blockquote></td>
</tr>
<tr class="even">
<td>23</td>
<td><blockquote>
<p>Quadrangle forth</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>24</td>
<td><blockquote>
<p>Quadrangle endtad</p>
</blockquote></td>
</tr>
<tr class="even">
<td>25</td>
<td><blockquote>
<p>Circle forth</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26</td>
<td><blockquote>
<p>Circle endtad</p>
</blockquote></td>
</tr>
<tr class="even">
<td>27</td>
<td><blockquote>
<p>Open out from left up corner</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>28</td>
<td><blockquote>
<p>Open out from right up corner</p>
</blockquote></td>
</tr>
<tr class="even">
<td>29</td>
<td><blockquote>
<p>Open out from left bottom corner</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>30</td>
<td><blockquote>
<p>Open out from right bottom corner</p>
</blockquote></td>
</tr>
<tr class="even">
<td>31</td>
<td><blockquote>
<p>Bevel open out</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>32</td>
<td><blockquote>
<p>AntiBevel open out</p>
</blockquote></td>
</tr>
<tr class="even">
<td>33</td>
<td><blockquote>
<p>Enter into from left up corner</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>34</td>
<td><blockquote>
<p>Enter into from right up corner</p>
</blockquote></td>
</tr>
<tr class="even">
<td>35</td>
<td><blockquote>
<p>Enter into from left bottom corner</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>36</th>
<th><blockquote>
<p>Enter into from lower right corner</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>37</td>
<td><blockquote>
<p>Bevel enter into</p>
</blockquote></td>
</tr>
<tr class="even">
<td>38</td>
<td><blockquote>
<p>AntiBevel enter into</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>39</td>
<td><blockquote>
<p>Horizontal zebra crossing</p>
</blockquote></td>
</tr>
<tr class="even">
<td>40</td>
<td><blockquote>
<p>Vertical zebra crossing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>41</td>
<td><blockquote>
<p>Mosaic(big)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>42</td>
<td><blockquote>
<p>Mosaic(small)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>43</td>
<td><blockquote>
<p>Radiation(up)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>44</td>
<td><blockquote>
<p>Radiation(downwards)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>45</td>
<td><blockquote>
<p>Amass</p>
</blockquote></td>
</tr>
<tr class="even">
<td>46</td>
<td><blockquote>
<p>Drop</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>47</td>
<td><blockquote>
<p>Combination(Horizontal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>48</td>
<td><blockquote>
<p>Combination(Vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>49</td>
<td><blockquote>
<p>Backout</p>
</blockquote></td>
</tr>
<tr class="even">
<td>50</td>
<td><blockquote>
<p>Screwing in</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>51</td>
<td><blockquote>
<p>Chessboard(horizontal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>52</td>
<td><blockquote>
<p>Chessboard(vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>53</td>
<td><blockquote>
<p>Continuous scroll up</p>
</blockquote></td>
</tr>
<tr class="even">
<td>54</td>
<td><blockquote>
<p>Continuous scroll down</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>55</td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td>56</td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>57</td>
<td><blockquote>
<p>Gradual bigger(up)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>58</td>
<td><blockquote>
<p>Gradual smaller(down)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>59</td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td>60</td>
<td><blockquote>
<p>Gradual bigger(vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>61</td>
<td><blockquote>
<p>Flicker(horizontal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>62</td>
<td><blockquote>
<p>Flicker(vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>63</td>
<td><blockquote>
<p>Snow</p>
</blockquote></td>
</tr>
<tr class="even">
<td>64</td>
<td><blockquote>
<p>Scroll down</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>65</td>
<td><blockquote>
<p>Scroll from left to right</p>
</blockquote></td>
</tr>
<tr class="even">
<td>66</td>
<td><blockquote>
<p>Open out from top to bottom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>67</td>
<td><blockquote>
<p>Sector expand</p>
</blockquote></td>
</tr>
<tr class="even">
<td>68</td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>69</td>
<td><blockquote>
<p>Zebra crossing (horizontal)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>70</td>
<td><blockquote>
<p>Zebra crossing (Vertical)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>32768</td>
<td><blockquote>
<p>Random effect</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

1.  6.Text extend tag

The Text of contain extend tags may contain extend tags as below and all
extend tag must be write in lowercase letters.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Extend sign</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;size&gt;</td>
<td><blockquote>
<p>Designate the size of letters , must append attribute value,
otherwise it will be ignore,if the attribute</p>
<p>value is inoperative,it will be ignore</p>
<p>also.Attribute value is the size of letter, virtual</p>
<p>value as below：</p>
<p>&lt;size=8&gt; : 8 lattice letter</p>
<p>&lt;size=16&gt; : 16 lattice letter</p>
<p>&lt;size=24&gt; : 24 lattice letter</p>
<p>&lt;size=32&gt; : 32 lattice letter</p>
</blockquote></td>
</tr>
<tr class="even">
<td>&lt;color&gt;</td>
<td><blockquote>
<p>Designate the color of letters , must append</p>
<p>attribute value, otherwise it will be ignore,if the attribute value
is inoperative,it will be ignore</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>also.Attribute value is the color of RGB hex</p>
<p>value ,for example：</p>
<p>&lt;color=#ff0000&gt; : Red</p>
<p>&lt;color=#00ff00&gt; : Green</p>
<p>&lt;color=#0000ff&gt; : Blue</p>
</blockquote></td>
</tr>
<tr class="even">
<td>&lt;p&gt;</td>
<td><blockquote>
<p>Newline</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>&lt;align&gt;</td>
<td><blockquote>
<p>The level of alignment , must append attribute value, otherwise it
will be ignore,if the attribute value is inoperative,it will be ignore
also.Virtual value</p>
<p>as below：</p>
<p>&lt;align=left&gt; : left Alignment</p>
<p>&lt;align=center&gt; ：center Alignment</p>
<p>&lt;align=right&gt; ：right Alignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>&lt;font&gt;</td>
<td><blockquote>
<p>Designate the font style of letters , must append attribute value,
otherwise it will be ignore,if the attribute value is inoperative,it
will be ignore also.Attribute value is the size of letter, virtual</p>
<p>value as below：</p>
<p>&lt;font=0&gt; : Default font &lt;font=1&gt; : Font 1</p>
<p>……</p>
<p>&lt;font=7&gt; : Font 7</p>
</blockquote></td>
</tr>
</tbody>
</table>

7.  Font size code and font style

    1.  Font size code

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th><blockquote>
<p>Font Size(lattice)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>24</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>32</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>40</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>48</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>56</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Font style code

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th><blockquote>
<p>Font style</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td><blockquote>
<p>Font 0 defaule font</p>
</blockquote></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>Font 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>Font 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>Font 3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>Font 4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Font 5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>Font 6</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>Font 7</p>
</blockquote></td>
</tr>
</tbody>
</table>

Note：If no special instructions, the parameter of the function in this
document called

> \"nFontSize\" was defined in the following format:
>
> Byte 0\~1：font size（lattice），如 8、12、24、32、40、48、56
>
> Byte 2：Bit 0\~2，font style code；
>
> Bit 3，Whether the specified font to use for each character (0 default
> font, 1 specify the font with each character), and add tagtext program
> is set to 1, others it is set to 0;
>
> Bit4\~7，Resvered.
>
> Byte 3：Resvered

8.  Font color code

One-byte font color code:

It can express 8 kinds of color. Use each one bit to represent
red、green、blue.

The lowest stands for red

The last but one stands for green The antepenultimate stands for blue 3
One-byte font color code:

It can express all kinds of color. Use each one byte to represent
red、green、blue.

9.  Picture effect code

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Picture effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Center</td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>Zoom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>Stretch</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>tile</p>
</blockquote></td>
</tr>
</tbody>
</table>

10. Clock format and display content

Clock format： Represent by one byte：

bit 0: Signal timing(0: 12signal timing；1: 24 signal timing) bit 1:
Year by bit(0: 4 bit；1: 2 bit) bit 2: Line folding(0: single-row；1:
multi-row) bit 3\~5: Reserved(set to 0) bit 6: Show time scale "Hour
scale、Minute scale" bit 7: Reserved(set to 0)

Clock display content：

Represent by one byte： Ascertain the display content by bit:

bit 7: pointer bit 6: week bit 5: second bit 4: minute bit 3: hour bit
2: day bit 1: month bit 0: year

1.11. Simple picture data format

> Data composition：

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data head</p>
</blockquote></th>
<th><blockquote>
<p>Red data(optional)</p>
</blockquote></th>
<th>Green data(optional)</th>
<th><blockquote>
<p>Blue data(optional)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Data head description：

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 19%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th>3</th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>identify</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>width</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>height</p>
</blockquote></td>
<td><blockquote>
<p>property</p>
</blockquote></td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Data name</th>
<th><blockquote>
<p>Data size(byte)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Identify</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>Set to “I1”。</td>
</tr>
<tr class="even">
<td>Width</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>The width of the picture, low byte previous(little endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Height</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>The height of the picture,low byte previous(little endian)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Property</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The gray-scale and color of the picture</p>
<p>Bit0: Whether exist red data, exist when 1.</p>
<p>Bit1: Whether exist green data, exist when 1.</p>
<p>Bit2: Whether exist blue data, exist when 1.</p>
<p>Bit3: Reserved, set to 0.</p>
<p>Bit4~7: Gray-scale, only support 0 and 7 now.</p>
<p>0: 2 levels gray, Each lattic data use 1 bit.</p>
<p>7: 256 levels gray, Each lattic data use 8 bit.</p>
<p>Each line of the picture data is aligned by byte. As for 2 levels
gray picture, when the line data is not enough for 8 bit, add 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Reserved</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>Set 0</td>
</tr>
</tbody>
</table>

> Data description：

The color of the data is order by red、green、blue. If the identify bit
of the property is 0, the color data is not exist.

For one color data, order by " left to right, top to bottom". First put
the data to the first line, then second line and so on.

1.12. Global zone message format

Each zone take 16 bytes, the format as below:

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th>3</th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
<th><blockquote>
<p>8</p>
</blockquote></th>
<th><blockquote>
<p>9</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>B</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>F</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>Type</p>
</blockquote></td>
<td><blockquote>
<p>Mode</p>
</blockquote></td>
<td><blockquote>
<p>x</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cx</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cy</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>ItemPropData</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>Data name</th>
<th><blockquote>
<p>Data size(byte)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1：Show text</p>
<p>2：Show specify picture file</p>
<p>3：Clock</p>
<p>4：Temperature</p>
<p>5：Humidity</p>
<p>6：Hint text(After the ’\n’)</p>
<p>7：Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Mode</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Have different meanings according to the window mode.</p>
<p>When the window mode is 1 or 6 means text align mode.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>When window mode is 2 means the picture show effect:</p>
<p>0: Center 1:zoom 2:stretch 3:tile</p>
<p>Ignore the other window mode right now,set to 0 default.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Start point X, high byte previous(big endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Start point Y, high byte previous(big endian)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cx</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Zone width, high byte previous(big endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>cy</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Zone height, high byte previous(big endian)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ItemPropData</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>The property value of the zone, it depends on the window mode.</p>
</blockquote></td>
</tr>
</tbody>
</table>

ItemPropData particular description

1.Show text

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>B</p>
</blockquote></th>
<th>C</th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>F</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>start</p>
</blockquote></td>
<td><blockquote>
<p>end</p>
</blockquote></td>
<td colspan="2">Stay</td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Data</p>
<p>Size(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Start</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Start number,valid value: 1～100</p>
</blockquote></td>
</tr>
<tr class="even">
<td>End</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>End number,valid value: 1～100</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Stay</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Stay time of each valid variable in second. High byte previous(big
endian)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Font color</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~3：Font size</p>
<p>0：8 lattic</p>
<p>1：12 lattic</p>
<p>2：16 lattic</p>
<p>3：24 lattic</p>
<p>4：32 lattic</p>
<p>5：40 lattic</p>
<p>6：48 lattic</p>
<p>7：56 lattic</p>
<p>8：64 lattic</p>
<p>Bit4~6：Color</p>
<p>0：Black</p>
<p>1：Red</p>
<p>2：Green</p>
<p>3：Yellow</p>
<p>4：Blue</p>
<p>5：Mauve</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><p>6：Cyan</p>
<p>7：White</p>
<p>Bit7：Whether invert color，1 is yes</p></td>
</tr>
</tbody>
</table>

2.Show specify picture file

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>B</p>
</blockquote></th>
<th>C</th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th>F</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>Start</p>
</blockquote></td>
<td><blockquote>
<p>End</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay</p>
</blockquote></td>
<td>Reserved</td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Data</p>
<p>Size(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Start</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Start number,valid value: 1～100</p>
</blockquote></td>
</tr>
<tr class="even">
<td>End</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>End number,valid value: 1～100</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Stay</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Stay time of each valid variable in second. High byte previous(big
endian)</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.Clock

4.Temperature

5.Humidity

6.Hint text

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>B</p>
</blockquote></th>
<th>C</th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>F</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hint window number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay</p>
</blockquote></td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Data</p>
<p>Size(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The window number</p>
<p>of hint</p></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Mark which window need this hint by bit,1 is hint, 0 is not</p>
<p>Bit 0：window number 1</p>
<p>Bit 1：window number 2</p>
<p>……</p>
<p>Bit 15: window number 16</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Stay</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Stay time of each valid variable in second. High byte previous(big
endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Font color</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>See the “Font color” in “1. Show text”</p>
</blockquote></td>
</tr>
</tbody>
</table>

Note：

1.  It will ignore when the window number of hint is set to "6.hint
    > text".

2.  When the variable data of the window number of hint doesn't have'\n'
    > or have none data

> after the '\n', this variable will not take part in the hint.
>
> 3.When synchronization stay time equals the max time of switch window
> div the number of the hint window.

7\. Time

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th>B</th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th>F</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>Time number</p>
</blockquote></td>
<td><blockquote>
<p>Format</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay</p>
</blockquote></td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 15%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Font size(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Time number</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Time number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Format</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: “mm:ss”</p>
<p>1: “mm:ss:nn” 2: “hh:mm:ss”</p>
<p>3: “hh:mm:ss:nn”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Stay</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>Stay time of each valid variable in second. High byte previous(big
endian)</td>
</tr>
<tr class="even">
<td>Font color</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>See the “Font color” in “1. Show text”</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.13. Window position and property

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
<th><blockquote>
<p>8</p>
</blockquote></th>
<th><blockquote>
<p>9</p>
</blockquote></th>
<th><blockquote>
<p>A</p>
</blockquote></th>
<th><blockquote>
<p>B</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>D</p>
</blockquote></th>
<th><blockquote>
<p>E</p>
</blockquote></th>
<th><blockquote>
<p>F</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x00</td>
<td><blockquote>
<p>x</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cx</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>cy</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>Window property</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 16%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Data</p>
<p>Size(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>x</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Window start point x, high byte previous (big endian).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>y</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Window start point Y, high byte previous (big endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>cx</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Window width.High byte previous (big endian).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Cy</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Window height.High byte previous (big endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Window property</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Window default type and parameters.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Window property is represent by 8 bytes：

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th>1</th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>mode</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Parameter</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

The definition of the window mode：

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Mode value</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>Blank(Show nothing)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Clock、calendar</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Temperature、Humidity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Picture、Reference of the picture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Other</p>
</blockquote></td>
<td>Reserved</td>
</tr>
</tbody>
</table>

The parameter has different values according to the the mode.There are
all the modes's parameters. All reserved position should be set 0x00.

Blank type

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th>5</th>
<th>6</th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Reserved</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Text type

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th>4</th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th><blockquote>
<p>6</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>mode</p>
</blockquote></td>
<td><blockquote>
<p>Font size</p>
</blockquote></td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td><blockquote>
<p>Speed</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay time</p>
</blockquote></td>
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th>Length(BYTE)</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>mode</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>See in ‘1.7’</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font size</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>Bit0~2: Font size</p>
<blockquote>
<p>0x00: 8 lattice（Only english）</p>
<p>0x01: 12 lattice（Only english）</p>
<p>0x02: 16 lattice</p>
<p>0x03: 24 lattice</p>
<p>0x04: 32 lattice</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>Bit0~2: Font color</p>
<p>0x01: Red</p>
<p>0x02: Green</p>
<p>0x03: Yellow</p>
<p>0x04: Blue</p>
<p>Red、green、blue can make up another color by bit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Clock/Calendar type

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th>6</th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td>2</td>
<td>Font size</td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay time</p>
</blockquote></td>
<td>calendar</td>
<td>Format</td>
<td>Content</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Length(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Font size</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~2: Font size</p>
<p>0x00: 8 lattice（Only english）</p>
<p>0x01: 12 lattice（Only english）</p>
<p>0x02: 16 lattice</p>
<p>0x03: 24 lattice</p>
<p>0x04: 32 lattice</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>Bit0~2: Font color</p>
<p>0x01: Red</p>
<p>0x02: Green</p>
<p>0x03: Yellow</p>
<p>0x04: Blue</p>
<p>Red、green、blue can make up another color by bit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Stay time</p>
</blockquote></td>
<td><blockquote>
<p>0x0000~0xffff</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte previous(big endian), in seconds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Calendar</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>0: The gregorian calendar</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Format</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>bit 0: Signal timing(0: 12 signal timing；1: 24 signal timing) bit 1:
Year by bit(0: 4 bit；1: 2 bit) bit 2: Line folding(0:
single-row；1:</p>
<p>multi-row)</p>
<p>bit 3~5: Reserved(set to 0)</p>
<p>bit 6: Show time scale ”Hour scale、 Minute scale” bit 7:
Reserved(set to 0)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Content</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>Ascertain the display content by bit:</p>
<p>bit 7: pointer bit 6: week bit 5: second bit 4: minute bit 3: hour
bit 2: day bit 1: month bit 0: year</p>
</blockquote></td>
</tr>
</tbody>
</table>

Temperature and Humidity type

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th>6</th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td>3</td>
<td>Font size</td>
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay time</p>
</blockquote></td>
<td>Format</td>
<td colspan="2">Reserved</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Length(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Font size</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~2: Font size</p>
<p>0x00: 8 lattice（Only english）</p>
<p>0x01: 12 lattice（Only english）</p>
<p>0x02: 16 lattice</p>
<p>0x03: 24 lattice</p>
<p>0x04: 32 lattice</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font color</p>
</blockquote></td>
<td></td>
<td></td>
<td><p>Bit0~2: Font color</p>
<blockquote>
<p>0x01: Red</p>
<p>0x02: Green</p>
<p>0x03: Yellow</p>
<p>0x04: Blue</p>
<p>Red、green、blue can make up another color by bit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Stay time</p>
</blockquote></td>
<td><blockquote>
<p>0x0000~0xffff</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte previous (big endian), in seconds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Format</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Celsius</p>
<p>1: Fahrenheit</p>
<p>2: Humidity</p>
</blockquote></td>
</tr>
</tbody>
</table>

Picture and reference to the picture

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th>6</th>
<th><blockquote>
<p>7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Mode</p>
</blockquote></td>
<td><blockquote>
<p>Speed</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Stay time</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Reserved</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th>Value</th>
<th><blockquote>
<p>Length(BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Mode</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><blockquote>
<p>See in “1.7”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Speed</p>
</blockquote></td>
<td>0～9</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The smaller of the value, the faster. Invalid when display
immediately.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Stay time</p>
</blockquote></td>
<td>0x0000~0xffff</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>High byte previous (big endian). In seconds.</td>
</tr>
</tbody>
</table>

1.14、The meaning of each byte of the scan parameters

A total of 16 bytes of scan parameters, set the scanning parameters and
read the scan parameters to be used, the meaning of each byte is as
follows:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 46%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Byte</th>
<th><blockquote>
<p>Byte</p>
<p>Meaning</p>
</blockquote></th>
<th><blockquote>
<p>CPower3200/2200/1200 Value Description</p>
</blockquote></th>
<th><blockquote>
<p>CPower5200/4200 Value</p>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x00</td>
<td><blockquote>
<p>Column order</p>
</blockquote></td>
<td><blockquote>
<p>0:Positive(+),1:Negvtive(-)</p>
</blockquote></td>
<td>0:Positive(+),1:Negvtive(-)</td>
</tr>
<tr class="even">
<td>0x01</td>
<td><blockquote>
<p>Data polarity</p>
</blockquote></td>
<td><blockquote>
<p>0:Positive(+),1:Negvtive(-)</p>
</blockquote></td>
<td>0:Positive(+),1:Negvtive(-)</td>
</tr>
<tr class="odd">
<td>0x02</td>
<td><blockquote>
<p>OE polarity</p>
</blockquote></td>
<td><blockquote>
<p>CPower3200/2200:This parameter does not exist , is set to 0.</p>
<p>CPower1200:0:Positive(+),1:Negvtive(-)</p>
</blockquote></td>
<td><blockquote>
<p>0:Positive(+),1:Negvtive(-)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0x03</td>
<td><blockquote>
<p>Line adjust</p>
</blockquote></td>
<td><blockquote>
<p>0:-1,1:0,2:1,3:2</p>
</blockquote></td>
<td>0:0,1:1,2:2,3:-1</td>
</tr>
<tr class="odd">
<td>0x04</td>
<td><blockquote>
<p>Hide scan</p>
</blockquote></td>
<td><blockquote>
<p>0:No，1：Yes</p>
</blockquote></td>
<td><p>0:No hide，1:Hide front，</p>
<blockquote>
<p>2:Hide back，3:Hide both</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0x05</td>
<td><blockquote>
<p>Color order</p>
</blockquote></td>
<td><blockquote>
<p>0：Red-Green，1：Green-Red</p>
</blockquote></td>
<td><p>0:Red-Green-Blue ，</p>
<blockquote>
<p>1:Red-Blue-Green，</p>
<p>2: Green-Red-Blue,</p>
<p>3：Green-Blue-Red，</p>
<p>4：Blue-Red-Green，</p>
<p>5：Blue-Green-Red</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>0x06</td>
<td><blockquote>
<p>Color mode</p>
</blockquote></td>
<td><blockquote>
<p>0：6Mhz，1：12Mhz</p>
</blockquote></td>
<td>0~15：Mode 1~Mode 16</td>
</tr>
<tr class="even">
<td>0x07</td>
<td><blockquote>
<p>Timing trimming</p>
</blockquote></td>
<td><blockquote>
<p>This parameter does not exist , is set to 0.</p>
</blockquote></td>
<td><blockquote>
<p>0：1,1：2,2：3,3：4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>0x08</td>
<td><blockquote>
<p>Pulse trimming</p>
</blockquote></td>
<td><blockquote>
<p>This parameter does not exist , is set to 0.</p>
</blockquote></td>
<td><blockquote>
<p>0：1,1：2,2：3,3：4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0x09</td>
<td><blockquote>
<p>Scan mode</p>
</blockquote></td>
<td><blockquote>
<p>0：1/16，1：1/8，2：1/4，3：1/2，4：Static</p>
</blockquote></td>
<td><blockquote>
<p>0：1/16，1：1/8，2：1/4，3：</p>
<p>1/2，4：Static</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>0x0A</td>
<td><blockquote>
<p>Module size</p>
</blockquote></td>
<td><blockquote>
<p>0：16-Line，1：8-Line，2：4-Line，3：2-Line，</p>
<p>4：1-Line</p>
</blockquote></td>
<td>0：16-Line，1：8-Line，2： 4-Line，3：2-Line，4：1-Line</td>
</tr>
<tr class="even">
<td>0x0B</td>
<td><blockquote>
<p>Line change space</p>
</blockquote></td>
<td><blockquote>
<p>0：Every 4，1：Every 8，2：Every 16，3：</p>
<p>Every 32</p>
</blockquote></td>
<td><blockquote>
<p>0：Every 8，1：Every 4，2：</p>
<p>Every 16，3：Every 32</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>0x0C</td>
<td><blockquote>
<p>Line change direction</p>
</blockquote></td>
<td><blockquote>
<p>0:Positive(+),1:Negvtive(-)</p>
</blockquote></td>
<td>0:Positive(+),1:Negvtive(-)</td>
</tr>
<tr class="even">
<td>0x0D</td>
<td><blockquote>
<p>Signal reverse</p>
</blockquote></td>
<td><blockquote>
<p>0:None，</p>
<p>1:Odd line reverse，</p>
<p>2:Even linereverse，</p>
<p>3:All</p>
</blockquote></td>
<td><blockquote>
<p>0：None，1：Reverse 8-pixel，</p>
<p>2：Reverse 4-pixel，</p>
<p>3：Reverse 16-pixel，</p>
<p>4：Reverse 32-pixel，</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>0x0E</td>
<td><blockquote>
<p>Output board</p>
</blockquote></td>
<td><blockquote>
<p>0:Normal，1:Extend</p>
</blockquote></td>
<td><p>0：Type 1,1：Type 2,</p>
<blockquote>
<p>2：Type 3,3：Type 4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>0x0F</td>
<td><blockquote>
<p>Line reverse</p>
</blockquote></td>
<td><blockquote>
<p>This parameter does not exist , is set to 0.</p>
</blockquote></td>
<td><blockquote>
<p>0 ： None,2 ： Even line reverse,3: Odd line reverse</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.15、The meaning of each byte of the parameters of formatted text item

Formatted text control data

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 11%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Formatted text control data length(little endian)</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font point size</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Font point size(little endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Flag</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0-7:</p>
<p>Bit 0：Bold</p>
<p>Bit 1：Italic</p>
<p>Bit 2：Underline</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Align mode</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: Horizontal( 0:Left, 1:horizontal center, 2:right )</p>
<p>Bit2~3: Vertical(0:Top, 1: vertical center, 2: down ）</p>
<p>Others: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Paging</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: Paging mode（0：No，1：Horizontal，2：Vertical）</p>
<p>Bit 2：Break word between pages( 1: Yes; 0: No )</p>
<p>Bit 3：Image Cover whole page or not( 1: Yes; 0: No )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font forground color</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Font background color</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Page background color</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Row height</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Row height of every row of string( by pixel )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Y-Offset</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Offset of vertical direction( by pixel )</p>
</blockquote></td>
</tr>
</tbody>
</table>

Screen data

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 11%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Screen data length( little endian )</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen width</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Pixel( little endian )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen height</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Pixel( little endian )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Color</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The color data and data format that contain in the Image data .</p>
<p>The lower 4 bit show what color data of exist. Can be a combination
of the following values</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>0x01: Red data is exist.</p>
<p>0x02: Green data is exist</p>
<p>0x04: Blue data is exist</p>
</blockquote>
<p>The hign 4 bit show dormat of data(Gray-level), support two
formats</p>
<p>0x0: Binary image. Line in accordance with the level of images, each
of the eight data points to form a byte, the less than 8 points at the
end to make up a byte 0; the amount of a color data (unit: bytes) is:
((picture width + 7)</p>
<p>/ 8) * picture height.</p>
<p>0x7: 256 gray-scale data. Each point expressed by 1 byte; the amount
of a color data (unit: bytes) is: image width * image height.</p>
<p>For example：0x71 show 256 gray picture, only exist red data</p></td>
</tr>
</tbody>
</table>

1.16、The meaning of each byte of the parameters of extent formatted
text item Extent formatted text content

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Screen data length( little endian )</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Text encoding</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>0x00：multibyte</p>
<p>0x01：widechar</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Text segment count</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Text’s segment count(one line string represents one segment)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Text segment</p>
</blockquote></td>
<td>Variable-l ength</td>
<td><blockquote>
<p>Reference to <u>Text segment format</u> definition</p>
</blockquote></td>
</tr>
</tbody>
</table>

Text segment format

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Screen data length( little endian )</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Align mode</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Bit0~1: Horizontal( 0:Left, 1:horizontal center,</p>
<p>2:right )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Substring count</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Text segment’s substring count</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Substring</p>
</blockquote></td>
<td>Variable-l ength</td>
<td><blockquote>
<p>Reference to <u>Substring format</u> definition</p>
</blockquote></td>
</tr>
</tbody>
</table>

Substring format

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 13%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Screen data length( little endian )</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Flag</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0-7:</p>
<p>Bit 0：Bold</p>
<p>Bit 1：Italic</p>
<p>Bit 2：Underline</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Font forground color</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font background color</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Font point size</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Font point size(little endian)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Font facename length</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Font facename length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Font facename</p>
</blockquote></td>
<td><blockquote>
<p>Variable-l ength</p>
</blockquote></td>
<td><blockquote>
<p>Font facename string, end with 0x00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>String length</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>String length(little endian)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>String</p>
</blockquote></td>
<td><blockquote>
<p>Variable-l ength</p>
</blockquote></td>
<td><blockquote>
<p>String, end with 0x00</p>
</blockquote></td>
</tr>
</tbody>
</table>

Extent formatted text control data

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Formatted text control data length(little endian)</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Align mode</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Bit0~1: Vertical(0:Top, 1: vertical center, 2: down ）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Others: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Paging</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: Paging mode（0：No，1：Horizontal，2：</p>
<p>Vertical）</p>
<p>Bit 2：Break word between pages( 1: Yes; 0: No )</p>
<p>Bit 3：Image Cover whole page or not( 1: Yes; 0:</p>
<p>No )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Page background color</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>BYTE 0：RED；1：GREEN；2：BLUE；3：0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Row height</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Row height of every row of string( by pixel )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Y-Offset</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Offset of vertical direction( by pixel )</p>
</blockquote></td>
</tr>
</tbody>
</table>

Extent screen data

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Item</th>
<th><blockquote>
<p>Length(</p>
<p>BYTE)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Data length</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Screen data length( little endian )</p>
<p>(except data item “Length”)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen width</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Pixel( little endian )</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen height</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Pixel( little endian )</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Color</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The color data and data format that contain in the Image data .</p>
<p>The lower 4 bit show what color data of exist. Can be a combination
of the following values</p>
<p>0x01: Red data is exist.</p>
<p>0x02: Green data is exist</p>
<p>0x04: Blue data is exist</p>
<p>The hign 4 bit show dormat of data(Gray-level), support two
formats</p>
<p>0x0: Binary image. Line in accordance with the level of images, each
of the eight data points to form a byte, the less than 8 points at the
end to make up a byte 0; the amount of a color data (unit: bytes) is:
((picture width + 7) / 8) * picture height.</p>
<p>0x7: 256 gray-scale data. Each point expressed by 1 byte; the amount
of a color data (unit: bytes) is: image width * image height.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>For example：0x71 show 256 gray picture, only exist red data</td>
</tr>
</tbody>
</table>

# API function for creating program file  {#api-function-for-creating-program-file}

2.1. Overview of program creating API functions

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 39%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th><blockquote>
<p>Function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_Program_Create</p>
</blockquote></td>
<td><blockquote>
<p>Create program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_Program_Destroy</p>
</blockquote></td>
<td><blockquote>
<p>Destroy program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_Program_SetProperty</p>
</blockquote></td>
<td><blockquote>
<p>Set the attribute value of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_Program_SetBackgndImage</p>
</blockquote></td>
<td><blockquote>
<p>Set the background image of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CP5200_Program_AddPlayWindow</p>
</blockquote></td>
<td><blockquote>
<p>Add play window to program</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>CP5200_Program_SetWindowProperty</p>
</blockquote></td>
<td><blockquote>
<p>Set window property</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>CP5200_Program_SetItemProperty</p>
</blockquote></td>
<td><blockquote>
<p>Set play item property</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>CP5200_Program_AddText</p>
<p>CP5200_Program_AddText1</p>
</blockquote></td>
<td><blockquote>
<p>Add text item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>CP5200_Program_AddTagText</p>
<p>CP5200_Program_AddTagText1</p>
</blockquote></td>
<td><blockquote>
<p>Add text item of contain extend tag to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>CP5200_Program_AddFormattedText</p>
</blockquote></td>
<td><blockquote>
<p>Add formatted text item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>CP5200_Program_AddFormattedTextW</p>
</blockquote></td>
<td><blockquote>
<p>Add formatted text item to play window(wide character)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>CP5200_Program_AddFormattedTextEx</p>
</blockquote></td>
<td><blockquote>
<p>Add extent formatted text item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>CP5200_Program_AddPicture</p>
</blockquote></td>
<td><blockquote>
<p>Add picture item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>CP5200_Program_AddImage</p>
</blockquote></td>
<td><blockquote>
<p>Add image item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>CP5200_Program_AddLafPict</p>
</blockquote></td>
<td><blockquote>
<p>Add Laf picture item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>CP5200_Program_AddLafVideo</p>
</blockquote></td>
<td><blockquote>
<p>Add Laf animator item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>CP5200_Program_AddAnimator</p>
</blockquote></td>
<td><blockquote>
<p>Add animator item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>CP5200_Program_AddClock</p>
</blockquote></td>
<td><blockquote>
<p>Add clock item to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td><blockquote>
<p>CP5200_Program_AddTemperature</p>
</blockquote></td>
<td><blockquote>
<p>Add temperature item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20</td>
<td><blockquote>
<p>CP5200_Program_AddVariable</p>
</blockquote></td>
<td><blockquote>
<p>Add custom variable data to play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>21</td>
<td><blockquote>
<p>CP5200_Program_AddTimeCounter</p>
</blockquote></td>
<td><blockquote>
<p>Add time counter data to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>22</td>
<td><blockquote>
<p>CP5200_Program_SaveToFile</p>
</blockquote></td>
<td><blockquote>
<p>Save program to file</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Create program object
>
> Step 2: Add play window
>
> Step 3: Add play item to play window
>
> Step 4: Save program to file
>
> Step 5: Destroy program object

2.2. Detail of creating program file API functions

> CP5200_Program_Create

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_Program_Create(WORD width, WORD height,
BYTE color)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Create program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>width: Width of the screen, unit is pixel</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>height: Height of the screen, unit is pixel</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>color: Color and gray-scale.</p>
<p>Bit0~2: 1 red color, 3 red &amp; green color, 7 red , green and blue
color</p>
<p>Bit4~6: gray scale. 0 (white or black), 7(256 grayscale)</p>
<p>For Example: 0x01(red color no gray), 0x77 full color, 256 gray
scale)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>Handle of program object, all these kind of API functions use this
handle</p>
<p>Return NULL if fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>When an application no longer requires a given object, it should be
destroyed to free the resource.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Program_Destroy

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_Destroy(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Destroy program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object to be destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid program object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_SetProperty

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_SetProperty(HOBJECT hObj, int
nPropertyValue, DWORD nPropertyID)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set the attribute value of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPropertyValue: Attribute value ，depend on
parameter“nPropertyID”have different meanings program repetition play
times’s range is1~65535 program play time’s unit is second and range is
1~65535</p>
<p>Code conversion: 0: no conversion;1: simplified Chinese = &gt;
traditional Chinese;2: traditional Chinese = &gt; simplified
Chinese;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPropertyID: Attribute identify，must be the one as below:</p>
<p>1: program repetition play times</p>
<p>2: program play time</p>
<p>3: Code conversion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>-1: Wrong handle of program object</p>
<p>0: Unacquainted Attribute identify</p>
<p>&gt;0: Setting success</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>“program repetition play times”and “program play time”,only one is
virtuous and the lastly setting is virtuous。</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Program_SetBackgndImage

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Program_SetBackgndImage(HOBJECT hObj,
const BYTE* pImgDat, WORD wImgWidth,</p>
<p>WORD wImgHeight, BYTE color, int nMode, int nCompress)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set the background image of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of program objec</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><p>pImgDat: Image data buffer。Determine the data of the color and
data</p>
<blockquote>
<p>format by the value of parameters “color”. Multi-color data exist,
the first red data, add the green data, and finally the blue data.</p>
<p>Data for each color, to put the data of line one frist, add then line
second , the data of each pixel based on parameters “color” high</p>
<p>4 bit to determine。</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>wImgWidth: Picture width points</th>
</tr>
<tr class="header">
<th>wImgHeight:Picture height points</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>color: The color data and data format that contain in the Image
data . The lower 4 bit show what color data of exist. Can be a
combination of the following values</p>
<blockquote>
<p>0x01: Red data is exist.</p>
<p>0x02: Green data is exist</p>
<p>0x04: Blue data is exist</p>
<p>The hign 4 bit show dormat of data(Gray-level), support two
formats</p>
<p>0x0: Binary image. Line in accordance with the level of images,</p>
<p>each of the eight data points to form a byte, the less than 8 points
at the end to make up a byte 0; the amount of a color data (unit: bytes)
is: ((picture width + 7) / 8) * picture height.</p>
<p>0x7: 256 gray-scale data. Each point expressed by 1 byte; the</p>
<p>amount of a color data (unit: bytes) is: image width * image
height.</p>
</blockquote>
<p>For example：0x71 show 256 gray picture, only exist red data</p></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>nMode: Display dispose mode</p>
<p>0: center</p>
<p>1: by scaling</p>
<p>2: Stretch</p>
<p>3: flat</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCompress: Compressed image data. Only support the non-compressed
now</p>
<p>0：non-compressed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>-1: Invalid program object handle</p>
<p>-4 : Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddPlayWindow

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddPlayWindow(HOBJECT hObj, WORD x,
WORD y, WORD cx, WORD cy)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add play window to program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>x: Start X of the play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>y: Start X of the play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>cx: Width of play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cy: Height of play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Number of play window</p>
<p>-1: Invalid program object handle</p>
<p>-3: Argument error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_SetWindowProperty
>
> int CP5200_Program_SetWindowProperty(HOBJECT hObj, int nWinNo, int
> nPropertyValue, int nPropertyID);

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Set window property</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWinNo: Number of play window,base on 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPropertyValue: property value</p>
<p>When the attribute ID is 1, meaning its value is as follows:</p>
<p>bit0 ~ 1: frame speed (the smaller the faster) bit2: border
background color (1 green, 0 for black) bit3: Border foreground color (1
red, 0 for white) bit4 ~ 6: Border action mode (0 No border,1 Single
point , 2 Dash, 3 Cross, 4 chase) bit7: Border rolling direction (0
clockwise, 1 counterclockwise)</p>
<p>When the attribute ID is 2, meaning its value is as follows:</p>
<p>0: still, 1: loop 2: Hide</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPropertyID: attribute ID, can be one of the following values:</p>
<p>1: Set the Properties window frame</p>
<p>2: Set the window waiting for the type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_SetItemProperty

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_SetItemProperty(HOBJECT hObj, int
nWinNo, int nItem , int nPropertyValue, int nPropertyID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set play item property</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window,base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nItem:Play item no</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nPropertyValue: Color，RGB value same as windows macro RGB(r,g,b),
Cancel transparent color when it is -1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPropertyID: Value of 1 means set the transparent color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: success</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddText (CP5200_Program_AddText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Program_AddText(HOBJECT hObj, int nWinNo,
const char* pText, int nFontSize,</p>
<p>COLORREF crColor, int nEffect, int nSpeed, int nStay)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add text item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be added</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>CP5200_Program_AddText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddTagText
>
> (CP5200_Program_AddTagText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddTagText(HOBJECT hObj, int nWinNo,
const char* pText, int nFontSize, COLORREF crColor, int nEffect, int
nSpeed, int nStay)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add text item of contain extend tag to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be added</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Default use the parameters value of the text size, color and other
attribute values, if the text contains the extensible tag, from
extensible tag, use the value of extensible tag specified.</p>
<p>CP5200_Program_AddTagText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddFormattedText
>
> int CP5200_Program_AddFormattedText( HOBJECT hObj, int nWinNo, const
> char \*pText, const char \*pFontFaceName, const byte \*pFormatData,
> const byte \*pScreenData, int nMode, int nEffect, int nSpeed, int
> nStay, int nCompress )

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Add formatted text item to play window</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pFontFaceName：Font face name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pformatData：<u>Formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pScreenData：<u>Screen data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
<p>4: Lefttop</p>
<p>8: Vertical multipage</p>
<p>11: Horizontal multi page (Align left)</p>
<p>12: Horizontal multi page (Align right)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
<p>-5: Invalid params related to format text data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddFormattedTextW

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddFormattedTextW( HOBJECT hObj, int
nWinNo, const wchar_t *pText, const char *pFontFaceName, const byte
*pFormatData, const byte *pScreenData, int nMode, int nEffect, int
nSpeed, int nStay, int nCompress )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add formatted text item to play window(wide character)</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="11">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFontFaceName：Font face name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pformatData：<u>Formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pScreenData：<u>Screen data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
<p>4: Lefttop</p>
<p>8: Vertical multipage</p>
<p>11: Horizontal multi page (Align left)</p>
<p>12: Horizontal multi page (Align right)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
<p>-5: Invalid params related to format text data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddFormattedTextEx

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Program_AddFormattedTextEx( HOBJECT hObj,
int nWinNo, const byte</p>
<p>*pTextContent, const byte *pFormatData, const byte *pScreenData, int
nMode, int nEffect, int nSpeed, int nStay, int nCompress );</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add extent formatted text item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTextContent: <u>Extent formatted text content</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFormatData：<u>Extent formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pScreenData：<u>Extent screen data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
<p>4: Lefttop</p>
<p>8: Vertical multipage</p>
<p>11: Horizontal multi page (Align left)</p>
<p>12: Horizontal multi page (Align right)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
<p>-5: Invalid params related to format text data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddPicture

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddPicture(HOBJECT hObj, int nWinNo,
const char* pPictFile, int nMode, int nEffect, int nSpeed, int nStay,
int nCompress)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add picture item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pPictFile: Path and file name of the picture file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
<p>4: Lefttop</p>
<p>8: Vertical multipage</p>
<p>11: Horizontal multi page (Align left)</p>
<p>12: Horizontal multi page (Align right)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddImage

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddImage(HOBJECT hObj, int nWinNo,
const BYTE* pImgDat, WORD wImgWidth, WORD wImgHeight, BYTE color, int
nMode, int nEffect, int nSpeed, int nStay, int nCompress, int
nPageCount)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add image item to the play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pImgDat: Image data buffer。Determine the data of the color and
data</p>
<p>format by the value of parameters “color”. Multi-color data exist,
the first red data, add the green data, and finally the blue data.</p>
<p>Data for each color, to put the data of line one frist, add then line
second ,</p>
<p>the data of each pixel based on parameters “color” high 4 bit to
determine。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wImgWidth: Picture width points.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wImgHeight: Picture height points.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>color: The color data and data format that contain in the Image data
. The lower 4 bit show what color data of exist. Can be a combination of
the following values</p>
<p>0x01: Red data is exist.</p>
<p>0x02: Green data is exist</p>
<p>0x04: Blue data is exist</p>
<p>The hign 4 bit show dormat of data(Gray-level), support two
formats</p>
<p>0x0: Binary image. Line in accordance with the level of images,</p>
<p>each of the eight data points to form a byte, the less than 8 points
at the end to make up a byte 0; the amount of a color data (unit: bytes)
is: ((picture width + 7) / 8) * picture height.</p>
<p>0x7: 256 gray-scale data. Each point expressed by 1 byte; the</p>
<p>amount of a color data (unit: bytes) is: image width * image
height.</p>
<p>For example：0x71 show 256 gray picture, only exist red data</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nMode: Render Moder</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nEffect: Show effect</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPageCount: The page count</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>The size of the image must fit the window size</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddLafPict

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddLafPict(HOBJECT hObj, int nWinNo,
const char* pLafFile, int nMode, int nEffect, int nSpeed, int nStay, int
nCompress)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add Laf picture item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pLafFile: Path and file name of the laf picture file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed. 0 fastest</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCompress: Compress picture data</p>
<p>0：Do not compress it</p>
<p>1：Convert to 256 color and compress the data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddLafVideo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddLafVideo(HOBJECT hObj, int nWinNo,
const char* pLafFile, int nMode, int nRepeat)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add Laf animator item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pLafFile: Path and file name of laf video file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nRepeat: Repeat time. 1 time, 2 times, …</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddAnimator

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddAnimator(HOBJECT hObj, int nWinNo,
const char* pAniFile, int nMode, int nRepeat)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add animator item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pAniFile: Path and file name of gif file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nMode: Render mode</p>
<p>0: Center</p>
<p>1: Zoom to fit the window</p>
<p>2: Stretch to fit the window</p>
<p>3: Tile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nRepeat: Repeat time. 1 time, 2 times, …</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddClock

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Program_AddClock(HOBJECT hObj, int nWinNo,
const char* pText, int nFontSize,</p>
<p>COLORREF crColor, int nStay, WORD wAttr)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add clock item to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>wAttrib: Clock attribute. By bit to determine the content to
display.</p>
<p>bit 0: Show year bit 1: Show month bit 2: Show day bit 3:Show hour
bit 4:Show minute bit 5:Show second bit 6:Show week bit 7:Show clock
hand bit 8: when the system (0: 12 hour; 1: 24 hours system) bit 9: Year
digit (0: 4; 1: 2) bit 10: Branch (0: single; 1: multi-line) bit 11~13:
Format control, such as the November 12, 2010 Friday , according to
diffenert values expressed as:</p>
<p>0: 2010/11/12 Friday 16:20:30</p>
<p>1: Fri，12/11/2010 16:20:30</p>
<p>2: 2010-11-12 Fri. 16:20:30</p>
<p>3: Friday，12 November 2010 16:20:30 4: Fri，Nov 12,2010 16:20:30</p>
<p>5: Friday，November 12 2010 16:20:30</p>
<p>6: Fri，11/12/2010 16:20:30</p>
<p>7: 2010/11/12，Fri.16:20:30 bit 14: show hands,marks bit 15
Transparent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddTemperature
>
> int CP5200_Program_AddTemperature(HOBJECT hObj, int nWinNo, const
> char\* pText, int nFontSize, COLORREF crColor, int nStay, WORD wAttr)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Add temperature item to play window</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wAttrib: Temperature attribute</p>
<p>0: Celsius degree</p>
<p>1: Fahrenheit degree</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddVariable

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddVariable(HOBJECT hObj, int nWinNo,
int nFontSize, COLORREF crColor, int nStay, WORD wAttr)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add custom variable data to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Font Color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: StayTime</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>wAttrib: Custom data attributes</p>
<p>High-byte format: the following: 0: text data.Direct display variable
text 1：picture data.Variable text shows the low byte of the specified
image as a variable number, valid values 1 to 100, specify which user
variables</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_AddTimeCounter

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_AddTimeCounter(HOBJECT hObj, int
nWinNo, int nFontSize, COLORREF crColor, int nStay, int nOption , const
int* pBaseTime ,const char* pContent)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add time counter data to play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWinNo: Number of play window, base on 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Font Color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStay: StayTime</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption: Display properties</p>
<p>Byte 1：Format，</p>
<p>Bit0: time counter type。0:up timer，1 countdown Bit1~7: reserved</p>
<p>Byte 2 ：Align,</p>
<p>Bit0~1:horizontal alignment;Bit2~3:vertical alignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBaseTime: Integer array Pointer , the array Length is 6,</p>
<p>store year,month,day,hour,minute,second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pContent:</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Play item no</p>
<p>-1: Invalid program object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-3: Invalid play window number</p>
<p>-4: Memory not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Program_SaveToFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Program_SaveToFile(HOBJECT hObj, const char*
pFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Save program to file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: Path and file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid program object handle</p>
<p>-3: File create error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# API function for creating playbill file  {#api-function-for-creating-playbill-file}

3.1. Overview of playbill creating API function

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th><blockquote>
<p>Function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_Playbill_Create</p>
</blockquote></td>
<td><blockquote>
<p>Create playbill object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_Playbill_Destroy</p>
</blockquote></td>
<td><blockquote>
<p>Destroy playbill object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_Playbill_SetProperty</p>
</blockquote></td>
<td><blockquote>
<p>Set the attribute value of playbill object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_Playbill_AddFile</p>
</blockquote></td>
<td><blockquote>
<p>Add program file to playbill</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CP5200_Playbill_DelFile</p>
</blockquote></td>
<td>Delete program file from playbill</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>CP5200_Playbill_SaveToFile</p>
</blockquote></td>
<td><blockquote>
<p>Save playbill to file</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Create playbill object
>
> Step 2: Add program file to playbill
>
> Step 3: Save playbill to file
>
> Step 4: Destroy playbill object

3.2. Detail of creating playbill file functions

> CP5200_Playbill_Create

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_Playbill_Create(WORD width, WORD height,
BYTE color)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Create playbill object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>width: Screen width, unit is pixel</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>height: Screen height, unit is pixel</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>color: Color and gray-scale.</p>
<p>Bit0~2: 1 red color, 3 red &amp; green color, 7 red , green and blue
color Bit4~6: gray scale. 0 (white or black), 7(256 grayscale)</p>
<p>For Example: 0x01(red color no gray), 0x77 full color, 256 gray
scale)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>Handle of playbill object, all these kind of API functions use this
handle</p>
<p>Return NULL if fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>When an application no longer requires a given object, it should be
destroyed to free the resource.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Playbill_Destroy

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Playbill_Destroy(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Destroy playbill object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of playbill object to be destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid playbill object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Playbill_SetProperty

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Playbill_SetProperty(HOBJECT hObj, int
nPropertyValue, DWORD nPropertyID)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set the attribute value of playbill object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of program object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPropertyValue: Attribute value ，depend on
parameter“nPropertyID”have different meanings rotation : 0: Don’t rotate
; 1: Rotate 90 degrees</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPropertyID: Attribute identify，must be the one as below:</p>
<p>1: rotation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>-1: Wrong handle of program object</p>
<p>0: Unacquainted Attribute identify</p>
<p>&gt;0: Setting success</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Playbill_AddFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Playbill_AddFile(HOBJECT hObj, const char*
pFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add program file to playbill</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of playbill object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: Path and file name of program file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Add file success</p>
<p>-1: Invalid playbill object handle</p>
<p>-3: Not short file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Playbill_DelFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Playbill_DelFile(HOBJECT hObj, const char*
pFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete program file from play bill</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of playbill object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: Path and file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Delete success</p>
<p>-1: Invalid playbill object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-3: File create error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Playbill_SaveToFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Playbill_SaveToFile(HOBJECT hObj, const char*
pFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Save playbill to file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of playbill object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: Path and file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid playbill object handle</p>
<p>-3: File create error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# API function for data communication  {#api-function-for-data-communication}

4.1. Overview of data communication API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 45%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th><blockquote>
<p>Function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_CommData_Create</p>
</blockquote></td>
<td><blockquote>
<p>Create communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_CommData_Destroy</p>
</blockquote></td>
<td><blockquote>
<p>Destroy communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_CommData_SetParam</p>
</blockquote></td>
<td><blockquote>
<p>Set data packet parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_MakeCreateFileData</p>
</blockquote></td>
<td><blockquote>
<p>Make create file command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CP5200_ParseCreateFileRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of create file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>CP5200_MakeWriteFileData</p>
</blockquote></td>
<td><blockquote>
<p>Make write file command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>CP5200_ParseWriteFileRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of write file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>CP5200_MakeCloseFileData</p>
</blockquote></td>
<td><blockquote>
<p>Make close file command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>CP5200_ParseCloseFileRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of close file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>CP5200_MakeDeleteFileNoData</p>
</blockquote></td>
<td><blockquote>
<p>Make delete file command data (By file number)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>CP5200_ParseDeleteFileNoRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of delete file by file number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>CP5200_MakeDeleteFileNameData</p>
</blockquote></td>
<td><blockquote>
<p>Make delete file command data (By file name)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 45%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>13</th>
<th>CP5200_ParseDeleteFileNameRet</th>
<th>Parse return data of delete file by file name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>14</td>
<td>CP5200_MakeReadTimeData</td>
<td>Make query controller time command data</td>
</tr>
<tr class="even">
<td>15</td>
<td>CP5200_ParseReadTimeRet</td>
<td>Parse return data of query controller time</td>
</tr>
<tr class="odd">
<td>16</td>
<td>CP5200_MakeWriteTimeData</td>
<td>Make set controller time command data</td>
</tr>
<tr class="even">
<td>17</td>
<td>CP5200_ParseWriteTimeRet</td>
<td>Parse return data of set controller time</td>
</tr>
<tr class="odd">
<td>18</td>
<td>CP5200_MakeReadBrightnessData</td>
<td>Make query brightness setting command data</td>
</tr>
<tr class="even">
<td>19</td>
<td>CP5200_ParseReadBrightnessRet</td>
<td>Parse return data of set brightness</td>
</tr>
<tr class="odd">
<td>20</td>
<td>CP5200_MakeWriteBrightnessData</td>
<td>Make set brightness command data</td>
</tr>
<tr class="even">
<td>21</td>
<td>CP5200_ParseWriteBrightnessRet</td>
<td>Parse return data of set brightness</td>
</tr>
<tr class="odd">
<td>22</td>
<td>CP5200_MakeWriteIOOnOffTimeData</td>
<td>Make set IO timing control command data</td>
</tr>
<tr class="even">
<td>23</td>
<td>CP5200_ParseWriteIOOnOffTimeRet</td>
<td>Parse return data of set IO timing control</td>
</tr>
<tr class="odd">
<td>24</td>
<td>CP5200_MakeReadIOOnOffTimeData</td>
<td>Make query IO timing control information</td>
</tr>
<tr class="even">
<td>25</td>
<td>CP5200_ParseReadIOOnOffTimeRet</td>
<td>Parse query IO timing control information</td>
</tr>
<tr class="odd">
<td>26</td>
<td>CP5200_MakeWriteOnOffTimeData</td>
<td>Make set auto ONOFF control command data</td>
</tr>
<tr class="even">
<td>27</td>
<td>CP5200_ParseWriteOnOffTimeRet</td>
<td>Parse return data of set auto ONOFF control</td>
</tr>
<tr class="odd">
<td>28</td>
<td>CP5200_MakeReadOnOffTimeData</td>
<td><p>Make query auto ONOFF control</p>
<p>information command data</p></td>
</tr>
<tr class="even">
<td>29</td>
<td>CP5200_ParseReadOnOffTimeRet</td>
<td>Parse return data of query auto ONOFF control information</td>
</tr>
<tr class="odd">
<td>30</td>
<td>CP5200_MakeReadVersionData</td>
<td>Make query version information command data</td>
</tr>
<tr class="even">
<td>31</td>
<td>CP5200_ParseReadVersionRet</td>
<td>Parse return data of query version information</td>
</tr>
<tr class="odd">
<td>32</td>
<td>CP5200_MakeFormatData</td>
<td>Make format controller file system command data</td>
</tr>
<tr class="even">
<td>33</td>
<td>CP5200_ParseFormatRet</td>
<td>Parse return data of format controller file system</td>
</tr>
<tr class="odd">
<td>34</td>
<td>CP5200_MakeRestartAppData</td>
<td>Make restart Appcommand data</td>
</tr>
<tr class="even">
<td>35</td>
<td>CP5200_ParseRestartAppRet</td>
<td>Parse return data of restart App</td>
</tr>
<tr class="odd">
<td>36</td>
<td>CP5200_MakeRestartSysData</td>
<td>Make restart controller command data</td>
</tr>
<tr class="even">
<td>37</td>
<td>CP5200_ParseRestartSysRet</td>
<td>Parse return data of restart controller</td>
</tr>
<tr class="odd">
<td>38</td>
<td>CP5200_MakeGetFreeSpaceData</td>
<td>Make query free space in controller command data</td>
</tr>
<tr class="even">
<td>39</td>
<td>CP5200_ParseGetFreeSpaceRet</td>
<td>Parse return data of query free space in controller</td>
</tr>
<tr class="odd">
<td>40</td>
<td>CP5200_MakeGetFileInfoData</td>
<td>Make query file information command data</td>
</tr>
<tr class="even">
<td>41</td>
<td>CP5200_ParseGetFileInfoRet</td>
<td>Parse return data of query file information</td>
</tr>
<tr class="odd">
<td>42</td>
<td>CP5200_ParseGetFirstFileInfoRet</td>
<td>Parse return data of query file information and get first file
information</td>
</tr>
<tr class="even">
<td>43</td>
<td>CP5200_ParseGetNextFileInfoRet</td>
<td>Parse return data of query file information</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 45%" />
<col style="width: 45%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th colspan="2">and get next file information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>44</td>
<td>CP5200_MakeBeginFileUploadData</td>
<td colspan="2">Make start upload file command data</td>
</tr>
<tr class="even">
<td>45</td>
<td>CP5200_ParseBeginFileUploadRet</td>
<td colspan="2">Parse return data of start upload file command</td>
</tr>
<tr class="odd">
<td>46</td>
<td>CP5200_MakeFileUploadData</td>
<td colspan="2">Make upload file command data</td>
</tr>
<tr class="even">
<td>47</td>
<td>CP5200_ParseFileUploadRet</td>
<td colspan="2">Parse return data of upload file command</td>
</tr>
<tr class="odd">
<td>48</td>
<td>CP5200_MakeEndFileUploadData</td>
<td colspan="2">Make finish upload file command data</td>
</tr>
<tr class="even">
<td>49</td>
<td>CP5200_ParseEndFileUploadRet</td>
<td colspan="2">Parse return data of finish upload file command</td>
</tr>
<tr class="odd">
<td>50</td>
<td>CP5200_MakeGetTypeInfoData</td>
<td colspan="2">Make query type information command data</td>
</tr>
<tr class="even">
<td>51</td>
<td>CP5200_ParseGetTypeInfoRet</td>
<td colspan="2">Parse return data of query type information</td>
</tr>
<tr class="odd">
<td>52</td>
<td>CP5200_MakeGetTempHumiData</td>
<td colspan="2">Make query temperature and humidity information command
data</td>
</tr>
<tr class="even">
<td>53</td>
<td>CP5200_ParseGetTempHumiRet</td>
<td colspan="2">Parse return data of query temperature information</td>
</tr>
<tr class="odd">
<td>54</td>
<td>CP5200_MakeReadConfigData</td>
<td colspan="2">Make read configuration information command data</td>
</tr>
<tr class="even">
<td>55</td>
<td>CP5200_ParseReadConfigRet</td>
<td colspan="2">Parse return data of read configuration information</td>
</tr>
<tr class="odd">
<td>56</td>
<td>CP5200_MakeWriteConfigData</td>
<td colspan="2">Make write configuration information command data</td>
</tr>
<tr class="even">
<td>57</td>
<td>CP5200_ParseWriteConfigRet</td>
<td colspan="2">Parse return data of write configuration
information</td>
</tr>
<tr class="odd">
<td>58</td>
<td>CP5200_MakeReadRunningInfoData</td>
<td colspan="2">Make query running info data</td>
</tr>
<tr class="even">
<td>59</td>
<td>CP5200_ParseReadRunningInfoRet</td>
<td colspan="2">Parse return value of query running info command</td>
</tr>
<tr class="odd">
<td>60</td>
<td>CP5200_MakeScreenTestData</td>
<td colspan="2">Make show test pattern data</td>
</tr>
<tr class="even">
<td>61</td>
<td>CP5200_ParseScreenTestRet</td>
<td colspan="2">Parse return value of q show test pattern command</td>
</tr>
<tr class="odd">
<td>62</td>
<td><p>CP5200_MakeInstantMessageData</p>
<p>CP5200_MakeInstantMessageData1</p></td>
<td colspan="2">Make instant message data</td>
</tr>
<tr class="even">
<td>63</td>
<td>CP5200_MakeSendInstantMessageData</td>
<td colspan="2">Make send instant message data</td>
</tr>
<tr class="odd">
<td>64</td>
<td>CP5200_ParseSendInstantMessageRet</td>
<td colspan="2">Parse return value of send instant message command</td>
</tr>
<tr class="even">
<td>65</td>
<td>CP5200_MakeReadHWSettingData</td>
<td colspan="2">Make read scan param command data</td>
</tr>
<tr class="odd">
<td>66</td>
<td>CP5200_ParseReadHWSettingRet</td>
<td colspan="2">Parse return data of read scan param</td>
</tr>
<tr class="even">
<td>67</td>
<td>CP5200_MakeWriteHWSettingData</td>
<td colspan="2">Make write scan param command data</td>
</tr>
<tr class="odd">
<td>68</td>
<td>CP5200_ParseWriteHWSettingRet</td>
<td colspan="2">Parse return data of write scan param</td>
</tr>
<tr class="even">
<td>69</td>
<td>CP5200_MakeReadSoftwareSwitchInfoData</td>
<td colspan="2">Make read software switch info data</td>
</tr>
<tr class="odd">
<td>70</td>
<td>CP5200_ParseReadSoftwareSwitchInfoRet</td>
<td colspan="2">Parse return data of read software switch info data</td>
</tr>
<tr class="even">
<td>71</td>
<td>CP5200_MakeWriteSoftwareSwitchInfoData</td>
<td colspan="2">Make write software switch info data</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>72</p>
</blockquote></td>
<td>CP5200_ParseWriteSoftwareSwitchInfoRet</td>
<td colspan="2"><blockquote>
<p>Parse return data of write software switch info data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>73</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_MakeQueryControllerInfo</p>
</blockquote></td>
<td><blockquote>
<p>Make query controller information data</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>74</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_ParseQueryControllerInfoRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of query controller information data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>75</p>
</blockquote></td>
<td>CP5200_MakeOpenFileData</td>
<td colspan="2"><blockquote>
<p>Make open file data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>76</p>
</blockquote></td>
<td>CP5200_ParseOpenFileRet</td>
<td colspan="2"><blockquote>
<p>Parse return value of open file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>77</p>
</blockquote></td>
<td>CP5200_MakeGetDirentryData</td>
<td colspan="2"><blockquote>
<p>Make get file info</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>78</p>
</blockquote></td>
<td>CP5200_ParseGetDirentryRet</td>
<td colspan="2"><blockquote>
<p>Parse return value of get file info command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>79</p>
</blockquote></td>
<td>CP5200_MakeReadFileNoData</td>
<td colspan="2"><blockquote>
<p>Make read file data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td>CP5200_ParseReadFileNoRet</td>
<td colspan="2"><blockquote>
<p>Parse return value of read file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>81</p>
</blockquote></td>
<td>CP5200_MakeCloseFileNoData</td>
<td colspan="2"><blockquote>
<p>Make close file data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>82</p>
</blockquote></td>
<td>CP5200_ParseCloseFileNoRet</td>
<td colspan="2"><blockquote>
<p>Parse return value of close file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Create data object
>
> Step 2: Make communication data, include RS232/485's code convert
>
> (0xa5 =\> 0xaa 0x05, ...), or network ID code
>
> Step 3: Send communication data to the controller
>
> Step 4: Receive data from controller, and process code convert (0xaa
>
> 0x05 =\> 0xa5, ...)
>
> Step 5: Parse the return data and get the result
>
> Step 6: Destroy data object

4.2. Detail of data communication API functions

> CP5200_CommData_Create

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_CommData_Create(int nCommType, BYTE
byCardID, DWORD dwIDCode)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Create communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCommType: RS232/485 or network communication type</p>
<p>0: RS232/485</p>
<p>1: Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwIDCode: Network ID code of the controller. RS232 ignore it.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>Handle of communication data object, all these kind of API functions
use</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>this handle</p>
<p>Return NULL if fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>When an application no longer requires a given object, it should be
destroyed to free the resource.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_CommData_Destroy

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_CommData_Destroy(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Destroy communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object to de destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_CommData_SetParam

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_CommData_SetParam (HOBJECT hObj, int
nParamType, const char *pParamString)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set data packet parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nParamType：Parameter type，valid value 1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pParamString：Parameter string</p>
<p>When parameter type is 1，pParamString is controller’s device ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: No error</p>
<p>0: Parameter type is wrong</p>
<p>-1: Invalid data object handle</p>
<p>-2: pParamString is wrong</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeCreateFileData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeCreateFileData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const char* pFilename, long lFilesize, const
BYTE* pTimeBuffer)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make create file command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: File name to be created. Must be short name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>lFilesize: Size of the new file (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pTimeBuffer: File time information, the length is 6</p>
<p>Byte 0: Year-2000 (00~99), the year value plus 2000 is the real year
value</p>
<p>Byte 1: Month (1~12)</p>
<p>Byte 2: Day (1~31)</p>
<p>Byte 3: Hour(0~23)</p>
<p>Byte 4: Minute (0~59)</p>
<p>Byte 5: Second (0~59)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>If these is an old file in the controller, it will be overwritten</p>
<p>The maximum file size is 1.5M byte</p>
<p>Only ONE file can be read or write at the same time</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseCreateFileRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseCreateFileRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of create file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: File is created successfully</p>
<p>0: Can not create file</p>
<p>-2: Incorrect return data</p>
<p>-3: Return data length is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteFileData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeWriteFileData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const BYTE *pData,</p>
<p>WORD wDatLen, WORD *pwChksum)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make write file command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pData: File data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wDataLen: Data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pwChksum: WORD type pointer to a checksum variable, input old
checksum value and return new checksum value</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-2: Incorrect return data</p>
<p>-3: Return data length is not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>If a file is large, it should be split to blocks and write one block
each time, each block no more than 1000 bytes</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteFileRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteFileRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of write file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Incorrect return data</p>
<p>-3: Return data length is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Controller saved the received file data in a temporary buffer, and
the data is written to file when file closing</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_MakeCloseFileData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>int CP5200_MakeCloseFileData(HOBJECT hObj, BYTE *pBuffer, int
nBufSize, WORD wChksum)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Description</p>
</blockquote></td>
<td><blockquote>
<p>Make close file command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p>Parameter</p>
</blockquote></td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wChksum: Checksum of file data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Return</p>
</blockquote></td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Note</p>
</blockquote></td>
<td><blockquote>
<p>Closing file need to write all file data to the disk, it need
sometime to do this, the time is about：</p>
</blockquote>
<p>((file size / 4096) + 1) * 200 + 100 ms</p></td>
</tr>
</tbody>
</table>

> CP5200_ParseCloseFileRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseCloseFileRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of close file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>255: Checksum error</p>
<p>-2: Incorrect return data</p>
<p>-3: Return data length is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeDeleteFileNoData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeDeleteFileNoData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, int fno)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make delete file command data (By file number)</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>fno: File number</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseDeleteFileNoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseDeleteFileNoRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of delete file by file number</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Incorrect return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-3: Return data length is not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_MakeDeleteFileNameData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeDeleteFileNameData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const char</p>
<p>*pFilename)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make delete file command data (By file name)</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: File name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_ParseDeleteFileNameRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseDeleteFileNameRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of delete file by file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_MakeReadTimeData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadTimeData(HOBJECT hObj, BYTE *pBuffer,
int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query controller time command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_ParseReadTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadTimeRet (HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pTimeBuffer, int nTimeBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pTimeBuffer: Time information buffer，the meaning is:</p>
<p>Byte 0: Second</p>
<p>Byte 1: Minute</p>
<p>Byte 2: Hour</p>
<p>Byte 3: Week day</p>
<p>Byte 4: Day</p>
<p>Byte 5: Month</p>
<p>Byte 6: Year(2-year, plus 2000 is real year value)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nTimeBufSize: Length of time information buffer, at least 7 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteTimeData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeWriteTimeData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const BYTE* pTimeBuffer)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set controller time command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>pTimeBuffer: Time information data buffer, ，the meaning is:</p>
<p>Byte 0: Second</p>
<p>Byte 1: Minute</p>
<p>Byte 2: Hour</p>
<p>Byte 3: Week day</p>
<p>Byte 4: Day</p>
<p>Byte 5: Month</p>
<p>Byte 6: Year(2-year, plus 2000 is real year value)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteTimeRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadBrightnessData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadBrightnessData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query brightness setting command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadBrightnessRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadBrightnessRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pBrightnessBuffer, int
nBrightBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query brightness setting</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBrightnessBuffer: Brightness information buffer, one byte one hour’s
brightness, total 24 bytes. Each byte has the meaning:</p>
<p>Value 0~31: Brightness level</p>
<p>Value &gt;31: Auto brightness by light sensor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBrightBufSize: Brightness information buffer size, at least 24
bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteBrightnessData
>
> int CP5200_MakeWriteBrightnessData(HOBJECT hObj, BYTE \*pBuffer, int
> nBufSize, const

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">BYTE *pBrightnessBuffer)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set brightness command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBrightnessBuffer: Brightness setting information buffer, one byte
one hour’s brightness, total 24 bytes. Each byte has the meaning:</p>
<p>Value 0~31: Brightness level</p>
<p>Value &gt;31: Auto brightness by light sensor</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteBrightnessRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteBrightnessRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set brightness</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteIOOnOffTimeData
>
> int CP5200_MakeWriteIOOnOffTimeData(HOBJECT hObj, BYTE \*pBuffer, int
> nBufSize, const

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">BYTE *pOnOffBuffer)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set IO timing control command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pOnOffBuffer: IO timing control information buffer, at least 4
bytes</p>
<p>Byte 0~1: Hour and minute of “ON”</p>
<p>Byte 2~3: Hour and minute of “OFF”</p>
<p>If “ON” time and ”OFF” time is same, it will always “ON”; if hour
large than 23 or minute large than 59, the time invalid</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>IO signal is out put from J3 pin5 and pin6</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteIOOnOffTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteIOOnOffTimeRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set IO timing control</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadIOOnOffTimeData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadIOOnOffData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query IO timing control information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadIOOnOffTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_ParseReadIOOnOffTimeRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength,</p>
<p>BYTE* pOnOffBuffer, int nOnOffBufSize)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse query IO timing control information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pOnOffBuffer: IO timing control information buffer, total 4 bytes</p>
<p>Byte 0~1: Hour and minute of “ON”</p>
<p>Byte 2~3: Hour and minute of “OFF”</p>
<p>If “ON” time and ”OFF” time is same, it will always “ON”; if hour
large than 23 or minute large than 59, the time invalid</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nOnOffBufSize: IO timing control information buffer size, at least 4
bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-4: The size of information buffer is too small</p>
<p>-5: Checksum error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteOnOffTimeData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeWriteOnOffTimeData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const BYTE</p>
<p>*pOnOffBuffer)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set auto ONOFF control command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pOnOffBuffer: Auto ONOFF control information buffer， total 6
bytes</p>
<p>Byte 0~1: Hour and minute of “ON”</p>
<p>Byte 2~3: Hour and minute of “OFF”</p>
<p>Byte 4~5: Reserve, set to 0</p>
<p>If “ON” time and ”OFF” time is same, it will always “ON”; if hour
large than 23 or minute large than 59, the time invalid</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteOnOffTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteOnOffTimeRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set auto ONOFF control</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadOnOffTimeData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadOnOffTimeData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query auto ONOFF control information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadOnOffTimeRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadOnOffTimeRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pOnOffBuffer, int nOnOffBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query auto ONOFF control information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pOnOffBuffer: Auto ONOFF control information buffer, total 6
bytes</p>
<p>Byte 0~1: Hour and minute of “ON”</p>
<p>Byte 2~3: Hour and minute of “OFF”</p>
<p>Byte 4~5: Reserve, default is 0</p>
<p>If “ON” time and ”OFF” time is same, it will always “ON”; if hour
large than 23 or minute large than 59, the time invalid</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nOnOffBufSize: Auto ONOFF control information buffer size, at
least</p>
<p>6bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of information buffer is too small</p>
<p>-5: Checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadVersionData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadVersionData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query version information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadVersionRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadVersionRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query version information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: Version information buffer, version information include
3 bytes, in each byte the high 4 bits is major version and the low 4 bit
is miner version (0x10 = V1.0)</p>
<p>Byte 0: Bios version</p>
<p>Byte 1: Logic version</p>
<p>Byte 2: Software version</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: version information buffer size, at least 3 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of version information buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadVersionRet2

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadVersionRet2(HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query version information, include card type
number, each version info represented by 2 bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: Version information buffer, return value were
defined:</p>
<p>Byte 0: effective data len, include this byte</p>
<p>Byte 1: control card type</p>
<p>Byte 2~3: Bios version</p>
<p>Byte 4~5: Logic version</p>
<p>Byte 6~7: APP(program)version</p>
<p>BIOS、Logic、APP version info represented by 2 bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: version information buffer size</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of version information buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeFormatData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeFormatData(HOBJECT hObj, BYTE *pBuffer,
int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make format controller file system command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Format will delete all files in the controller!</p>
<p>For formatting disk need some time, so after sending the format
command to controller, need to wait about 1 second before respond data
can be received.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseFormatRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseFormatRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of format controller file system</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeRestartAppData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeRestartAppData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make restart App command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseRestartAppRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseRestartAppRet (HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of restart App</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeRestartSysData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeRestartSysData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make restart controller command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseRestartSysRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseRestartSysRet (HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of restart controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeGetFreeSpaceData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeGetFreeSpaceData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query free space in controller command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetFreeSpaceRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseGetFreeSpaceRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query free space in controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Size of free space（Byte）</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeGetFileInfoData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeGetFileInfoData(HOBJECT hObj, BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query file information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>It gets all files’ information in the controller, so the buffer for
return data should be large enough for all files. It needs:</p>
<p>(file quantity) * 32 + 10</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetFileInfoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_ParseGetFileInfoRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, int pos,</p>
<p>BYTE* pInfoBuffer, int nInfoBufSize)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query file information and get next file
information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pos: Current file sequence number</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>pInfoBuffer: File information buffer</p>
<p>Byte 0~44: File name and extension, including partition point ‘.’
between them ,for example:a1.txt</p>
<p>45~45:The two high of year. For example: in 2009, the byte value
is</p>
<p>20; in 1999, the byte value is 19</p>
<p>46~46: The two low of year . For example: in 2009, the byte value is
9; in 1999, the byte value is 99</p>
<p>47~47:Month</p>
<p>48~48: Day</p>
<p>49~49: Hour</p>
<p>50~50: Minute</p>
<p>51~51: Second</p>
<p>52~55: File size, lower byte in the front</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nInfoBufSize: File information buffer size, at least 64 bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0:File information number in the “pBuffer”</p>
<p>0: No required information, no next file</p>
<p>-1: Invalid data object handle</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of information buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>File sequence number base on 0, if pos=0 this function get file
information of the second file.</p>
<p>Use CP5200_ParseGetFirstFileInfoRet and this function to get file
information one by one.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetFirstFileInfoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_ParseGetFirstFileInfoRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength,</p>
<p>BYTE* pInfoBuffer, int nInfoBufSize)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query file information and get first file
information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: File information buffer</p>
<p>Byte 0~11: File name</p>
<p>12~15 : File extend name</p>
<p>16~18:File Data( Year,Month,Day) , A value for each byte,the
value</p>
<p>range of year is 0~99, the year value plus 2000 is the real year
value</p>
<p>19~21: File time( Hour,Minute,Second) , A value for each byte,</p>
<p>22~25: File size, lower byte in the front</p>
<p>26~31: Reserve</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: File information buffer size, at least 32 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: No required information, no any file in the controller</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of information buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Use this function and CP5200_ParseGetNextFileInfoRet to get file
information one by one</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetNextFileInfoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseGetNextFileInfoRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, int pos, BYTE* pInfoBuffer, int
nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query file information and get next file
information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pos: Current file sequence number</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>pInfoBuffer: File information buffer</p>
<p>Byte 0~11: File name</p>
<p>12~15 : File extend name</p>
<p>16~18:File Data( Year,Month,Day) , A value for each byte,the
value</p>
<p>range of year is 0~99, the year value plus 2000 is the real year
value</p>
<p>19~21: File time( Hour,Minute,Second) , A value for each byte,</p>
<p>22~25: File size, lower byte in the front</p>
<p>26~31: Reserve</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nInfoBufSize: File information buffer size, at least 32 bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: No required information, no next file</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
<p>-4: The size of information buffer is too small</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>File sequence number base on 0, if pos=0 this function get file
information of the second file.</p>
<p>Use CP5200_ParseGetFirstFileInfoRet and this function to get file
information one by one.</p>
<p>If the return value is less than 4,it show get all information of the
controller already.</p>
<p>If the return value is equal to 4,you can get more information by
called the function of “CP5200_MakeGetFileInfoData()” again</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_MakeBeginFileUploadData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeBeginFileUploadData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const char* pFilename, long lFilesize, const
BYTE* pTimeBuffer)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make start upload file command data,to inform the controller prepare
to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>receive data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pFilename:The file name to be create,must bu short file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>lFilesize: The file size(byte) to be create</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTimeBuffer: file time message，6 bytes length byte0: year(00~99),
real year-2000 byte 1: month(1~12) byte 2: day(1~31) byte 3: hour (0~23)
byte 4: minute(0~56) byte 5: second(0~59)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of create data</p>
<p>-1: Invalid data object handle</p>
<p>-4: The size of buffer is too small</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>If the controller have a same name file,the old file will be cover
with.</p>
<p>The file’s max size is 1.5M byte</p>
<p>Controller can operate only one file each time</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseBeginFileUploadRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseBeginFileUploadRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of start upload file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeFileUploadData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeFileUploadData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, const BYTE</p>
<p>*pData, WORD wDatLen, WORD wSegNo, WORD wSegLen, int
nWantRet)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make upload file command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pData: The uploaded file data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wDataLen: length of the actual upload data. Can not be greater than
wSegLen.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wSegNo: Data segment number, from 0 to start</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wSegLen: Data segment length of not more than 1024, it can be set to
512</p>
<p>generally. For each upload, the parameters need to be consistent.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWantRet: Whether or not to return immediately to confirm the
information。</p>
</blockquote>
<ol type="1">
<li><p>.No return</p></li>
<li><p>.Ruturn</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>If the file is too big ,must upload data in multiple</p>
<p>The time between two intervals upload to be not less than 50
milliseconds. Must be based on the value of “nWantRet” to determine
whether or not to deal with the return of information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseFileUploadRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseFileUploadRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of upload file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Only need to use this function while passed to the parameter
“nWantRet” of the function “CP5200_MakeWriteFileData” is non-0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_MakeEndFileUploadData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeEndFileUploadData(HOBJECT hObj, BYTE
*pBuffer, int nBufSize, WORD wTotalSeg)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make finish upload file command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wTotalSeg: The total number of data segment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseEndFileUploadRet
>
> int CP5200_ParseEndFileUploadRet(HOBJECT hObj, const BYTE\* pBuffer,
> int nLength, BYTE\*

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of finish upload file command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: Upload result information buffer, to record data segment
unsuccessful. Every 2 bytes of data on behalf of one data segment
number.</p>
<p>Low byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: Upload result information buffer size, at least 72
bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>&gt;0 And &lt;=36: Wrong data segment amount</p>
<p>255: No file to be closed</p>
<p>-2: Return wrong data</p>
<p>-3: The length of return data is not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Return the number of errors in the data above does not mean that all
of the wrong data segment , re-issued the above known data errors, and
then the result of new information, know that there is no error so
far.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_MakeGetTypeInfoData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeGetTypeInfoData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query type information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetTypeInfoRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseGetTypeInfoRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query type information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: type of information buffer (10 bytes) byte 0: Control
Card Type byte 1: FPGA version bytes 2-5: BIOS version bytes 6-9: APP
version</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: type result information buffer size, at least 10
bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeGetTempHumiData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeGetTempHumiData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize ,byte byFlag)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query temperature and humidifier information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>byFlag:Query flag</p>
<p>Bit0: Is query temperature (0 No,1Yes)</p>
<p>Bit1: Is query humidifier (0 No,1Yes)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetTempHumiRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseGetTempHumiRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query temperature and humidity information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p>pInfoBuffer: temperature and humidity information buffer, length is 8
bytes , the meanings :</p>
<p>byte 0：Query flag. The same as send package byte 1~2：temperature
(degress Celsius)：</p>
<p>Byte 1：Bit7: numeric symbols。1 negative，0 positive。 Bit6~0: the
high 7 bit of the integer part of temperature absolute</p>
</blockquote>
<p>Byte 2：Bit7~4: the lower 4 bit of the integer part of</p>
<blockquote>
<p>temperature absolute</p>
<p>Bit3~0: fractional part ，unit is 1/16(0.0625)</p>
<p>byte 3~4：temperature (degress Fahrenheit)： byte 5：temperature
adjustment value，</p>
<p>Bit7: 1 degress Fahrenheit，0 degress Celsius</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the temperature adjustment</p>
<p>byte 6：humidity。Valid values 0～100 byte 7：humidity adjustment
value</p>
<p>Bit7: reserved</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the humidity adjustment</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nInfoBufSize: temperature result information buffer size</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>-1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadConfigData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadConfigData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, int nFlag)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make read configuration information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFlag: Read the configuration information of the tag</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadConfigRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadConfigRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of read configuration information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: configuration of information buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: configuration result information buffer size ,at least
10 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>6: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteConfigData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeWriteConfigData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, const BYTE* pConfig, int nCfgLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make write configuration information command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pConfig: Configuration information content pointers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nCfgLength: Configuration information length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteConfigRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteConfigRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of write configuration information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadRunningInfoData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadRunningInfoData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, int nFlag)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make read running info data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFlag: to read the run mark</p>
<p>1: The current playing program number</p>
<p>2: Read the current font information</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadRunningInfoRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadRunningInfoRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of read running info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The running info buffer byte 0：Confirmation message，0
failed；&gt;0 success</p>
<p>If the flag is 1：The current playing program number，Byte1~Byte5 as
follows：</p>
<p>Byte 1：Paly type</p>
<p>Byte 2~3：Program total. High byte first</p>
<p>Byte 4~5：Program number. High byte first</p>
<p>If the flag is 2：Read the current font information，Byte1~Byte6 as
follows：</p>
<p>Byte 1：Font type</p>
<p>Byte 2：Reserved</p>
<p>Byte 3~4: ASCII character available size. High byte first Byte 5~6:
Extended font available size. High byte first</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: Running info buffer size ,at least 7 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=6. success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_MakeScreenTestData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeScreenTestData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, BYTE* pInfoBuffer, int nInfLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make show the test pattern data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: Test pattern info buffer，Details are as follows： byte
0：Option：Bit7: 0 to cancel the test, 1 immediate access to the
test.</p>
<p>Bit6: 1 automatic return, 0 don’t automatically return</p>
</blockquote>
<p>Bit0~5: automatically returns the number of previous tests.</p>
<blockquote>
<p>When cancel the test, the latter parameter is invalid.</p>
<p>byte 1~2：Screen width. High byte first</p>
<p>0：defaule，&gt;0 Screen width</p>
<p>byte 3~4：Screen height. High byte first</p>
<p>0：defaule，&gt;0 Screen height</p>
<p>byte 5：Pattern color：Bit0~2：base color</p>
<p>Bit3：Whether the combination of the basic color</p>
<p>Bit4~7：Resvered, fill 0.</p>
<p>byte 6: Pattern gray: Bit0~3：Gray</p>
<p>Bit4~7：Resvered, fill 0.</p>
<p>byte 7: Test pattern：0: the entire screen</p>
<p>1: Single slash left</p>
<p>2: oblique grid line to the left other：Resvered, fill 0..</p>
<p>byte 8~9：Switching time, High byte first. Units of 10
milliseconds.</p>
<p>0 is the default time (3 seconds the entire screen, move 20 ms)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfLength: The test pattern data length, and now is 10 bytes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseScreenTestRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseScreenTestRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of show test pattern command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1. success</p>
<p>0: failed</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeInstantMessageData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeInstantMessageData( BYTE* pBuffer, int
nBufSize, byte byPlayTimes , int x , int y , int cx , int cy , byte
byFontSizeColor , int nEffect , byte nSpeed , byte byStayTime ,const
char* pText );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make instant message data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>pBuffer:Output data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: The size of the output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>byFontSizeColor: Font size and color.</p>
<p>Bit0~3: Font size.</p>
<p>Bit4: The weight of the red color</p>
<p>Bit5: The weight of the green color</p>
<p>Bit6: The weight of the blue color</p>
<p>Bit 7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: The length of the make data</p>
<p>&lt;=0: The result buffer is not big enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>This function only packs the message but not send. You should use it
with the functions: CP5200_MakeSendInstantMessageData and</p>
<p>CP5200_ParseSendInstantMessageRet</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_MakeInstantMessageData1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int MakeInstantMessageData1( BYTE* pBuffer, int
nBufSize, BYTE byPlayTimes , int x , int y , int cx , int cy , int
nFontSize ,byte byColorAlign , int nEffect , BYTE nSpeed , BYTE
byStayTime ,const char* pText );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make instant message data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>pBuffer:Output data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: The size of the output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7"></td>
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byColorAlign：color and alignment</p>
<p>Bit0: Red flag</p>
<p>Bit1: Green flag</p>
<p>Bit2: Blue flag</p>
<p>Bit3: Resvered</p>
<p>Bit4~5: Horizontal alignment. 0 Left, 1 Middle, 2 right</p>
<p>Bit6~7: Vertical alignment. 0 Top , 1 Middle , 2 Bottom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: The length of the make data</p>
<p>&lt;=0: The result buffer is not big enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>This function only packs the message but not send. You should use it
with the functions: CP5200_MakeSendInstantMessageData and</p>
<p>CP5200_ParseSendInstantMessageRet</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendInstantMessageData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendInstantMessageData(HOBJECT hObj,
BYTE* pBuffer, int nBufSize, const BYTE* pData, int nDataLen , byte
byLastPacket , long lDataOffset);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send instant message data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pData: The instant message data which is return of the function
CP5200_MakeInstantMessageDat.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nDataLen: The length of data. Low byte previous (little endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>byLastPacket: Whether is the last packet.</p>
<p>1: YES</p>
<p>0: NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>lDataOffset: The data offset, Low byte previous (little endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>This function sends the packet which is made by</p>
<p>CP5200_MakeInstantMessageData function. The length of each packet can
not bigger than 1024 bytes, 200 is proposition.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendInstantMessageRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendInstantMessageRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int
nInfoBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of send instant message command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: The length of the data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: 5 bytes.</p>
<p>Byte 1: 0x00:Failure. Not 0: Success</p>
<p>Other: Low byte previous (little endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadHWSettingData
>
> int CP5200_MakeReadHwSettingData(HOBJECT hObj, BYTE\* pBuffer, int
> nBufSize)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Make read scan param command data</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadHWSettingRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadHWSettingRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize , int
nPassword)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of read scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: Scan param buffer，at least 16 bytes，see the meaning of
each byte <u>1.14、The meaning of each byte of the scan
parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: The size of Scan param buffer，at least 16 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>16: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteHWSettingData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeWriteHWSettingData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, const BYTE* pSetting, int nPassword)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make write scan param command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSetting: Scan param buffer，16 bytes，see the meaning of each byte
<u>1.14</u>、</p>
<p><u>The meaning of each byte of the scan parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteHWSettingRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseWriteConfigRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of write scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Success</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadSoftwareSwitchInfoData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadSoftwareSwitchInfoData(HOBJECT hObj,
BYTE *pBuffer, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make read software switch info data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data(BYTE)</p>
<p>-1: Invalid data object handle</p>
<p>-4: Buffer len not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadSoftwareSwitchInfoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 1%" />
<col style="width: 21%" />
<col style="width: 11%" />
<col style="width: 47%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6">int CP5200_ParseReadSoftwareSwitchInfoRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int
nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td colspan="5"><blockquote>
<p>Parse return data of read software switch info data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td colspan="5"><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>pInfoBuffer: Software switch info buffer, software switch info
include 9</p>
<p>BYTEs</p>
</blockquote>
<p>Data Length Description</p></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>Switch info</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>0: off</p>
<blockquote>
<p>1: on</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><p>BYTE 1~2: Turn on hour, minute</p>
<blockquote>
<p>BYTE 3~4: Turn off hour, minute</p>
<p>BYTE 5~8: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>nInfoBufSize: The size of Software switch info buffer，at least 9
bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td colspan="5"><blockquote>
<p>1: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="5"><blockquote>
<p>0: Fail</p>
<p>-1: Incorrect data object handle</p>
<p>-2: Returned data type error</p>
<p>-3: Returned data len not enough</p>
<p>-4: Buffer size not enough</p>
<p>-5: Checksum error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td colspan="5"></td>
</tr>
</tbody>
</table>

> CP5200_MakeWriteSoftwareSwitchInfoData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 1%" />
<col style="width: 21%" />
<col style="width: 11%" />
<col style="width: 47%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6">int CP5200_MakeWriteSoftwareSwitchInfoData(HOBJECT hObj,
BYTE* pBuffer, int nBufSize, const BYTE *pSoftwareSwitchInfoBuf)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td colspan="5"><blockquote>
<p>Make write software switch info data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td colspan="5"><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>pSoftwareSwitchInfoBuf: Software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>Data</p>
</blockquote></td>
<td><blockquote>
<p>Length</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Switch info</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>0: Turn off immediately</p>
<blockquote>
<p>1: Turn on immediately</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td>Default: 0</td>
</tr>
<tr class="odd">
<td>Return</td>
<td colspan="5"><blockquote>
<p>&gt;0: Length of the output data(BYTE)</p>
<p>-1: Invalid data object handle</p>
<p>-4: Buffer len not enough</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td colspan="5"></td>
</tr>
</tbody>
</table>

> CP5200_ParseWriteSoftwareSwitchInfoRet
>
> int CP5200_ParseWriteSoftwareSwitchInfoRet(HOBJECT hObj, const BYTE\*
> pBuffer, int nLength, BYTE\* pInfoBuffer, int nInfoBufSize)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 1%" />
<col style="width: 21%" />
<col style="width: 11%" />
<col style="width: 47%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th colspan="5"><blockquote>
<p>Parse return data of write software switch info data</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7">Parameter</td>
<td colspan="5"><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>pInfoBuffer: Software switch info buffer, Software switch info
include at least 1 byte</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>Data</p>
</blockquote></td>
<td><blockquote>
<p>Length</p>
</blockquote></td>
<td>Description</td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Status</p>
</blockquote></td>
<td><blockquote>
<p>&gt;=1</p>
</blockquote></td>
<td><p>First byte：0 turn off screen，1 turn on screen</p>
<blockquote>
<p>Others: ignored</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>nInfoBufSize: The size of Software switch info buffer，at least 1
bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td colspan="5"><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
<p>-1: Incorrect data object handle</p>
<p>-2: Returned data type error</p>
<p>-3: Returned data len not enough</p>
<p>-4: Buffer size not enough</p>
<p>-5: Checksum error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td colspan="5"></td>
</tr>
</tbody>
</table>

> CP5200_MakeQueryControllerInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeQueryControllerInfo( HOBJECT hObj, BYTE*
pBuffer, int nBufSize, byte byInfoFlag, const BYTE *pAppendBuf, int
nAppendLen )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query controller information data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>byInfoFlag：Query flag , currently only support 0x0b</p>
<p>0x00：（invalid）</p>
<p>0x01：The current playing program number</p>
<p>0x02：Read current font information</p>
<p>0x0a: Query the check result in the program playing</p>
<p>0x0b: Query playing status and data others：retention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pAppendBuf：Append data</p>
<p>When query flag is 0x01 or 0x02, no append data.</p>
<p>When query flag is 0x0a, the append data only one byte, is 0x31. When
query flag is 0x0b, the append data length &gt;=1 bytes, to read the
information and parameters</p>
<p>The first byte =0 returns the screenshot data identification, program
number, program has been playing time.</p>
<p>The first byte =1 returns the screenshot data identification, program
number, program has been playing time, in addition to return in the
broadcast on the screen picture data. The second byte multiplied by 8 is
the number of bytes per packet data of a desired picture contains the 0
representation is determined by the control card.</p>
<p>The first byte=2 returns the actual image data. Second and three
bytes for the image datapacket sequence number, the high byte in the
front.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nAppendLen：Append data length</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data(BYTE)</p>
<p>-1: Invalid data object handle</p>
<p>-4: Buffer len not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseQueryControllerInfoRet

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseQueryControllerInfoRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength, byte byInfoFlag, byte byAppendFlag,
byte *pInfoBuf, int nInfoBufLen )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query controller information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>byInfoFlag：Query flag , currently only support 0x0b</p>
<p>0x00：（invalid）</p>
<p>0x01：The current playing program number</p>
<p>0x02：Read current font information</p>
<p>0x0a: Query the check result in the program playing</p>
<p>0x0b: Query playing status and data others：retention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byAppendFlag：</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuf：See below result cache description</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufLen：结果缓存长度</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Valid data length</p>
<p>0: The AppendFlag is invalid</p>
<p>-1: Incorrect data object handle</p>
<p>-2: Returned data type error</p>
<p>-3: Returned data len not enough</p>
<p>-4: Buffer size not enough</p>
<p>-5: Checksum error</p>
<p>-6: The return data error</p>
<p>-7: The “byInfoFlag” invalid.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

Result cache description

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Query flag</p>
</blockquote></th>
<th><blockquote>
<p>Return data description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x01：Query current play program number</p>
</blockquote></td>
<td><blockquote>
<p>5 bytes。</p>
<p>Byte 0: Play type.</p>
<p>Bit0~3: 0 general program,</p>
<p>Bit4: 0 the first set of programs, 1 second sets of programs Bit5~7:
reserves</p>
<p>Byte 1~2: The total number of bytes of program. High byte in the
front</p>
<p>Byte 3~4: Program number. High byte in the front</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0x02：Query current font</p>
</blockquote></td>
<td><p>6 bytes。</p>
<blockquote>
<p>Byte 0: font type</p>
<p>Byte 1: reserves</p>
<p>Byte 2~3: ASCII font available size. High byte in the front</p>
<p>Byte 4~5: extended fonts available size. High byte in the front</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0x0a ： Query the check result in the program playing， the append
data</p>
</blockquote></td>
<td><blockquote>
<p>Variable length, no more than 150 bytes.</p>
<p>Byte 0: Append value (with the transmitted value)</p>
<p>Byte 1~2: The total program numbers in play list. High byte in the
front</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>value must to be set to</p>
<p>0x31</p></td>
<td><p>Byte 3~4: checked program number. When it is broadcast program,
this value may be in error. High byte in the front</p>
<p>Byte 5~6: Program error message data length. High byte in the
front</p>
<p>Byte 7~: Program error message data. According to the program
sequence, each of the 8 program information is represented by 1 bytes (1
bits each program), 0 id not found error (alsomay not have to check), 1
identity is wrong.</p></td>
</tr>
<tr class="odd">
<td><p>0x0b：Query playing status and data</p>
<p>The return value is determined according to the append value</p></td>
<td><p>Append value is 0 and 1：</p>
<p>The append value of 0 to return to 0~17 bytes of information; the
append value of 1, also returns 18 bytes and the later data:</p>
<p>Byte 0~5: current screenshot data identifies</p>
<p>Byte 6~7: program number. High byte in the front, the first program
from the beginning of 1, 0 indicates no programs in play or play the
temporary information</p>
<p>Byte 8~9: playing item no..</p>
<p>Byte 10~13: program has broadcast time, the unit is 1/10 seconds,
high byte in the front</p>
<p>Byte 14~17: play item has the playing time, the unit is 1/10 seconds,
high byte in the front</p>
<p>Following</p>
<p>Byte 18~19: image width, high byte in the front</p>
<p>Byte 20~21: image height, high byte in the front</p>
<p>Byte 22: color and gray</p>
<p>Byte 23: multiplied by 8 for an image data packet length</p>
<p>Byte 24~27: image data length, high byte in the front Append value is
2:</p>
<p>Byte 0~5: current screenshot data identifies</p>
<p>Byte 6~7: the total number of image data packet, the high byte in the
front</p>
<p>Byte 8~9: image data packet sequence number, the high byte in the
front</p>
<p>Byte 10~13: image data offset, high byte in the front</p>
<p>Byte 14~15: image data length, high byte in the front</p>
<p>Byte 16~: image data</p></td>
</tr>
</tbody>
</table>

> CP5200_MakeOpenFileData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeOpenFileData(HOBJECT hObj, BYTE* pBuffer,
int nBufSize, const char* chFileName)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make open file data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>chFileName: The file name will to be open.If the file in the system
disk, name needs coupled with the “S:”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseOpenFileRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseOpenFileRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of open file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: file info buffer byte 0~1：file number，Low byte
first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: the file info buffer size ，require more than 2
bytes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Success , the file number will to be open</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-4: the info buffer length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeGetDirentryData
>
> int CP5200_MakeGetDirentryData(HOBJECT hObj, BYTE\* pBuffer, int
> nBufSize, WORD dno, int nPath)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Make get file info data</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dno: file number，Obtained by CP5200_ParseOpenFileRet</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPath：Path infp，user disk is 1，system disk is 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseGetDirentryRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseGetDirentryRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of get file info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: file info buffer</p>
<p>Byte 0 to 31: File Name</p>
<p>Bytes 32 to 43: the file name extension</p>
<p>Bytes 44 to 45: file attributes</p>
<p>Bytes 46 to 47: File checksum</p>
<p>Bytes 48 to 49: Reserved</p>
<p>Bytes 50 to 53: file generation time</p>
<p>Bytes 54 to 57: Date of file generation</p>
<p>Bytes 58 to 59: meaning unknown</p>
<p>Bytes 60 to 63: File Size</p>
<p>All data are low byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: the file info buffer size ，require more than 64
bytes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the file number</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-4: the info buffer length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeReadFileNoData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeReadFileNoData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize,WORD wdCount, byte fno)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make read file data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wdCount: the data length will to be read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>fno：file number，Obtained by CP5200_ParseOpenFileRet</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseReadFileNoRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseReadFileNoRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data read file data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pInfoBuffer: The file data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize: The file data buffer size, require more than 512
bytes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The length of the data has been read</p>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-4: the info buffer length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeCloseFileNoData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeCloseFileNoData(HOBJECT hObj, BYTE*
pBuffer, int nBufSize, byte fno)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make close file data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>fno：file number，Obtained by CP5200_ParseOpenFileRet</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Length of the output data</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseCloseFileNoRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseCloseFileNoRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength, BYTE*)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of close file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Incorrect data object handle</p>
<p>-2: return data error</p>
<p>-3: the returned data length less than</p>
<p>-4: the info buffer length less than</p>
<p>-5: checksum error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# API function for multi-window protocal data communication  {#api-function-for-multi-window-protocal-data-communication}

5.1、Overview of data communication API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 40%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th><blockquote>
<p>Function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_CmmPacker_Create</p>
</blockquote></td>
<td><blockquote>
<p>Create multi-window communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_CmmPacker_Destroy</p>
</blockquote></td>
<td><blockquote>
<p>Destroy multi-window communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_CmmPacket_SetParam</p>
</blockquote></td>
<td><blockquote>
<p>Set communication data packet parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_CmmPacker_Count</p>
</blockquote></td>
<td><blockquote>
<p>Get the number of packets in the object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CP5200_CmmPacker_Data</p>
</blockquote></td>
<td><blockquote>
<p>Get the data of packet in the object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>CP5200_MakeSplitScreenData</p>
</blockquote></td>
<td><blockquote>
<p>Make split window command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>CP5200_ParseSplitScreenRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>CP5200_MakeSendTextData</p>
<p>CP5200_MakeSendTextData1</p>
</blockquote></td>
<td><blockquote>
<p>Make send text command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>CP5200_ParseSendTextRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>CP5200_MakeSendTagTextData</p>
<p>CP5200_MakeSendTagTextData1</p>
</blockquote></td>
<td><blockquote>
<p>Make send tag text command data. Font, color , etc… can be controlled
by tag text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>CP5200_ParseSendTagTextRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send tag text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>CP5200_MakeSendPictureData</p>
</blockquote></td>
<td><blockquote>
<p>Make send picture command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>CP5200_ParseSendPictureRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send picture command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td><blockquote>
<p>CP5200_MakeSendStaticData</p>
</blockquote></td>
<td><blockquote>
<p>Make send static text command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td><blockquote>
<p>CP5200_ParseSendStaticRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send static text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td><blockquote>
<p>CP5200_MakeSendClockData</p>
</blockquote></td>
<td><blockquote>
<p>Make send clock command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17</td>
<td><blockquote>
<p>CP5200_ParseSendClockRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send clock command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>18</td>
<td><blockquote>
<p>CP5200_MakeExitSplitScreenData</p>
</blockquote></td>
<td><blockquote>
<p>Make exit split window command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19</td>
<td><blockquote>
<p>CP5200_ParseExitSplitScreenRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of exit split window</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>20</td>
<td><blockquote>
<p>CP5200_MakeSaveClearWndData</p>
</blockquote></td>
<td><blockquote>
<p>Make save or clear window data command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>21</td>
<td><blockquote>
<p>CP5200_ParseSaveClearWndRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of save or clear window data command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>22</td>
<td><blockquote>
<p>CP5200_MakePlaySelectedPrgData</p>
<p>CP5200_MakePlaySelectedPrgData1</p>
</blockquote></td>
<td><blockquote>
<p>Make select play program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>23</td>
<td><blockquote>
<p>CP5200_ParsePlaySelectedPrgRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of select play program command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>24</td>
<td><blockquote>
<p>CP5200_MakeSetUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Make set user variable command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>25</td>
<td><blockquote>
<p>CP5200_ParseSetUserVarRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of set user variable command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26</td>
<td><blockquote>
<p>CP5200_MakeSelectedAndUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Make selected and user variable data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>27</td>
<td><blockquote>
<p>CP5200__ParseSelectedAndUserVarRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of selected and user variable command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>28</td>
<td><blockquote>
<p>CP5200_MakeSetGlobalZoneData</p>
</blockquote></td>
<td><blockquote>
<p>Make set global zone data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>29</td>
<td><blockquote>
<p>CP5200_ParseSetGlobalZoneRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of set global zone command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>30</td>
<td><blockquote>
<p>CP5200_MakePushUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Make push user variable data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>31</td>
<td><blockquote>
<p>CP5200_ParsePushUserVarRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of push user variable data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>32</td>
<td><blockquote>
<p>CP5200_MakeTimerCtrlData</p>
</blockquote></td>
<td><blockquote>
<p>Make the timer ctronl data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>33</td>
<td><blockquote>
<p>CP5200_ParseTimerCtrlRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of timer contrl command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>34</td>
<td><blockquote>
<p>CP5200_MakeSetZoneAndVariableData</p>
</blockquote></td>
<td><blockquote>
<p>Make set global zone and user variable value data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>35</td>
<td><blockquote>
<p>CP5200_ParseSetZoneAndVariableRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of set global zone and user variable value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>36</td>
<td><blockquote>
<p>CP5200_MakeSendPureTextData</p>
</blockquote></td>
<td><blockquote>
<p>Make send pure text data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>37</td>
<td><blockquote>
<p>CP5200_ParseSendPureTextRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse the return data of send pure text</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage：
>
> Step 1: Create multi-window communication data object
>
> Step 2: Make communication data, include RS232/485's code convert
>
> (0xa5 =\> 0xaa 0x05, ...), or network ID code
>
> Step 3: Get the number of packets in the object
>
> Step 4: One by one to handle each packet of data by the following
> manner：

1.  Send the packet data to the controller

2.  Receive data from controller, and process code convert

> (0xaa 0x05 =\> 0xa5, ...)

3.  Parse the return data and get the result

> Step 5: Destroy multi-window communication data object

5.2 、 Detail of multi-window protocal data

communication API functions

> CP5200_CmmPacker_Create

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_ CmmPacker_Create(int nCommType, BYTE
byCardID, DWORD dwIDCode)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Create multi-window communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCommType: RS232/485 or network communication type</p>
<p>0: RS232/485</p>
<p>1: Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwIDCode: Network ID code of the controller. RS232 ignore it.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>Handle of multi-window communication data object, all these kind of
API functions use this handle</p>
<p>Return NULL if fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>When an application no longer requires a given object, it should be
destroyed to free the resource.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_CmmPacker_Destroy

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_CmmPacker_Destroy(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Destroy multi-window communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of multi-window communication data object to de
destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: No error</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_CmmPacket_SetParam
>
> HOBJECT CP5200_CmmPacket_SetParam (HOBJECT hObj, int nParamType, const
> char

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">*pParamString)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set data packet communication parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nParamType：Parameter type，valid value 1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pParamString：Parameter string</p>
<p>When parameter type is 1，pParamString is controller’s device ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: No error</p>
<p>0: Parameter type is wrong</p>
<p>-1: Invalid data object handle</p>
<p>-2: pParamString is wrong</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_CmmPacker_Count

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_CmmPacker_Count(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get the number of packets in the object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_CmmPacker_Data

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_CmmPacker_Data(HOBJECT hObj , BYTE *pBuffer,
int nBufSize, int nPackIndex )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get the data of packet in the object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: Output data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Size of output data buffer (BYTE)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPackIndex: Pack index,starting from 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the length of packet data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSplitScreenData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSplitScreenData(HOBJECT hObj, int
nScrWidth, int nScrHeight, int nWndCnt, const int *pWndRects);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make split window command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrWidth: the width of screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrHeight: the height of screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt: the split window number ，RMS 1~8。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndRects: Window coordinates, each window with four integer said
the</p>
<p>"left, up,right,down” coordinates,ave the same data structure with
the</p>
<p>"RECT"of windows。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSplitScreenRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSplitScreenRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendTextData
>
> (CP5200_MakeSendTextData1)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendTextData(HOBJECT hObj, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int
nEffect, int nStayTime, int nAlignment);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send text command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>CP5200_MakeSendTextData1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendTextRet
>
> int CP5200_ParseSendTextRet(HOBJECT hObj, const BYTE\* pBuffer, int
> nLength)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Parse return data of send text command</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendTagTextData (CP5200_MakeSendTagTextData1)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendTagTextData(HOBJECT hObj, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int
nEffect, int nStayTime, int nAlignment)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send tag text data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: indow sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor:Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed:Show speed</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect:Render effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment。</p>
<p>0: Left alignment</p>
<p>1: Center alignment</p>
<p>2: Right alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of packets</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>CP5200_MakeSendTagTextData1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendTagTextRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendTagTextRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of send tag text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength The length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendPictureData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendPictureData(HOBJECT hObj, int nWndNo,
int nPosX, int nPosY, int nCx, int nCy, const char *pPictureFile, int
nSpeed, int nEffect, int nStayTime, int nPictRef);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send picture command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nCx: The width of picture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCy: The heigth of picture</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>pPictureFile: Path and file name of the picture file ,this is based
on the value of nPictRef.</p>
<p>When the value of nPictRef is 0: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 1: pPictureFile is the Path and file
name of the GIF file on the controller card.</p>
<p>When the value of nPictRef is 2: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 3: pPictureFile is the Path and file
name of picture packages and the serial number of the picture on the
controller card.</p>
<p>Packages name followed by is separated by a space. For example:</p>
<p>“images.rpk 1”</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPictRef: the way to send picture and meaning.</p>
<p>0：display the local picture that will be converted into the format
of GIF to send.</p>
<p>1：display the gif picture that on the controller card.</p>
<p>2：display the local picture that will be converted into the format
of simple to send.</p>
<p>3：display the picture in the picture packages that on the controller
card.</p>
<p>Other values: deal with 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendPictureRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendPictureRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send picture command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendSimpleImageData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendSimpleImageData(HOBJECT hObj, int
nWndNo, int nPosX, int nPosY, int nSpeed, int nEffect, int nStayTime,
BYTE* pPicData , long lPicDataLen );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send simple image command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPicData: simple picture data,see the <u>1.11 simple picture data
fomart.</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>lPicDataLen:the length of simple picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_ParseSendSimpleImageRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendSimpleImageRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send simple picture command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendStaticData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendStaticData(HOBJECT hObj, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nAlignment, int
x, int y, int cx, int cy);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send static text command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>x: Start X of the play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y: Start Y of the play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>cx: The width of play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>cy: The height of play window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendStaticRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendStaticRet (HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send static text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendClockData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendClockData(HOBJECT hObj, int nWinNo ,
int nStayTime , int nCalendar , int nFormat , int nContent , int nFont ,
int nRed , int nGreen , int nBlue , LPCSTR pTxt);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send clock command data</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="11">Parameter</th>
<th><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nStayTime: Stay time in second。</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nCalendar: Calendar 0: Gregorian calendar date and time</p>
<p>1: Lunar date and time</p>
<p>2: Chinese lunar solar terms</p>
<p>3: Lunar time and date + Solar Terms</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nFormat: Format bit 0: when the system (0: 12 hour; 1: 24 hours
system) bit 1: Year digit (0: 4; 1: 2) bit 2: Branch (0: single; 1:
multi-line)</p>
<p>bit 3~5: Format control, such as the November 12, 2010 Friday ,
according to diffenert values expressed as: 0: 2010/11/12 Friday
16:20:30</p>
<p>1: Fri，12/11/2010 16:20:30</p>
<p>2: 2010-11-12 Fri. 16:20:30</p>
<p>3: Friday，12 November 2010 16:20:30 4: Fri，Nov 12,2010 16:20:30</p>
<p>5: Friday，November 12 2010 16:20:30</p>
<p>6: Fri，11/12/2010 16:20:30 7: 2010/11/12，Fri.16:20:30 bit 6: show
hands,marks bit 7: Transparent</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nContent: Content</p>
<p>By bit to determine the content to display.</p>
<p>bit 7: Pointer bit 6: weeks bit 5: seconds bit 4: minute bit 3: hour
bit 2: day bit 1: month bit 0: year</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nFont: Font，Bit0~3: font size</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nRed: The red color component</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nGreen: The red green component</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nBlue: The red blue component</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>pTxt: Text string to the end of 0x00.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendClockRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendClockRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send clock command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeExitSplitScreenData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_MakeExitSplitScreenData(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make exit split window command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseExitSplitScreenRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseExitSplitScreenRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of exit split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSaveClearWndData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_MakeSaveClearWndData(HOBJECT hObj, int
nSavaOrClear);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make save or clear window data command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSavaOrClear：Save or clear data 0: Save data to the flash.</p>
<p>1: Clear data from the flash.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSaveClearWndRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSaveClearWndRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of save or clear window data command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakePlaySelectedPrgData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakePlaySelectedPrgData(HOBJECT hObj, const
WORD *pSelected, int nSelCnt, int nOption)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make select play program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakePlaySelectedPrgData1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakePlaySelectedPrgData1(HOBJECT hObj, const
WORD *pSelected, int nSelCnt, int nOption , int nScrWidth, int
nScrHeight , byte byColorGray , byte nWndCnt )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make select play program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrWidth：Screen width</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrHeight：Screen height</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byColorGray：color gray</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt：window count</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParsePlaySelectedPrgRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParsePlaySelectedPrgRet (HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of select play program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSetUserVarData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSetUserVarData(HOBJECT hObj, int bSave ,
int nVarNum , int bAstride , int* nVarLen , byte* byNoData );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set user variable command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bSave: Bit0:Whether to save all variables to the flash 0:No
save，1:Save。</p>
<p>Bit1~7: Reserved,set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarNum: Variable number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted; 1 is permit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：Bytes of data specified for each variable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byNoData：Specified number of variables and variable data for each
variable, the first byte of each variable is the variable number,
followed by a specified length of variable data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Corresponds to a variable number of each variable area size of each
variable region is 32 bytes. Multiple continuous variables can be linked
to a variable area used,occupied area of the variable number of
variables can not be used。</p>
<p>When does not allow cross-variable area, more than 32 bytes of data
are discarded；When allow cross-variable area,calculate the length of
the data area to use the number of variables.</p>
<p>Valid values for the variable number is 1~100。Number of variables
corresponding to each variable area can store 32 bytes of data, a number
of continuous variable area can be used together for a variable, the
variable area occupied number of variables can not be used。</p>
<p>When variable values are not updated and just save the variable value
to the FLASH, it can set the " nVarNum " of the value of 0, set the "
bSave " to save</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseSetUserVarRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSetUserVarRet (HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set user variable command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSelectedAndUserVarData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSelectedAndUserVarData(HOBJECT hObj, int
nOption , int nVarNum , int bAstride , int* nVarLen , byte* byNoData,
int nSelPrg)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>作用</td>
<td><blockquote>
<p>Make selected and user variable command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>参数</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nOption:</p>
<p>Bit0: Whether to save the program number to the FLASH</p>
<p>0:Not save, 1: Save</p>
<p>Bit1: Whether to save all the variables to the FLASH</p>
<p>0:Not save, 1: Save</p>
<p>Bit2: Whether to clear the old variables</p>
<p>0:Not clear, 1:Clear</p>
<p>Bit3~7: Reserved,set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarNum: Variable Number。Bit0~6：The variable number which to be
set</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted; 1 is permit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen: Variable data length.Sort every variable byte data in
alphabet order.The total length of variable number and data is
(1+n)byte.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>byNoData: Variable No and data. The first byte is variable No,
followed by a specify length data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelPrg: Program No.The List of the selected program No.Each
program</p>
<p>No has 2 bytes,high byte is previous.The overflow program will be
ignored.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>返回值</td>
<td><blockquote>
<p>&gt;=0: the number of packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>其它说明</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSelectedAndUserVarRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSelectedAndUserVarRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>作用</td>
<td><blockquote>
<p>Parse return data of selected and user variable command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSetGlobalZoneData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSetGlobalZoneData(HOBJECT hObj, byte
byConfig , byte bySynchro , byte byZoneNum , byte *byZoneMsg)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>作用</td>
<td><blockquote>
<p>Make set global messge command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">参数</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig:</p>
<p>Bit0: Whether to save to FLASH</p>
<p>0:Not save, 1:Save</p>
<p>Bit1~7:Reserved, set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>bySynchro: Synchronization。</p>
<p>Bit0: Whether to synchronization, 0 Not synchronous，1
synchronous。</p>
<p>Bit1~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byZoneNum: Zone number.The golobal display zone number which to be
set.Cancel all the zone when zone number is 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byZoneMsg: Zone definition, the size of the zone is zone count
multiply 16 bytes. See in “1.7 global zone message format”.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>返回值</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>其它说明</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSetGlobalZoneRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSetGlobalZoneRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set global message command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakePushUserVarData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakePushUserVarData( HOBJECT hObj, byte
byOption , byte byVarZoonNum , byte byVarDataLen , byte* pVarNoAndData
)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make push and user variable command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0:Whether to save all the variable to the FLASH</p>
<p>0:Not Save 1:Save</p>
<p>Bit1: Push direction. 0:push back 1:push forward Bit2~3: Reserved,
set to 0.</p>
<p>Bit4~7: Push count. +1 is the push of zoon number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byVarZoonNum: Zoon number.</p>
<p>Bit0~6:the zoon numbe which to be pushed:1~100</p>
<p>Bit7: Reserved, please set 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byVarDataLen: Variable data length.Sort every variable byte data in
alphabet order.The total length of variable number and data is
(1+n)byte.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pVarNoAndData: Variable No and data. The first byte is variable No,
followed by a specify length data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParsePushUserVarRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParsePushUserVarRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of push and user variable command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeTimerCtrlData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeTimerCtrlData( HOBJECT hObj, byte
byTimerNo , byte byCmd , byte byProp ,</p>
<p>DWORD dwValue )</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make timer ctrlon command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byTimerNo: Timer no,set the Timer by byte,1 is activity Bit0: Timer
1.</p>
<p>Bit1: Timer 2</p>
<p>Bit3: Timer 3</p>
<p>Bit4: Timer 4</p>
<p>Bit5: Timer 5</p>
<p>Bit6: Timer 6.</p>
<p>Bit7: Timer 7.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byCmd: Action。 1： Initializtion Timer</p>
<p>2： Reset Timer</p>
<p>3： Start Timer 4： Puse Timer</p>
<p>Other：Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>byProp: Property. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>Bit0: 0 Time, 1 count down</p>
<p>Bit1: 0 pause, 1 start immediately</p>
<p>Bit2~3: Reserved</p>
<p>Bit4~7: time count</p>
<p>Set to 0 when the action is other.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwValue: Value. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>The initialization value when count down, in seconds.</p>
<p>High byte previous.</p>
<p>Set to 0 when timing.</p>
<p>Set to 0 when the action is other.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The numbe of the packets.</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_ParseTimerCtrlRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseTimerCtrlRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of timer crtlon command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSetZoneAndVariableData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSetZoneAndVariableData(HOBJECT hObj,
const BYTE* pZoneData, int nZoneLen, const BYTE* pVariableData, int
nVarLen, WORD wCtrl, WORD wReserved)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set global zone and user variable value data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pZoneData：The global zone data. Including the zone Options, the
number of zone, zone number, the zone defined.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nZoneLen：The global zone data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pVariableData：Variable data, including variable options, variable
data and</p>
<p>cross-district allows ,the length of the variable data table, the
variable number and data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：The variable data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wCtrl：Effective control parameters play times, high byte first.</p>
<p>The value of 0 has been effective .</p>
<p>Bit15: Resvered, fill 0.</p>
<p>Bit0~14: Display times.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wReserved：resvered</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The numbe of the packets.</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>After use this conmand, the global zone to be automatic into
synchronous display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_ParseSetZoneAndVariableRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSetZoneAndVariableRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of set global zone and user variable value</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendPureTextData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendPureTextData(HOBJECT hObj, int
nWndNo, const char *pText, COLORREF crColor, int nFontSize, int nSpeed,
int nEffect, int nStayTime, int nAlignment);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send pure text data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The numbe of the packets.</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendPureTextRet
>
> int CP5200_ParseSendPureTextRet(HOBJECT hObj, const BYTE\* pBuffer,
> int nLength)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Parse the return data of send pure text data</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_MakeSendMultiProtocol

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_MakeSendMultiProtocol(HOBJECT hObj, int
nItem, const BYTE *pText, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send multi protocol data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nItem: Items of multi protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Datas of multi protocol，see<u>《 C-Power external calls
communication</u> <u>protocol》send multi protocol data CC=0x60 Data
item</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength:Length of datas</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The numbe of the packets.</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_ParseSendMultiProtocolRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_ParseSendMultiProtocoltRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of send multi protocol data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# Template data communication API function  {#template-data-communication-api-function}

6.1、Overview of template data communication API functions

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 55%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No</p>
</blockquote></th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSetProgramTemplateData
CPowerBox_MakeSetProgramTemplateData1</p>
</blockquote></td>
<td><blockquote>
<p>Make set program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSetProgramTemplateRet</p>
</blockquote></td>
<td><blockquote>
<p>Pare return data of set program template command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeInOutProgramTemplateData</p>
</blockquote></td>
<td><blockquote>
<p>Make the in or out program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseInOutProgramTemplateRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of in or out program template command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeQueryProgramTemplateData
CPowerBox_MakeQueryProgramTemplateData1</p>
</blockquote></td>
<td><p>Make the query program</p>
<blockquote>
<p>template data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseQueryProgramTemplateRet</p>
</blockquote></td>
<td>Parse the return data of query program template data.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeDeleteProgramData</p>
</blockquote></td>
<td><blockquote>
<p>Make delete program command data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseDeleteProgramRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of delete program command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSendTextData</p>
</blockquote></td>
<td><blockquote>
<p>Make send text command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSendTextRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send text command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSendPictureData</p>
</blockquote></td>
<td><blockquote>
<p>Make send picture command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSendPictureRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of send picture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSendClockOrTemperatureData</p>
</blockquote></td>
<td><blockquote>
<p>Make send clock and temperature command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSendClockOrTemperatureRet</p>
</blockquote></td>
<td>Parse return data of send clock and temperature command</td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSetAloneProgramData</p>
</blockquote></td>
<td>Make set alone program command data</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSetAloneProgramRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of set alone program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeQueryProgramData</p>
</blockquote></td>
<td><blockquote>
<p>Make query program command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseQueryProgramRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of query program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSetProgramPropertyData</p>
</blockquote></td>
<td><blockquote>
<p>Make set program property command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSetProgramPropertyRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of set program property command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeSetScheduleData</p>
</blockquote></td>
<td><blockquote>
<p>Make set schedule command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseSetScheduleRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of set set schedule command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeDeleteScheduleData</p>
</blockquote></td>
<td>Make delete schedule command data</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseDeleteScheduleRet</p>
</blockquote></td>
<td>Parse return data of delete schedule command</td>
</tr>
<tr class="even">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_MakeGetScheduleData</p>
</blockquote></td>
<td><blockquote>
<p>Make get schedule command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_ParseGetScheduleRet</p>
</blockquote></td>
<td><blockquote>
<p>Parse return data of get schedule command</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage：
>
> Step 1: Create template communication data object
>
> Step 2: Make communication data, include RS232/485's code convert
>
> (0xa5 =\> 0xaa 0x05, ...), or network ID code Step 3: Get the number
> of packets in the object
>
> Step 4: One by one to handle each packet of data by the following
> manner：

4.  Send the packet data to the controller

5.  Receive data from controller, and process code convert

> (0xaa 0x05 =\> 0xa5, ...)

6.  Parse the return data and get the result

> Step 5: Destroy template communication data object

6.2、Detail of template data communication base API functions

> CPowerBox_MakeSetProgramTemplateData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_MakeSetProgramTemplateData(HOBJECT
hObj, byte byColor ,USHORT nWidth ,</p>
<p>USHORT nHeight , byte nWndNum , byte *byDefParam , byte*
pWndParam);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeSetProgramTemplateData1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_MakeSetProgramTemplateData(HOBJECT
hObj, byte byColor ,USHORT nWidth ,</p>
<p>USHORT nHeight , byte nWndNum , BYTE byOption, byte *byDefParam ,
byte* pWndParam);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Forced into the program template run</p>
<p>Bit1: Save the template position. 0: user disk, 1: system disk.</p>
<p>If the template is saved to the system tray, the original template of
the user tray is cleared; if the template is saved to the user's disk,
the original template of the system disk is cleared。</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSetProgramTemplateRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseSetProgramTemplateRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set program template command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeInOutProgramTemplateData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeInOutProgramTemplateData(HOBJECT
hObj,byte byInOrOut );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make in or out program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byInOrOut: In or Out。 1: In the program template</p>
<p>0: Out the program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseInOutProgramTemplateRet
>
> int CPowerBox_ParseInOutProgramTemplateRet(HOBJECT hObj, const BYTE\*
> pBuffer, int

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of in or out program template command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeQueryProgramTemplateData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeQueryProgramTemplateData(HOBJECT hObj
);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of template communication data object to de
destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeQueryProgramTemplateData1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeQueryProgramTemplateData(HOBJECT hObj
, byte byFlag );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query program template command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:</p>
<p>Bit0: Whether to query program template status parameter</p>
<p>Bit1:Whether to return the template definition color gray, screen
size information</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CPowerBox_ParseQueryProgramTemplateRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseQueryProgramTemplateRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength ,BYTE* pInfoBuffer, int
nInfoBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query program template command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize:Length of the return information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pInfoBuffer" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x83</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data of query program template
status parameter.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Options</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value of “Options”.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Template mode</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Not program template</p>
<p>1: program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Template status</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: template availability</p>
<p>0: the template is not available</p>
<p>1: the template can be used others: Reserved</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Color gray</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Color and gray。</p>
<p>Same with define“set program template”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen width</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen height</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Window count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Play window count。</p>
<p>Supports up to 10 play windows</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_MakeDeleteProgramData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeDeleteProgramData(HOBJECT hObj,byte
byConfig , byte byProNum , byte* pDelPro );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make delete program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig:</p>
<p>Bit0: The range of the delete program</p>
<p>0：Delete all program</p>
<p>1：Delete the specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNum: The program number. Do not need this item when delete all
the programs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDelPro: The delete program list. Each program is represent by 1
byte, start from 1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CPowerBox_ParseDeleteProgramRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseDeleteProgramRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of delete program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeSendTextData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeSendTextData(HOBJECT hObj, DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byProp , byte
*byShowFormat , char* pText);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send text command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProp: Property，Bit0~3: Text type 0：Common Text</p>
<p>Bit4: Display format. 0: default format 1:specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byShowFormat: Show format. Do not need this item when the property’s
display format is 0.</p>
<p>Byte0~1: Stay time,High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text data, end with ‘0x00’</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets</p>
<p>-1: Invalid data object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSendTextRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Int CPowerBox_ParseSendTextRet(HOBJECT hObj, const BYTE*
pBuffer, int nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of send text command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeSendPictureData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeSendPictureData(HOBJECT hObj,DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byPicType , byte
*byShowFormat , byte* pPicData , long lPicDataLen);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make send picture command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPicType: Picture type. Bit0~3: Picture type</p>
<p>1: Data of GIF picture file which include the information of the
picture’s width and height so on.</p>
<p>2: The stored GIF filename in the contrl card.</p>
<p>4. Simple picture data, Check the format information at ”Simple
Picture data format”</p>
<p>Bit4: Show format. 0 default format,1 specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>byShowFormat: Show format.</p>
<p>Do not need this item when the property’s display format is 0.</p>
<p>Byte0~1: Stay time, High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Show effect See”Show effect code”</p>
<p>Byte4: Picture style(zoom、tile), see “Picture style code”</p>
<p>Byte5: Reserved</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pPicData: Picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>lPicDataLen: Picture data length.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets -1: Invalid data object handle.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSendPictureRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseSendPictureRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send picture command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3">Return</td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeSendClockOrTemperatureData
>
> int CPowerBox_MakeSendClockOrTemperatureData(HOBJECT hObj,DWORD
> dwAppendCode , BYTE byProNo , BYTE byWndNo , BYTE byProgramType , UINT
> nPropLen , BYTE\* pProgramProp )

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Make send clock and temperature command data</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byProgramType: Program type Bit0~3: Type</p>
<p>2：Clock ; 3：Temperature Bit4: Display format.</p>
<p>0: default format 1:specify format</p>
<p>Bit5~7: Reserved, fill in 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPropLen: Property length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pProgramProp：Program property</p>
<p>The meaning of the attribute data according to different types</p>
<p>Type = 2 , see <u>Clock/Calendar type</u> proprtey</p>
<p>Type = 3 , see <u>Temperature and Humidity type</u> proprtey</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets -1: Invalid data object handle.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSendClockOrTemperatureRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseSendClockOrTemperatureRet(HOBJECT
hObj, const BYTE* pBuffer, int nLength , BYTE* pInfoBuffer, int
nInfoBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of send clock and temperature command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize:Length of the return information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pInfoBuffer" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x87</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to show
clock/temperature in the specified window of the specified program</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Program No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>The same value with send value “Program no”.</p>
<blockquote>
<p>Valid value:1~100</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Window No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value “Window no”. Valid value:1~10,Invalid
when out of program template definition.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Packet loss number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The number of packets that have not yet received. Sends the first
packet loss number is the total number of packets minus one.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>The packet number of the packet loss</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Packet loss packet number. Always in accordance with small to large;
the first packet packet number is 0. Each package a byte.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_MakeSetAloneProgramData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeSetAloneProgramData(HOBJECT hObj,
DWORD dwAppendCode , BYTE byProgramNo , BYTE byWindowCnt ,BYTE*
pWndParam, BYTE* pWndData)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set alone program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWindowCnt: Window count. Valid value:1～10</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>pWndParam：windows parameter</p>
<p>Every window information table has a 22 bytes length parameter. The
1~16 bytes are window position and property, You can see the detail at
<u>1.13.</u> <u>Window position and property</u>; The 17~19 bytes are
window data offset; The 20~22 bytes are window data length. High byte
first.</p>
<p>If no data ,then window data offset and window data length all are
0.</p>
<p>The total length of the data is: the number of the window*22.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndData：Window play data:“Text”、“Picture”…</p>
<p>Byte 1：Data Type(1 Text；4 Picture)</p>
<p>Byte 2：Data Format（Like “Text type” in command 0x85 and “Picture
type” in command 0x86）</p>
<p>Byte 3：Text data or picture data。</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets -1: Invalid data object handle.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSetAloneProgramRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_ParseSetAloneProgramRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength ,</p>
<p>BYTE* pInfoBuffer, int nInfoBufSize )</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set alone program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize:Length of the return information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
<p>0x01 program template is invalid</p>
<p>0x11 program number is out of range</p>
<p>0x12 window number out of range</p>
</blockquote>
<p>0x13 The definition of the window outside the screen size of
the</p></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>program template definition</p>
<p>0x80 currently is not program template way</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pInfoBuffer" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th>Lenght(byte)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x88</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to send alone
program</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td>4</td>
<td>The user’s append code, high byte previous.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Program No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Valid value:1~100</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reserved</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Reserved, fill in 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Packet loss number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The number of packets that have not yet received. Sends the first
packet loss number is the total number of packets minus one.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>The packet number of the packet loss</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Packet loss packet number. Always in accordance with small to large;
the first packet packet number is 0. Each package a byte.</p>
</blockquote></td>
</tr>
</tbody>
</table>

\*Must first send the first packet. Best to confirm the first packet
sent successfully, and then send subsequent packets.

- The meaning of \"return value\" in the return packet:

> 0x01 program template is invalid
>
> 0x11 program number is out of range
>
> 0x12 window number out of range
>
> 0x13 The definition of the window outside the screen size of the
> program template definition 0x80 currently is not program template way
>
> CPowerBox_MakeQueryProgramData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeQueryProgramData(HOBJECT hObj , byte
byFlag , byte* pParam )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make query program command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:Special which program info will to be query 1: Query valid
programs count and program number 2: Query specifies program
information.</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pParam:</p>
<p>If “byFlag” is 1：byte1~5，resvered，fill 0</p>
<p>If “byFlag” is 2：：byte1，program number；byte2~5，resvered，fill
0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets -1: Invalid data object handle.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseQueryProgramRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseQueryProgramRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength ,BYTE* pInfoBuffer, int nInfoBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of query program command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize:Length of the return information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pInfoBuffer" have the following meanings:

 Query"valid program count and program number"

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Valid program number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Each byte identifies an effective program。</p>
<p>Valid value 1～100。</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag

 Query specifies program information

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Now only return one information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Program number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Program number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>User append</p>
<blockquote>
<p>code</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>User append code</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag
>
> 0x11 Invalid programs
>
> 0x12 Can't get program information
>
> CPowerBox_MakeSetProgramPropertyData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeSetProgramPropertyData(HOBJECT hObj,
byte byOption , byte byProgramCnt , byte* pPrograms , byte byPropertyID1
, byte byPropertyID2 , byte byProgramLevel , USHORT nLoopCnt , USHORT
nTime , byte* pDuetime , byte* pTimeInterval);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set program property command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Set the range of the program property</p>
<p>0: All programes</p>
<p>1: Specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramCnt:The count of the program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPrograms: The list of the programes</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>ByPropertyID1：Property ID 1, marked which property you want to set
by</p>
<p>byte, set 0 if the data not exist.</p>
<p>Bit0: The level of the program.</p>
<p>Bit1: The cycle count.</p>
<p>Bit2: Valid time. How long will the program be valid from now on.</p>
<p>Bit3: Interval time</p>
<p>Bit4~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ByPropertyID2: Property ID 2。Bit0~4: valid time. &gt;0 the count of
the valid time.&lt;=4</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramLevel: The program level. 1～3 level, The high level of the
program is priority.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nLoopCnt: Loop count, High byte previous(big-endian).</p>
<p>0: Do not play the program, use to shield program temporarily.</p>
<p>1~255: The loop count of the program.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nTime: Valid time. High byte previous (big-endian). In minute.</p>
<p>0: Not limit play time</p>
<p>&gt;0: Specify play time in minute.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDuetime: time limit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTimeInterval:The interval time. The start tag
“Hour/Minute/Second”and the end tag “Hour/Minute/Second” both represent
by one byte.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: The number of the packets -1: Invalid data object handle.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSetProgramPropertyRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseSetProgramPropertyRet(HOBJECT hObj,
const BYTE* pBuffer, int nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse the return data of set program property command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeSetScheduleData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeSetScheduleData(HOBJECT hObj, DWORD
dwAppendCode, BYTE byScheduleNo, const BYTE* pProperty, const BYTE*
pBoxes, BYTE byBoxCnt);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make set schedule command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byScheduleNo: Schedule number，Valid value 1~100。Total support 100
plans, For each plan No, the new data cover the old data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pProperty: play property，total 14 bytes： byte 0：Format and level：
Bit0~3: Data format，fill in 0x01</p>
<p>Bit4~7: Indicates the priority level. The priority level the greater
the value, the more priority to play, 0 is the lowest priority.。。</p>
<p>byte 1：Weekday：Bit0~6: 7-bit logo Sunday to Saturday byte 2~4 ：
Begin date ， 3 bytes: Byte1:Year,Valid value0~99,means</p>
<p>2000~2999; Byte2:Month ;Byte3:Day</p>
<p>byte 5~7：End date，3 bytes: Byte1:Year,Valid value0~99,means
2000~2999;</p>
<p>Byte2:Month ;Byte3:Day</p>
<p>byte 8~10：Begin time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second
byte 11~13：End time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBoxes: program number , each byte represents a program. Numbered
in</p>
<p>ascending order, do not repeat.....</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byBoxCnt:program number count, Valid value:1～100,</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseSetScheduleRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseSetScheduleRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of set set schedule command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
<p>0x01 program template is invalid</p>
<p>0x80 currently is not program template way</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeDeleteScheduleData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeDeleteScheduleData(HOBJECT hObj, DWORD
dwAppendCode, const BYTE* pSchs, BYTE bySchCnt)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make delete schedule command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pSchs: schedule number, Valid value 1~100。Each byte represents a
play schedule。</p>
<p>When delete all play schedule, the length of this data is one , value
is 0xff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bySchCnt: The number of play schedule will to be delete。0 means
delete all play plans.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CPowerBox_ParseDeleteScheduleRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseDeleteScheduleRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of delete schedule command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data</p>
<p>0x01 program template is invalid</p>
<p>0x11 The number of play plan will to be delete is 0. 0x80 currently
is not program template way</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_MakeGetScheduleData

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_MakeGetScheduleData(HOBJECT hObj, DWORD
dwAppendCode, BYTE byType, BYTE byScheduleNo)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Make get schedule command data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byType：0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byScheduleNo: Valid value:1~100。When query type is 0，this data fill
in 0。</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x8d</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Describe the package is the return data which to query play plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Query type</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Count /Number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>When query type is 0，this value is valid play schedule count</p>
<p>When query type is 1，this value is play schedule number.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_ParseGetScheduleRet

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_ParseGetScheduleRet(HOBJECT hObj, const
BYTE* pBuffer, int nLength, BYTE* pInfoBuffer, int nInfoBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Parse return data of get schedule command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>hObj: Handle of communication data object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuffer: The return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Length of the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfoBuffer: The return information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nInfoBufSize:Length of the return information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Invalid data object handle</p>
<p>-2: Incorrect return data</p>
<p>-3: Incorrect length of return data 0x01 program template is invalid
0x11 Don’t support the query type.</p>
<p>0x12 Invalid play plan no.</p>
<p>0x80 currently is not program template way</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pInfoBuffer" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Play schedule number table/ play schedule content</p>
</blockquote></th>
<th></th>
<th>Variable-length</th>
<th><blockquote>
<p>When query type is 0，this value is valid play schedule number
table</p>
<p>When query type is 1，this value is play schedule content. Data
format like command 0x8B.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You must deal with the return data according to the different query
type.

The meaning of \"return value\" in the return packet:

> 0x01 program template is invalid 0x11 Don't support the query type.
>
> 0x12 Invalid play plan no.
>
> 0x80 currently is not program template way

# Communication base API function  {#communication-base-api-function}

7.1、 Overview of RS232 communication base API

functions

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>No</th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_RS232_Init</p>
</blockquote></td>
<td><blockquote>
<p>Initialize serial port parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_RS232_InitEx</p>
</blockquote></td>
<td><blockquote>
<p>Initialize serial port parameters and set timeout</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_RS232_Open</p>
</blockquote></td>
<td><blockquote>
<p>Open serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_RS232_OpenEx</p>
</blockquote></td>
<td><blockquote>
<p>Open serial port，assigned reading and writing timeout</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CP5200_RS232_Close</p>
</blockquote></td>
<td><blockquote>
<p>Close serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>CP5200_RS232_IsOpened</p>
</blockquote></td>
<td><blockquote>
<p>Test whether the serial port has been opened</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>CP5200_RS232_Write</p>
</blockquote></td>
<td><blockquote>
<p>Write data to serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>CP5200_RS232_Read</p>
</blockquote></td>
<td><blockquote>
<p>Read data from serial port</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>CP5200_RS232_WriteEx</p>
</blockquote></td>
<td><blockquote>
<p>Write data to serial port，and processing for transcoding</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>CP5200_RS232_ReadEx</p>
</blockquote></td>
<td><blockquote>
<p>Read data from serial port，and processing for transcoding</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize serial port parameters
>
> Step 2: Open serial port
>
> Step 3: Read and write operations on the serial
>
> Step 4: Close serial port

7.2、Detail of RS232 communication base API functions

> CP5200_RS232_Init

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_Init(const char *fName, int
nBaudrate)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Initialize serial port parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>fName: RS232 serial port name，for example:“COM1”、“COM2”、…</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBaudrate: baud rate，for example :115200、57600、...</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Other serial port parameters are fixed:</p>
<p>Parity: No parity</p>
<p>Data bits: 8</p>
<p>Stop bits: 1</p>
<p>Flow Control: None</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_InitEx

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_InitEx(const char *fName, int
nBaudrate, DWORD dwTimeout);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Initialize serial port parameters and set timeout</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>fName: RS232 serial port name，for example:“COM1”、“COM2”、…</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBaudrate: baud rate，for example :115200、57600、...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwTimeout; time of timeout</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Other serial port parameters are fixed:</p>
<p>Parity: No parity</p>
<p>Data bits: 8</p>
<p>Stop bits: 1</p>
<p>Flow Control: None</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_RS232_Open

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_Open(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Open serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>None</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>After using the serial port, need to call CP5200_RS232_Close () to
close</p>
<p>Read, write, timeouts are set to 600 ms</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_RS232_OpenEx

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_OpenEx(DWORD dwReadTimeout, DWORD
dwWriteTimeout)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Open serial port，assigned reading and writing timeout</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>dwReadTimeout: Reading timeout. Units ms</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwWriteTimeout: Writing timeout. Units ms</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>After using the serial port, need to call CP5200_RS232_Close () to
close</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_RS232_Close

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_Close(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Close serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>None</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail or the serial port is the closed state</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_IsOpened

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_IsOpened(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>作用</td>
<td><blockquote>
<p>Test whether the serial port has been opened</p>
</blockquote></td>
</tr>
<tr class="even">
<td>参数</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>返回值</td>
<td><blockquote>
<p>1: Has been opened</p>
<p>0: No open</p>
</blockquote></td>
</tr>
<tr class="even">
<td>其它说明</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_Write

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_Write(const void* pBuf, int
nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write data to serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: Data buffer pointer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength: Data length</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail or the serial port is the closed state</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_Read

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_Read(void* pBuf, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read data from serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: Data buffer pointer, stored data of reading</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Data Buffer size</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>Data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_WriteEx
>
> int CP5200_RS232_WriteEx(const void\* pBuf, int nLength)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Write data from serial port，and processing for transcoding</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: Data buffer pointer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nLength: Data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: success</p>
<p>0: fail or the serial port is the closed state</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Add code “0XA5” at the beginning of the data and add code “0XAE” at
the end of the data, send data of processing for transcoding</p>
<p>0xa5 =&gt; 0xaa 0x05</p>
<p>0xaa =&gt; 0xaa 0x0a</p>
<p>0xae =&gt; 0xaa 0x0e</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_ReadEx

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_ReadEx(void* pBuf, int nBufSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read data from serial port，and processing for transcoding</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: pBuf: Data buffer pointer, stored data of reading</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Data Buffer size</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>Data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Read the data between beginning code “0xa5” and ending code</p>
<p>“0xae”,the return data not contain beginning code “0xa5” and ending
code</p>
<p>“0xae”,and processing for transcoding the data of between beginning
code</p>
<p>“0xa5” and ending code “0xae”</p>
<p>0xaa 0x05 =&gt; 0xa5</p>
<p>0xaa 0x0a =&gt; 0xaa</p>
<p>0xaa 0x0e =&gt; 0xae</p>
</blockquote></td>
</tr>
</tbody>
</table>

7.3、Overview of Network communication base API functions

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>No</th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>CP5200_Net_Init</td>
<td>Initialize network parameters</td>
</tr>
<tr class="even">
<td>2</td>
<td>CP5200_Net_SetBindParam</td>
<td>Bind client IP and port</td>
</tr>
<tr class="odd">
<td>3</td>
<td>CP5200_Net_Connect</td>
<td>Open network connections</td>
</tr>
<tr class="even">
<td>4</td>
<td>CP5200_Net_IsConnected</td>
<td>Test whether the network has been connected</td>
</tr>
<tr class="odd">
<td>5</td>
<td>CP5200_Net_Disconnect</td>
<td>Close network connections</td>
</tr>
<tr class="even">
<td>6</td>
<td>CP5200_Net_Write</td>
<td>Write data to network</td>
</tr>
<tr class="odd">
<td>7</td>
<td>CP5200_Net_Read</td>
<td>Read data from network</td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize network parameters
>
> Step 2: Open network connections
>
> Step 3: Read and write operations network
>
> Step 4: Close network connections t

7.4 、 Detail of network communication base API

functions

> CP5200_Net_Init

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_Init(DWORD dwIP, int nIPPort, DWORD
dwIDCode, int nTimeOut)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Initialize network parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>dwIP:IP address. For example: 192.168.1.100 is 0xc0a80164</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nIPPort:Port</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwIDCode:ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nTimeOut:timeout</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SetBindParam

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SetBindParam( DWORD dwClientIP , int
nClientPort )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Bind client IP and port</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>dwClientIP: Bind client IP。For example： 192.168.1.100 is
0xc0a80164</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nClientPort: Bind client port</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_Connect

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_Connect(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Open network connections</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
<p>-1: IP is not valid</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_IsConnected

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_IsConnected(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Test whether the network has been connected</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Has been connected</p>
<p>0: No connect</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_Disconnect

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_Disconnect(void)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Close network connections</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure or network has been turned off.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_Write

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_Write(const BYTE* pBuf, int
nLength);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write data to network</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: Data buffer pointer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength: Data length</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
<p>-1: Network is the closed state.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_Read

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_Read(BYTE* pBuf, int nSize)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read data from network</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>pBuf: Data buffer pointer, stored data of reading</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: Data Buffer size</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;0: Data length</p>
<p>0: Failure</p>
<p>-1: Network is the closed state.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# Running plan API function  {#running-plan-api-function}

C-Power5200 controller control running program by date ,week. Running
plan is saved as file int the controller,the file name is "playbill.rsf"
and it can't change.

> Running program API function in order to create "playbill.rsf" file.

8.1、Overview of running plan API functions

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>No</th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CP5200_Runsch_Create</p>
</blockquote></td>
<td><blockquote>
<p>Create running plan object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CP5200_Runsch_Destroy</p>
</blockquote></td>
<td><blockquote>
<p>Destroy running plan object</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CP5200_Runsch_AddItem</p>
</blockquote></td>
<td><blockquote>
<p>Add running plan item</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>CP5200_Runsch_SaveToFile</p>
</blockquote></td>
<td><blockquote>
<p>Save running plan to file</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Create running plan object
>
> Step 2: Add running plan item
>
> Step 3: Save running plan to file
>
> Step 4: Destroy running plan object

8.2、Detail of running plan API functions

> CP5200_Runsch_Create

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HOBJECT CP5200_Runsch_Create(int nPrgSum, int
nAttrib)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Create running plan object</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nPrgSum: total number of program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nAttrib: Attribute</p>
<p>0: Default time period is not playing any program</p>
<p>1: Default time period is not playing all program</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>Running plan object handle,called by this type of API</p>
<p>Return “NULL” is said failure to create</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Object to create successful and no longer in use, the object must be
destroyed</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Runsch_Destroy

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Runsch_Destroy(HOBJECT hObj)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Destroy running plan object</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>hObj: The running plan object handle to be destroy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: no error</p>
<p>-1: object handle is null</p>
<p>-2: wrong object handle</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Runsch_AddItem

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Runsch_AddItem(HOBJECT hObj, int nGrade, int
nWeekDateRelative, int nWeeks, const int* pBeginDate, const int*
pEndDate, const int* pBeginTime, const int* pEndTime, int nItemCnt,
const int *pItems)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Add running plan item</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>hObj: The running plan object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nGrade: plan item level，0~9level, More higher-level priority。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWeekDateRelative: the relationship of date and week</p>
<p>0: Execute this plan must that all of week and date are satisfy</p>
<p>1: Execute this plan must that one of week and date are satisfy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWeeks: week tag, value can be one or more of the following
combination of values</p>
<p>1: Sunday</p>
<p>2: Monday</p>
<p>4: Tuesday</p>
<p>8: Wednesday</p>
<p>16: Thursday</p>
<p>32: Friday</p>
<p>64: Saturday</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBeginDate: Start date. Three integer values denote "Year"
"Month"</p>
<p>"Day" respectively</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pEndDate: End date. Three integer values denote "Year" "Month" "Day"
respectively</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>pBeginTime: Start time. Three integer values denote "hour"
"minute"</p>
<p>"second" respectively</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pEndTime: End time. Three integer values denote "hour" "minute"</p>
<p>"second" respectively</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nItemCnt:The number of program want to play。The number can’t greater
than the number of the first parameter of the function</p>
<p>“CP5200_Runsch_Create” specified</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>pItems: The program number that will to be play.length is
”nItemCnt”</p>
<p>integer.Every integer is the number of program to be play.Program
number started from 0, and the number less than the first parameter of
the function “CP5200_Runsch_Create”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: success , plan item number</p>
<p>-1: Invalid object handle</p>
<p>-2: Error parameter</p>
<p>-3: Memory not enough</p>
<p>-4: Memory wrong</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Runsch_SaveToFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Runsch_SaveToFile(HOBJECT hObj, const char*
pFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Save running plan to file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>hObj: The running plan object handle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename: File path and name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: no error</p>
<p>-1: Invalid object handle</p>
<p>-3: File operater fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# Time-limite play information by week  {#time-limite-play-information-by-week}

C-Power5200 controller support play by period of time, Time-limite
informatin is saved as file and its name is "playbill.lpt" , the file
format as below:

| File head        |
|------------------|
| The frist record |
| ...              |
| The n record     |

> File head's length is 7 bytes and every recor's length is 7 bytes two.

The file only record the time-limite information of time-limite
program.Program of always played do not need to record any information
in this file.

9.1、Detail of file head

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>2</th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th>6</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>File</p>
<p>ID</p>
</blockquote></td>
<td colspan="2">Format version number</td>
<td colspan="2">Record number</td>
<td><blockquote>
<p>Reservations</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Date name</th>
<th><blockquote>
<p>Data size(byte)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>File ID</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Fixed for the "LT"。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Format version numbe</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0x0100(the frist byte is 0x00,the second byte is 0x01)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Record number</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>number of time-limite players recorded information， Low byte
first。</p>
</blockquote></td>
</tr>
</tbody>
</table>

# 9.2、Detail definition of time-limite play information by week  {#detail-definition-of-time-limite-play-information-by-week .unnumbered}

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>4</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
<th>6</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0x00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Program number</p>
</blockquote></td>
<td><blockquote>
<p>week</p>
</blockquote></td>
<td><blockquote>
<p>Begin minute</p>
</blockquote></td>
<td><blockquote>
<p>Begin hour</p>
</blockquote></td>
<td><blockquote>
<p>End minute</p>
</blockquote></td>
<td><blockquote>
<p>End hour</p>
</blockquote></td>
</tr>
</tbody>
</table>

Description：

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Data name</th>
<th><blockquote>
<p>Data size(byte)</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Program number</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Program number, started from 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>week</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Limited by week,use 7 bits, Each bit denote one day. If the day need
to play,set corresponding bit to 1 .</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Sunday：0x01</p>
<p>Monday：0x02</p>
<p>Tuesday：0x04</p>
<p>Wednesday：0x08</p>
<p>Thursday：0x10</p>
<p>Friday：0x20</p>
<p>Saturday：0x40</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Begin minute</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>Begin play time: minute(0~59)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Begin hour</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Begin play time: hour (0~23)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>End minute</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>End play time: minute (0~59)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>End hour</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>End play time: hour (0~23)</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Multi-window control API function  {#multi-window-control-api-function}

10.1、Overview of RS232 multi-window control API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 44%" />
<col style="width: 1%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>No</th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SplitScreen</p>
</blockquote></td>
<td><blockquote>
<p>Send split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendText</p>
<p>CP5200_RS232_SendText1</p>
</blockquote></td>
<td><blockquote>
<p>Send text to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendTagText</p>
<p>CP5200_RS232_SendTagText1</p>
</blockquote></td>
<td><blockquote>
<p>Send tag text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendPicture</p>
</blockquote></td>
<td><blockquote>
<p>Send picture to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendStatic</p>
</blockquote></td>
<td><blockquote>
<p>Send static text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendClock</p>
</blockquote></td>
<td><blockquote>
<p>Send clock to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_ExitSplitScreen</p>
</blockquote></td>
<td><blockquote>
<p>Exit split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SaveClearWndData</p>
</blockquote></td>
<td><blockquote>
<p>Save or clear split window mesage</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_PlaySelectedPrg</p>
<p>CP5200_RS232_PlaySelectedPrg1</p>
</blockquote></td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SetUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Set user variable</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SetSelectedAndUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Set selected and user var command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SetGlobalZone</p>
</blockquote></td>
<td><blockquote>
<p>Set global message command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>13</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_PushUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Push user data command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>14</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_TimerCtrl</p>
</blockquote></td>
<td><blockquote>
<p>Set Timer contrl command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SetZoneAndVariable</p>
</blockquote></td>
<td><blockquote>
<p>Set global zone and user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td>16</td>
<td colspan="2"><blockquote>
<p>CP5200_RS232_SendPureText</p>
</blockquote></td>
<td><blockquote>
<p>Send pure text to special window</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize serial port parameters
>
> Only record the serial parameter initialization parameter information,
> not the actual serial port operation。
>
> Step 2: Send split window command，
>
> If the window has been divided and have been met requirements, this
> step can be dispensed with, or to send the split window command。 Step
> 3: Send text or picture to window。

Note: This category interface need not to consider whether the serial
port has been opened , as long as the serial port parameters have been
initialized.。

10.2 、 Detail of RS232 multi-window control API

function

> CP5200_RS232_SplitScreen

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SplitScreen(int nCardID, int nScrWidth,
int nScrHeight, int nWndCnt, const int *pWndRects)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrWidth: the width of screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrHeight: the height of screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt: The window number of the screen will be splitted , valid
values 1~8。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndRects: Window coordinates, each window with four integer said
the</p>
<p>"left, up,right,down” coordinates,ave the same data structure with
the</p>
<p>"RECT"of windows。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: The window number was too much</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>This function sets sub-windows information and sends split-screen
commad.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendText
>
> (CP5200_RS232_SendText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendText(int nCardID, int nWndNo, const
char *pText, COLORREF crColor, int nFontSize, int nSpeed, int nEffect,
int nStayTime, int nAlignment);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text will to be sent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>CP5200_RS232_SendText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendTagText (CP5200_RS232_SendTagText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendTagText(int nCardID, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int
nEffect, int nStayTime, int nAlignment)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send tag text to specify window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text which to be sent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment 1: center Alignment 2: right Alignment:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>CP5200_RS232_SendTagText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendPicture

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendPicture(int nCardID, int nWndNo,
int nPosX, int nPosY, int nCx, int nCy, const char *pPictureFile, int
nSpeed, int nEffect, int nStayTime, int nPictRef)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send picture to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nCx: The width of picture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCy: The heigth of picture</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>pPictureFile: Path and file name of the picture file ,this is based
on the value of nPictRef.</p>
<p>When the value of nPictRef is 0: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 1: pPictureFile is the Path and file
name of the GIF file on the controller card.</p>
<p>When the value of nPictRef is 2: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 3: pPictureFile is the Path and file
name of picture packages and the serial number of the picture on the
controller card.</p>
<p>Packages name followed by is separated by a space. For example:</p>
<p>“images.rpk 1”</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPictRef: the way to send picture and meaning.</p>
<p>0：display the local picture that will be converted into the format
of GIF to send.</p>
<p>1：display the gif picture that on the controller card.</p>
<p>2：display the local picture that will be converted into the format
of simple to send.</p>
<p>3：display the picture in the picture packages that on the controller
card.</p>
<p>Other values: deal with 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: Param “nWndNo” is wrong</p>
<p>-10: Image file does not exist</p>
<p>-11: The specified file is not available to support the image
file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Final image is converted to 256 color pictures to send, if given a
true color image, there may be color changes.</p>
<p>Image size will be stretched or compressed to fit the size of the
specified</p>
<p>window。</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendSimpleImageData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendSimpleImageData(int nCardID, int
nWndNo, int nPosX, int nPosY, const char *pPictureFile, int nSpeed, int
nEffect, int nStayTime, BYTE* pPicData , long lPicDataLen)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send simple picture to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPicData: simple picture data,see the <u>1.11 simple picture data
fomart.</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>lPicDataLen:the length of simple picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: Param “nWndNo” is wrong</p>
<p>-10: Image file does not exist</p>
<p>-11: The specified file is not available to support the image
file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Final image is converted to 256 color pictures to send, if given a
true color image, there may be color changes.</p>
<p>Image size will be stretched or compressed to fit the size of the
specified</p>
<p>window。</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_RS232_SendStatic

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendStatic(int nCardID, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nAlignment, int
x, int y, int cx, int cy)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send static text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>x: Start X of the play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y: Start Y of the play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cx: The width of play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>cy: The height of play window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Content outside the region remain unchanged</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendClock

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_RS232_SendClock( int nCardID, int nWinNo , int
nStayTime , int nCalendar , int nFormat , int nContent , int nFont , int
nRed , int nGreen , int nBlue , LPCSTR pTxt );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send clock to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStayTime: Stay time in second。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCalendar: Calendar 0: Gregorian calendar date and time</p>
<p>1: Lunar date and time</p>
<p>2: Chinese lunar solar terms</p>
<p>3: Lunar time and date + Solar Terms</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>nFormat: Format bit 0: when the system (0: 12 hour; 1: 24 hours
system) bit 1: Year digit (0: 4; 1: 2) bit 2: Branch (0: single; 1:
multi-line) bit 3~5: Format control, such as the November 12, 2010
Friday , according to diffenert values expressed as:</p>
<p>0: 2010/11/12 Friday 16:20:30</p>
<p>1: Fri，12/11/2010 16:20:30</p>
<p>2: 2010-11-12 Fri. 16:20:30</p>
<p>3: Friday，12 November 2010 16:20:30 4: Fri，Nov 12,2010 16:20:30</p>
<p>5: Friday，November 12 2010 16:20:30</p>
<p>6: Fri，11/12/2010 16:20:30 7: 2010/11/12，Fri.16:20:30 bit 6: show
hands,marks bit 7: Transparent</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nContent: Content</p>
<p>By bit to determine the content to display.</p>
<p>bit 7: Pointer bit 6: weeks bit 5: seconds bit 4: minute bit 3: hour
bit 2: day bit 1: month bit 0: year</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nFont: Font，Bit0~3: font size</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nRed: The red color component</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nGreen: The red green component</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBlue: The red blue component</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTxt: Text string to the end of 0x00.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_ExitSplitScreen

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_ExitSplitScreen( int nCardID );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Exit split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>其它说明</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SaveClearWndData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SaveClearWndData( int nCardID , int
nSavaOrClear );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Save or clear split window mesage</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSavaOrClear：Save or clear data 0: Save data to the flash.</p>
<p>1: Clear data from the flash.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_PlaySelectedPrg

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_PlaySelectedPrg(int nCardID, const WORD
*pSelected, int nSelCnt, int nOption)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_PlaySelectedPrg1

int CP5200_RS232_PlaySelectedPrg1(int nCardID, const WORD \*pSelected,
int nSelCnt, int

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">nOption, int nScrWidth , int nScrHeight , byte
byColorGray , byte nWndCnt)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrWidth：Screen width</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrHeight：Screen height</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byColorGray：color gray</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt：window count</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_SetUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Rs232_SetUserVarData(int nCardID, int bSave ,
int nVarNum , int bAstride , int* nWarLen , byte* byNoData );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bSave: Bit0:Whether to save all variables to the flash 0:No
save，1:Save。</p>
<p>Bit1~7: Reserved,set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarNum: Variable number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted;</p>
<p>1 is permit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：Bytes of data specified for each variable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byNoData：Specified number of variables and variable data for each
variable, the first byte of each variable is the variable number,
followed by a specified length of variable data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Corresponds to a variable number of each variable area size of each
variable region is 32 bytes. Multiple continuous variables can be linked
to a variable area used,occupied area of the variable number of
variables can not be used。</p>
<p>When does not allow cross-variable area, more than 32 bytes of data
are discarded；When allow cross-variable area,calculate the length of
the data area to use the number of variables.</p>
<p>Valid values for the variable number is 1~100。Number of variables
corresponding to each variable area can store 32 bytes of data, a number
of continuous variable area can be used together for a variable, the
variable area occupied number of variables can not be used。</p>
<p>When variable values are not updated and just save the variable value
to the FLASH, it can set the " nVarNum " of the value of 0, set the "
bSave " to save</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SetSelectedAndUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SetSelectedAndUserVarData(int nCardID,
int bSave , int nVarNum , int bAstride , int* nWarLen , byte* byNoData,
int nSelPrg )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set selected and user variable data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>bSave: Bit0:Whether to save all variables to the flash 0:No
save，1:Save。</p>
<p>Bit1~7: Reserved,set to 0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nVarNum: Variable number</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted;</p>
<p>1 is permit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nVarLen：Bytes of data specified for each variable.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byNoData：Specified number of variables and variable data for each
variable, the first byte of each variable is the variable number,
followed by a specified length of variable data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Corresponds to a variable number of each variable area size of each
variable region is 32 bytes. Multiple continuous variables can be linked
to a variable area used,occupied area of the variable number of
variables can not be used。</p>
<p>When does not allow cross-variable area, more than 32 bytes of data
are discarded；When allow cross-variable area,calculate the length of
the data area to use the number of variables.</p>
<p>Valid values for the variable number is 1~100。Number of variables
corresponding to each variable area can store 32 bytes of data, a number
of continuous variable area can be used together for a variable, the
variable area occupied number of variables can not be used。</p>
<p>When variable values are not updated and just save the variable value
to the FLASH, it can set the " nVarNum " of the value of 0, set the "
bSave " to save</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SetGlobalZone

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SetGlobalZone(int nCardID, byte
byConfig , byte bySynchro , byte byZoneNum , byte *byZoneMsg )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set global display zoneControl the internal timer</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig: Bit0: save the setting to FLASH or not 0 not to save，1
save。</p>
<p>Bit1~7: Reserved, set value 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>bySynchro: Synchronous display. 0 not synchronous, 1 synchronous.</p>
<p>Bit1~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byZoneNum: Zone count to be set. Normal 1~8, 0 clear all zones.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pZoneMsg: Zone definition data. 16 bytes for each zone. See the
following table for detail.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_PushUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 73%" />
<col style="width: 4%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>int CP5200_RS232_PushUserVarData(int nCardID, byte byOption
byVarZoonNum , byte byVarDataLen , byte* pVarNoAndData )</p>
</blockquote></th>
<th>,</th>
<th>byte</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Description</p>
</blockquote></td>
<td><blockquote>
<p>Push user variable data</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Parameter</p>
</blockquote></td>
<td><blockquote>
<p>nCardID: Control Card ID</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td colspan="3"><blockquote>
<p>byOption:</p>
<p>Bit0:Whether to save all the variable to the FLASH</p>
<p>0:Not Save 1:Save</p>
<p>Bit1: Push direction. 0:push back 1:push forward Bit2~3: Reserved,
set to 0.</p>
<p>Bit4~7: Push count. +1 is the push of zoon number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>byVarZoonNum: Zoon number.</p>
<p>Bit0~6:the zoon numbe which to be pushed:1~100</p>
<p>Bit7: Reserved, please set 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>byVarDataLen: Variable data length.Sort every variable byte data in
alphabet order.The total length of variable number and data is
(1+n)byte.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"><blockquote>
<p>pVarNoAndData: Variable No and data. The first byte is variable No,
followed by a specify length data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td colspan="3"><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td colspan="3"></td>
</tr>
</tbody>
</table>

> CP5200_RS232_TimerCtrl

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_TimerCtrl(int nCardID, byte byTimerNo ,
byte byCmd , byte byProp , DWORD dwValue );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set timer control</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>byTimerNo: Timer no,set the Timer by byte,1 is activity Bit0: Timer
1.</p>
<p>Bit1: Timer 2</p>
<p>Bit3: Timer 3</p>
<p>Bit4: Timer 4</p>
<p>Bit5: Timer 5</p>
<p>Bit6: Timer 6.</p>
<p>Bit7: Timer 7.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>byCmd: Action。 1： Initializtion Timer</p>
<p>2： Reset Timer</p>
<p>3： Start Timer 4： Puse Timer</p>
<p>Other：Reserved</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>byProp: Property. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>Bit0: 0 Time, 1 count down</p>
<p>Bit1: 0 pause, 1 start immediately</p>
<p>Bit2~3: Reserved</p>
<p>Bit4~7: time count</p>
<p>Set to 0 when the action is other.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dwValue: Value. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>The initialization value when count down, in seconds.</p>
<p>High byte previous.</p>
<p>Set to 0 when timing.</p>
<p>Set to 0 when the action is other.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

The description of all Actions and the correspondence property and value

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 35%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Action</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
<th><blockquote>
<p>Property</p>
</blockquote></th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Initialize</p>
<p>Timer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Bit0: 0 count up, 1 Count down</p>
<p>Bit1: 0 Pause, 1 start immediately</p>
<p>Bit2~3: reserved</p>
<p>Bit4~7: step distance</p>
</blockquote></td>
<td><blockquote>
<p>High byte previous.</p>
<p>The initialization value of countdown, measure time by millisecond.
The value reserved when time, set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reset Timer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Bit0: 0 Use old value，1 Use new value</p>
<p>Bit1: 0 Pause，1 start immediately Bit2~3: reserved</p>
</blockquote></td>
<td><blockquote>
<p>High byte previous. Countdown timer: Use as a new initialization
value when the property is set to use new value. Ignore when the
property is set to use the old value. Count up timer: reserved, set to
0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Start Timer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pause Timer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Save the timer setting to flash</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
<td><blockquote>
<p>reserved, set to 0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SetZoneAndVariable

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SetZoneAndVariable(int nCardID, const
BYTE* pZoneData, int nZoneLen, const BYTE* pVariableData, int nVarLen,
WORD wCtrl, WORD wReserved)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set global zone and user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pZoneData：The global zone data. Including the zone Options, the
number of zone, zone number, the zone defined.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nZoneLen：The global zone data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>pVariableData：Variable data, including variable options, variable
data and</p>
<p>cross-district allows ,the length of the variable data table, the
variable number and data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：The variable data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wCtrl：Effective control parameters play times, high byte first.</p>
<p>The value of 0 has been effective .</p>
<p>Bit15: Resvered, fill 0.</p>
<p>Bit0~14: Display times.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>wReserved：resvered</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>After use this conmand, the global zone to be automatic into
synchronous display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendPureText

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SendPureText(int nCardID, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int
nEffect, int nStayTime, int nAlignment)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send pure text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendMultiProtocol

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendMultiProtocol(int nCardID, int nItem,
const BYTE *pText, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send multi protocol data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nItem: Items of multi protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Datas of multi protocol，see<u>《 C-Power external calls
communication</u> <u>protocol》send multi protocol data CC=0x60 Data
item</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength:Length of datas</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

10.3、Overview of network multi-window control API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 41%" />
<col style="width: 1%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No</p>
</blockquote></th>
<th><blockquote>
<p>API function name</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SplitScreen</p>
</blockquote></td>
<td><blockquote>
<p>Send split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SendText</p>
<p>CP5200_Net_SendText1</p>
</blockquote></td>
<td><blockquote>
<p>Send text to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SendTagText</p>
<p>CP5200_Net_SendTagText1</p>
</blockquote></td>
<td><blockquote>
<p>Send tag text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SendPicture</p>
</blockquote></td>
<td><blockquote>
<p>Send picture to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SendStatic</p>
</blockquote></td>
<td><blockquote>
<p>Send static text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SendClock</p>
</blockquote></td>
<td><blockquote>
<p>Send clock to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_ExitSplitScreen</p>
</blockquote></td>
<td><blockquote>
<p>Exit split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SaveClearWndData</p>
</blockquote></td>
<td><blockquote>
<p>Save or clear split window mesage</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_PlaySelectedPrg</p>
<p>CP5200_Net_PlaySelectedPrg1</p>
</blockquote></td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SetUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Set user variable</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SetSelectedAndUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Set selected and user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_SetGlobalZone</p>
</blockquote></td>
<td><blockquote>
<p>Set global message</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_PushUserVarData</p>
</blockquote></td>
<td><blockquote>
<p>Push and use variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP5200_Net_TimerCtrl</p>
</blockquote></td>
<td><blockquote>
<p>Set timer control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td colspan="2">CP5200_RS232_SetZoneAndVariable</td>
<td><blockquote>
<p>Set global zone and user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td colspan="2">CP5200_RS232_SendPureText</td>
<td><blockquote>
<p>Send pure text to special window</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize network parameters
>
> Only record the network parameter initialization parameter
> information, not the actual network operation。
>
> Step 2: Send split window command，
>
> If the window has been divided and have been met requirements, this
> step can be dispensed with, or to send the split window command。 Step
> 3: Send text or picture to window。

Note: This category interface need not to consider whether the network
has been connected , as long as the network parameters have been
initialized.。

10.4 、 Detail of network multi-window control API function

> CP5200_Net_SplitScreen

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SplitScreen(int nCardID, int nScrWidth,
int nScrHeight, int nWndCnt, const int *pWndRects)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrWidth: the width of screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrHeight: the height of screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt: The window number of the screen will be splitted , valid
values 1~8。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndRects: Window coordinates, each window with four integer said
the</p>
<p>"left, up,right,down” coordinates,ave the same data structure with
the</p>
<p>"RECT"of windows。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: The window number was too much</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>This function sets sub-windows information and sends split-screen
commad.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendText (CP5200_Net_SendText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendText(int nCardID, int nWndNo, const
char *pText, COLORREF crColor, int nFontSize, int nSpeed, int nEffect,
int nStayTime, int nAlignment);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text will to be sent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>CP5200_Net_SendText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendTagText (CP5200_Net_SendTagText1)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendTagText(int nCardID, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize,b int nSpeed, int
nEffect, int nStayTime, int nAlignment)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send tag text to specify window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text which to be sent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u>，this parameter only support the font size, does not support
multiple font</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment 1: center Alignment 2: right Alignment:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>CP5200_Net_SendTagText1 is for single byte characters, ASCII and
extended ASCII.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_Net_SendPicture

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendPicture(int nCardID, int nWndNo, int
nPosX, int nPosY, int nCx, int nCy, const char *pPictureFile, int
nSpeed, int nEffect, int nStayTime, int nPictRef)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send picture to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nCx: The width of picture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCy: The heigth of picture</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>pPictureFile: Path and file name of the picture file ,this is based
on the value of nPictRef.</p>
<p>When the value of nPictRef is 0: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 1: pPictureFile is the Path and file
name of the GIF file on the controller card.</p>
<p>When the value of nPictRef is 2: pPictureFile is the Path and file
name of the file on the computer.</p>
<p>When the value of nPictRef is 3: pPictureFile is the Path and file
name of picture packages and the serial number of the picture on the
controller card.</p>
<p>Packages name followed by is separated by a space. For example:</p>
<p>“images.rpk 1”</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPictRef: the way to send picture and meaning.</p>
<p>0：display the local picture that will be converted into the format
of GIF to send.</p>
<p>1：display the gif picture that on the controller card.</p>
<p>2：display the local picture that will be converted into the format
of simple to send.</p>
<p>3：display the picture in the picture packages that on the controller
card.</p>
<p>Other values: deal with 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: Param “nWndNo” is wrong</p>
<p>-10: Image file does not exist</p>
<p>-11: The specified file is not available to support the image
file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Final image is converted to 256 color pictures to send, if given a
true color image, there may be color changes.</p>
<p>Image size will be stretched or compressed to fit the size of the
specified</p>
<p>window。</p>
</blockquote></td>
</tr>
</tbody>
</table>

CP5200_Net_SendSimpleImageData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendSimpleImageData(int nCardID, int
nWndNo, int nPosX, int nPosY, const char *pPictureFile, int nSpeed, int
nEffect, int nStayTime, BYTE* pPicData , long lPicDataLen)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send simple picture to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPosX: Began to show the location of X coordinate. Relative
upper-left corner the window.。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPosY: Began to show the location of Y coordinate. Relative
upper-left corner the window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPicData: simple picture data,see <u>1.11 simple picture data
fomart.</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>lPicDataLen:the length of simple picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
<p>-9: Param “nWndNo” is wrong</p>
<p>-10: Image file does not exist</p>
<p>-11: The specified file is not available to support the image
file</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>Final image is converted to 256 color pictures to send, if given a
true color image, there may be color changes.</p>
<p>Image size will be stretched or compressed to fit the size of the
specified</p>
<p>window。</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendStatic

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendStatic(int nCardID, int nWndNo, const
char *pText, COLORREF crColor, int nFontSize, int nAlignment, int x, int
y, int cx, int cy)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send static text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>x: Start X of the play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y: Start Y of the play window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cx: The width of play window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>cy: The height of play window.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Content outside the region remain unchanged</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendClock

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_Net_SendClock( int nCardID, int nWinNo , int
nStayTime , int nCalendar , int nFormat , int nContent , int nFont , int
nRed , int nGreen , int nBlue , LPCSTR pTxt );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send clock to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nStayTime: Stay time in second。</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nCalendar: Calendar 0: Gregorian calendar date and time</p>
<p>1: Lunar date and time</p>
<p>2: Chinese lunar solar terms</p>
<p>3: Lunar time and date + Solar Terms</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>nFormat: Format bit 0: when the system (0: 12 hour; 1: 24 hours
system) bit 1: Year digit (0: 4; 1: 2) bit 2: Branch (0: single; 1:
multi-line) bit 3~5: Format control, such as the November 12, 2010
Friday , according to diffenert values expressed as:</p>
<p>0: 2010/11/12 Friday 16:20:30</p>
<p>1: Fri，12/11/2010 16:20:30</p>
<p>2: 2010-11-12 Fri. 16:20:30</p>
<p>3: Friday，12 November 2010 16:20:30 4: Fri，Nov 12,2010 16:20:30</p>
<p>5: Friday，November 12 2010 16:20:30</p>
<p>6: Fri，11/12/2010 16:20:30 7: 2010/11/12，Fri.16:20:30 bit 6: show
hands,marks bit 7: Transparent</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nContent: Content</p>
<p>By bit to determine the content to display.</p>
<p>bit 7: Pointer bit 6: weeks bit 5: seconds bit 4: minute bit 3: hour
bit 2: day bit 1: month bit 0: year</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>nFont: Font，Bit0~3: font size</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>nRed: The red color component</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nGreen: The red green component</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBlue: The red blue component</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTxt: Text string to the end of 0x00.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_ExitSplitScreen

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_ExitSplitScreen( int nCardID );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Exit split window command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>其它说明</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SaveClearWndData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SaveClearWndData( int nCardID , int
nSavaOrClear );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Save or clear split window mesage</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSavaOrClear：Save or clear data 0: Save data to the flash.</p>
<p>1: Clear data from the flash.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_PlaySelectedPrg

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_PlaySelectedPrg(int nCardID, const WORD
*pSelected, int nSelCnt, int nOption)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_PlaySelectedPrg1

int CP5200_Net_PlaySelectedPrg1(int nCardID, const WORD \*pSelected, int
nSelCnt, int

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">nOption, int nScrWidth , int nScrHeight , byte
byColorGray , byte nWndCnt)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Select play stored program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSelected：The program number array of be selected to play</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSelCnt：The program count of be selected</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nOption：Whether to save select message to the flash</p>
<p>0：No save</p>
<p>1：Save</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nScrWidth：Screen width</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nScrHeight：Screen height</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byColorGray：color gray</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndCnt：window count</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Net_SetUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SetUserVarData(int nCardID, int bSave ,
int nVarNum , int bAstride , int* nWarLen , byte* byNoData );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bSave: Bit0:Whether to save all variables to the flash 0:No
save，1:Save。</p>
<p>Bit1~7: Reserved,set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarNum: Variable number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted;</p>
<p>1 is permit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：Bytes of data specified for each variable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byNoData：Specified number of variables and variable data for each
variable, the first byte of each variable is the variable number,
followed by a specified length of variable data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Corresponds to a variable number of each variable area size of each
variable region is 32 bytes. Multiple continuous variables can be linked
to a variable area used,occupied area of the variable number of
variables can not be used。</p>
<p>When does not allow cross-variable area, more than 32 bytes of data
are discarded；When allow cross-variable area,calculate the length of
the data area to use the number of variables.</p>
<p>Valid values for the variable number is 1~100。Number of variables
corresponding to each variable area can store 32 bytes of data, a number
of continuous variable area can be used together for a variable, the
variable area occupied number of variables can not be used。</p>
<p>When variable values are not updated and just save the variable value
to the FLASH, it can set the " nVarNum " of the value of 0, set the "
bSave " to save</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SetSelectedAndUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SetSelectedAndUserVarData(int nCardID,
int bSave , int nVarNum , int bAstride , int* nWarLen , byte* byNoData,
int nSelPrg )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set selected and user variable data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>bSave: Bit0:Whether to save all variables to the flash 0:No
save，1:Save。</p>
<p>Bit1~7: Reserved,set to 0</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>nVarNum: Variable number</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>bAstride: Whether to allow cross-variable zone setting. 0 is not
permitted;</p>
<p>1 is permit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nVarLen：Bytes of data specified for each variable.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byNoData：Specified number of variables and variable data for each
variable, the first byte of each variable is the variable number,
followed by a specified length of variable data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td><blockquote>
<p>Corresponds to a variable number of each variable area size of each
variable region is 32 bytes. Multiple continuous variables can be linked
to a variable area used,occupied area of the variable number of
variables can not be used。</p>
<p>When does not allow cross-variable area, more than 32 bytes of data
are discarded；When allow cross-variable area,calculate the length of
the data area to use the number of variables.</p>
<p>Valid values for the variable number is 1~100。Number of variables
corresponding to each variable area can store 32 bytes of data, a number
of continuous variable area can be used together for a variable, the
variable area occupied number of variables can not be used。</p>
<p>When variable values are not updated and just save the variable value
to the FLASH, it can set the " nVarNum " of the value of 0, set the "
bSave " to save</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_SetGlobalZone

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SetGlobalZone(int nCardID, byte byConfig
, byte bySynchro , byte byZoneNum , byte *byZoneMsg )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set global display message</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: contrl card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig:</p>
<p>Bit0: Whether to save to FLASH</p>
<p>0:Not save, 1:Save</p>
<p>Bit1~7:Reserved, set to 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>bySynchro: Synchronization。</p>
<p>Bit0: Whether to synchronization, 0 Not synchronous，1
synchronous。</p>
<p>Bit1~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byZoneNum: Zone number.The golobal display zone number which to be
set.Cancel all the zone when zone number is 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byZoneMsg: zone message.The specify message of global display
zone.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_PushUserVarData

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_PushUserVarData(int nCardID, byte
byOption , byte byVarZoonNum , byte byVarDataLen , byte* pVarNoAndData
)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Push user variable data</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Control Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>byOption:</p>
<p>Bit0:Whether to save all the variable to the FLASH</p>
<p>0:Not Save 1:Save</p>
<p>Bit1: Push direction. 0:push back 1:push forward Bit2~3: Reserved,
set to 0.</p>
<p>Bit4~7: Push count. +1 is the push of zoon number.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byVarZoonNum: Zoon number.</p>
<p>Bit0~6:the zoon numbe which to be pushed:1~100</p>
<p>Bit7: Reserved, please set 0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byVarDataLen: Variable data length.Sort every variable byte data in
alphabet order.The total length of variable number and data is
(1+n)byte.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>pVarNoAndData: Variable No and data. The first byte is variable No,
followed by a specify length data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_TimerCtrl

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Net_TimerCtrl(int nCardID, byte byTimerNo
, byte byCmd , byte byProp ,</p>
<p>DWORD dwValue);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set timer control</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th><blockquote>
<p>byTimerNo: Timer no,set the Timer by byte,1 is activity Bit0: Timer
1.</p>
<p>Bit1: Timer 2</p>
<p>Bit3: Timer 3</p>
<p>Bit4: Timer 4</p>
<p>Bit5: Timer 5</p>
<p>Bit6: Timer 6.</p>
<p>Bit7: Timer 7.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>byCmd: Action。 1： Initializtion Timer</p>
<p>2： Reset Timer</p>
<p>3： Start Timer 4： Puse Timer</p>
<p>Other：Reserved</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>byProp: Property. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>Bit0: 0 Time, 1 count down</p>
<p>Bit1: 0 pause, 1 start immediately</p>
<p>Bit2~3: Reserved</p>
<p>Bit4~7: time count</p>
<p>Set to 0 when the action is other.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dwValue: Value. Have different meaning according to the action.</p>
<p>When the action is initialize the time:</p>
<p>The initialization value when count down, in seconds.</p>
<p>High byte previous.</p>
<p>Set to 0 when timing.</p>
<p>Set to 0 when the action is other.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SetZoneAndVariable

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Net_SetZoneAndVariable(int nCardID, const
BYTE* pZoneData, int nZoneLen, const</p>
<p>BYTE* pVariableData, int nVarLen, WORD wCtrl, WORD
wReserved)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set global zone and user variable</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pZoneData：The global zone data. Including the zone Options, the
number of zone, zone number, the zone defined.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nZoneLen：The global zone data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pVariableData：Variable data, including variable options, variable
data and</p>
<p>cross-district allows ,the length of the variable data table, the
variable number and data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nVarLen：The variable data length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wCtrl：Effective control parameters play times, high byte first.</p>
<p>The value of 0 has been effective .</p>
<p>Bit15: Resvered, fill 0.</p>
<p>Bit0~14: Display times.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wReserved：resvered</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>After use this conmand, the global zone to be automatic into
synchronous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>display.</td>
</tr>
</tbody>
</table>

> CP5200_Net_SendPureText

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendPureText(int nCardID, int nWndNo,
const char *pText, COLORREF crColor, int nFontSize, int nSpeed, int
nEffect, int nStayTime, int nAlignment)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send pure text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nWndNo: Window sequence number, valid values 0 to 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text to be send</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>crColor: Text color</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Effect speed</p>
<p>0～100：The fastest value of 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Show effect。See the "1.5" section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nStayTime: Stay time in second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nAlignment: The level of alignment</p>
<p>0: left Alignment</p>
<p>1: center Alignment</p>
<p>2: right Alignment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendMultiProtocol

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SendMultiProtocol(int nCardID, int nItem,
const BYTE *pText, int nLength)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send multi protocol data</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nItem: Items of multi protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Datas of multi protocol，see<u>《 C-Power external calls
communication</u> <u>protocol》send multi protocol data CC=0x60 Data
item</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLength:Length of datas</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# Program template API function  {#program-template-api-function}

11.1 、 Overview of RS232 program template API

function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 52%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th><blockquote>
<p>Function name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>CPowerBox_RS232_SetProgramTemplate</p>
<p>CPowerBox_RS232_SetProgramTemplate1</p>
</blockquote></td>
<td><blockquote>
<p>Set program template command</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>CPowerBox_RS232_InOutProgramTemplate</p>
</blockquote></td>
<td><blockquote>
<p>In or out program template command</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>CPowerBox_RS232_QueryProgramTemplate</p>
</blockquote></td>
<td><blockquote>
<p>Query program template command</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>CPowerBox_RS232_QueryProgramTemplate1</td>
<td></td>
</tr>
<tr class="odd">
<td>4</td>
<td>CPowerBox_RS232_DeleteProgram</td>
<td>Delete program command</td>
</tr>
<tr class="even">
<td>5</td>
<td>CPowerBox_RS232_SendText</td>
<td>Send text to special window</td>
</tr>
<tr class="odd">
<td>6</td>
<td>CPowerBox_RS232_SendPicture</td>
<td>Send picture to special window</td>
</tr>
<tr class="even">
<td>7</td>
<td>CPowerBox_RS232_SendClockOrTemperature</td>
<td>Send clock and temperature to special window</td>
</tr>
<tr class="odd">
<td>8</td>
<td>CPowerBox_RS232_SetAloneProgram</td>
<td>Set alone program</td>
</tr>
<tr class="even">
<td>9</td>
<td>CPowerBox_RS232_QueryProgram</td>
<td>Query program information</td>
</tr>
<tr class="odd">
<td>10</td>
<td>CPowerBox_RS232_SetProgramProperty</td>
<td>Set program property</td>
</tr>
<tr class="even">
<td>11</td>
<td>CPowerBox_RS232_SetSchedule</td>
<td>Set play schedule</td>
</tr>
<tr class="odd">
<td>12</td>
<td>CPowerBox_RS232_DeleteSchedule</td>
<td>Delete play schedule</td>
</tr>
<tr class="even">
<td>13</td>
<td>CPowerBox_RS232_GetSchedule</td>
<td>Get play schedule</td>
</tr>
</tbody>
</table>

11.2、Detail of RS232 program template API function

> CPowerBox_RS232_SetProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SetProgramTemplate(int nCardID, byte
byColor ,USHORT nWidth , USHORT nHeight , byte nWndNum , byte
*byDefParam , byte* pWndParam)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_SetProgramTemplate1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SetProgramTemplate1(int nCardID,
BYTE byColor ,USHORT nWidth , USHORT nHeight , BYTE nWndNum , BYTE
byOption, BYTE* pDefParam , BYTE* pWndParam)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Forced into the program template run</p>
<p>Bit1: Save the template position. 0: user disk, 1: system disk.</p>
<p>If the template is saved to the system tray, the original template of
the user tray is cleared; if the template is saved to the user's disk,
the original template of the system disk is cleared。</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_InOutProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_InOutProgramTemplate( int
nCardID,byte byInOrOut )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set in or out program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>byInOrOut: In or Out</p>
<p>1: In program template style.</p>
<p>0: Out program template style.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_QueryProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_QueryProgramTemplate(int nCardID ,
byte* pState );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set query program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pState: template status, 1 is template mode and 0 is not template
mode</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CPowerBox_RS232_QueryProgramTemplate1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_QueryProgramTemplate1(int nCardID ,
byte byFlag , BYTE* pStateBuf , int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set query program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:</p>
<p>Bit0: Whether to query program template status parameter</p>
<p>Bit1:Whether to return the template definition color gray, screen
size information</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pStateBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

"pStateBuf" have the following meanings:：

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x83</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data of query program template
status parameter.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Options</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value of “Options”.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Template mode</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Not program template</p>
<p>1: program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Template status</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: template availability</p>
<p>0: the template is not available</p>
<p>1: the template can be used others: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Color gray</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Color and gray。</p>
<p>Same with define“set program template”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen width</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen height</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Window count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>Play window count。</p>
<blockquote>
<p>Supports up to 10 play windows</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_RS232_DeleteProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_DeleteProgram( int nCardID,byte
byConfig , byte byProNum , byte* pDelPro );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig: Bit0: The range of the delete program</p>
<p>0：Delete all the program</p>
<p>1：Delete the specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNum: Program number. Do not need this item when delete all the
program.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDelPro: The list of the program need to be delete.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_SendText

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SendText( int nCardID, DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byProp , byte
*byShowFormat , char* pText);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send text to the specify window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProp: Property，Bit0~3: Text type 0：Common Text</p>
<p>Bit4: Display format. 0: default format 1:specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byShowFormat: Show format. Do not need this item when the property’s
display format is 0.</p>
<p>Byte0~1: Stay time,High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text data, end with ‘0x00’</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_SendPicture

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SendPicture( int nCardID, DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byPicType , byte
*byShowFormat , byte* pPicData , long lPicDataLen);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send picture to the specify picture</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPicType: Picture type. Bit0~3: Picture type</p>
<p>1: Data of GIF picture file which include the information of the
picture’s width and height so on.</p>
<p>2: The stored GIF filename in the contrl card.</p>
<p>4. Simple picture data, Check the format information at ”Simple
Picture data format”</p>
<p>Bit4: Show format. 0 default format,1 specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byShowFormat: Show format.</p>
<p>Do not need this item when the property’s display format is 0.</p>
<p>Byte0~1: Stay time, High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Show effect See”Show effect code”</p>
<p>Byte4: Picture style(zoom、tile), see “Picture style code”</p>
<p>Byte5: Reserved</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pPicData: Picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>lPicDataLen:Picture data length.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_SendClockOrTemperature

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CPowerBox_RS232_SendClockOrTemperature( int
nCardID,DWORD dwAppendCode , BYTE byProNo , BYTE byWndNo , BYTE
byProgramType , UINT nPropLen , BYTE* pProgramProp ,byte* pBuf , int
nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send clock and temperature to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramType: Program type Bit0~3: Type</p>
<p>2：Clock ; 3：Temperature Bit4: Display format.</p>
<p>0: default format 1:specify format</p>
<p>Bit5~7: Reserved, fill in 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPropLen: Property length</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pProgramProp：Program property</p>
<p>The meaning of the attribute data according to different types</p>
<p>Type = 2 , see <u>Clock/Calendar type</u> proprtey</p>
<p>Type = 3 , see <u>Temperature and Humidity type</u> proprtey</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x87</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to show
clock/temperature in the specified window of the specified program</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Program No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>The same value with send value “Program no”.</p>
<blockquote>
<p>Valid value:1~100</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Window No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value “Window no”. Valid value:1~10,Invalid
when out of program template definition.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Packet loss number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The number of packets that have not yet received. Sends the first
packet loss number is the total number of packets minus one.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>The packet number of the packet loss</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Packet loss packet number. Always in accordance with small to large;
the first packet packet number is 0. Each package a byte.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_RS232_SetAloneProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_RS232_SetAloneProgram(int nCardID,DWORD
dwAppendCode , BYTE byProgramNo ,</p>
<p>BYTE byWindowCnt ,BYTE* pWndParam, BYTE* pWndData)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set alone program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWindowCnt: Window count. Valid value:1～10</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>pWndParam：windows parameter</p>
<p>Every window information table has a 22 bytes length parameter. The
1~16 bytes are window position and property, You can see the detail at
<u>1.13.</u> <u>Window position and property</u>; The 17~19 bytes are
window data offset; The 20~22 bytes are window data length. High byte
first.</p>
<p>If no data ,then window data offset and window data length all are
0.</p>
<p>The total length of the data is: the number of the window*22.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndData：Window play data:“Text”、“Picture”…</p>
<p>Byte 1：Data Type(1 Text；4 Picture)</p>
<p>Byte 2：Data Format（Like “Text type” in command 0x85 and “Picture
type” in command 0x86）</p>
<p>Byte 3：Text data or picture data。</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_QueryProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Int CPowerBox_RS232_QueryProgram( int nCardID ,byte
byFlag , byte* pParam , BYTE* pBuf , int nBufSize );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Query program information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID:Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:Special which program info will to be query 1: Query valid
programs count and program number 2: Query specifies program
information.</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>pParam:</p>
<p>If “byFlag” is 1：byte1~5，resvered，fill 0</p>
<p>If “byFlag” is 2：：byte1，program number；byte2~5，resvered，fill
0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings：

 Query"valid program count and program number"

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Valid program number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Each byte identifies an effective program。</p>
<p>Valid value 1～100。</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag

 Query specifies program information

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Now only return one information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>count</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Program number</td>
<td></td>
<td>1</td>
<td><blockquote>
<p>Program number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>User append</p>
<p>code</p></td>
<td></td>
<td>4</td>
<td><blockquote>
<p>User append code</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag
>
> 0x11 Invalid programs
>
> 0x12 Can't get program information
>
> CPowerBox_RS232_SetProgramProperty

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SetProgramProperty( int nCardID,
byte byOption , byte byProgramCnt , byte* pPrograms , byte byPropertyID1
, byte byPropertyID2 , byte byProgramLevel , USHORT nLoopCnt , USHORT
nTime , byte* pDuetime , byte* pTimeInterval);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program property</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: The control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Set the range of the program property</p>
<p>0: All programes</p>
<p>1: Specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramCnt:The count of the program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPrograms: The list of the programes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ByPropertyID1：Property ID 1, marked which property you want to set
by</p>
<p>byte, set 0 if the data not exist.</p>
<p>Bit0: The level of the program.</p>
<p>Bit1: The cycle count.</p>
<p>Bit2: Valid time. How long will the program be valid from now on.</p>
<p>Bit3: Interval time</p>
<p>Bit4~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>ByPropertyID2: Property ID 2。Bit0~4: valid time. &gt;0 the count of
the valid time.&lt;=4</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramLevel: The program level. 1～3 level, The high level of the
program is priority.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLoopCnt: Loop count, High byte previous(big-endian).</p>
<p>0: Do not play the program, use to shield program temporarily.</p>
<p>1~255: The loop count of the program.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>nTime: Valid time. High byte previous (big-endian). In minute.</p>
<p>0: Not limit play time</p>
<p>&gt;0: Specify play time in minute.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDuetime: time limit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTimeInterval:The interval time. The start tag
“Hour/Minute/Second”and the end tag “Hour/Minute/Second” both represent
by one byte.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_SetSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_SetSchedule(int nCardID, DWORD
dwAppendCode, BYTE byScheduleNo, const BYTE* pProperty, const BYTE*
pBoxes, BYTE byBoxCnt)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>byScheduleNo: Schedule number，Valid value 1~100。Total support 100
plans, For each plan No, the new data cover the old data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pProperty: play property，total 14 bytes： byte 0：Format and level：
Bit0~3: Data format，fill in 0x01</p>
<p>Bit4~7: Indicates the priority level. The priority level the greater
the value, the more priority to play, 0 is the lowest priority.。。</p>
<p>byte 1：Weekday：Bit0~6: 7-bit logo Sunday to Saturday byte 2~4：
Begin date ， 3 bytes: Byte1:Year,Valid value0~99,means</p>
<p>2000~2999; Byte2:Month ;Byte3:Day</p>
<p>byte 5~7：End date，3 bytes: Byte1:Year,Valid value0~99,means
2000~2999;</p>
<p>Byte2:Month ;Byte3:Day</p>
<p>byte 8~10：Begin time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second
byte 11~13：End time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBoxes: program number , each byte represents a program. Numbered
in</p>
<p>ascending order, do not repeat.....</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>byBoxCnt:program number count, Valid value:1～100,</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_DeleteSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_RS232_DeleteSchedule(int nCardID, DWORD
dwAppendCode, const BYTE* pSchs,</p>
<p>BYTE bySchCnt)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pSchs: schedule number, Valid value 1~100。Each byte represents a
play schedule。</p>
<p>When delete all play schedule, the length of this data is one , value
is 0xff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bySchCnt: The number of play schedule will to be delete。0 means
delete all play plans.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_RS232_GetSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_RS232_GetSchedule(int nCardID, DWORD
dwAppendCode, BYTE byType, BYTE byScheduleNo , byte* pBuf , int nBufSize
)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byType：0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byScheduleNo: Valid value:1~100。When query type is 0，this data fill
in 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-2: The command data package error</p>
<p>-3: Can not open serial port</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th>Lenght(byte)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x8d</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to query play plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td>4</td>
<td>The user’s append code, high byte previous.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Query type</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Count /Number</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><p>When query type is 0，this value is valid play schedule count</p>
<blockquote>
<p>When query type is 1，this value is play schedule number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Play schedule number table/ play schedule content</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>When query type is 0，this value is valid play schedule number
table</p>
<p>When query type is 1，this value is play schedule content. Data
format like command</p>
<p>0x8B.</p>
</blockquote></td>
</tr>
</tbody>
</table>

You must deal with the return data according to the different query
type.

The meaning of \"return value\" in the return packet:

> 0x01 program template is invalid 0x11 Don't support the query type.
>
> 0x12 Invalid play plan no.
>
> 0x80 currently is not program template way

11.3 、 Overview of Network program template API

function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 48%" />
<col style="width: 3%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No.</p>
</blockquote></th>
<th>Function name</th>
<th colspan="2"><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_SetProgramTemplate</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Set program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_InOutProgramTemplate</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Set in or out program template</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_QueryProgramTemplate</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Query program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_DeleteProgram</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Delete program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_SendText</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Send text to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>CPowerBox_Net_SendPicture</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Send picture to special window</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_SendClockOrTemperature</td>
<td><blockquote>
<p>Send clock and temperature to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_SetAloneProgram</td>
<td><blockquote>
<p>Set alone program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_QueryProgram</td>
<td><blockquote>
<p>Query program information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_SetProgramProperty</td>
<td><blockquote>
<p>Set program property</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_SetSchedule</td>
<td><blockquote>
<p>Set play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_DeleteSchedule</td>
<td><blockquote>
<p>Delete play schedule</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td colspan="2">CPowerBox_Net_GetSchedule</td>
<td><blockquote>
<p>Get play schedule</p>
</blockquote></td>
</tr>
</tbody>
</table>

11.4、Detail of Network program template API function

> CPowerBox_Net_SetProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_SetProgramTemplate(int nCardID, byte
byColor ,USHORT nWidth , USHORT nHeight , byte nWndNum , byte
*byDefParam , byte* pWndParam)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_SetProgramTemplate1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_SetProgramTemplate1(int nCardID, BYTE
byColor ,USHORT nWidth , USHORT nHeight , BYTE nWndNum , BYTE byOption,
BYTE* pDefParam , BYTE* pWndParam)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColor: Bit0: Red mark</p>
<p>Bit1: Green mark</p>
<p>Bit2: Blue mark</p>
<p>Bit3: Reserved</p>
<p>Bit4～6: Gray level</p>
<p>0: 2 level gray，7: 256 level gray</p>
<p>Bit7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWidth: The width of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nHeight: The height of the screen，high byte previous</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nWndNum: The display window number,the maximum number is 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Forced into the program template run</p>
<p>Bit1: Save the template position. 0: user disk, 1: system disk.</p>
<p>If the template is saved to the system tray, the original template of
the user tray is cleared; if the template is saved to the user's disk,
the original template of the system disk is cleared。</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>byDefParam: Default parameter。</p>
<p>Byte0~1: Stay time in second. High byte previous.</p>
<p>Byte2: Speed。The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Picture type. See”Picture type code”</p>
<p>Byte7: Clock Format. See “Clock format and content”</p>
<p>Byte8: Clock content. See “Clock format and content”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndParam: Window parameter. Each window has a 16 bytes length
parameter. The total length of the data is: the number of the window*16.
You can see the detail at “appendix:1 window position and property”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_InOutProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_InOutProgramTemplate( int nCardID,byte
byInOrOut )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set in or out program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>byInOrOut: In or Out</p>
<p>1: In program template style.</p>
<p>0: Out program template style.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_QueryProgramTemplate

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_QueryProgramTemplate(int nCardID ,
byte* pState );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set query program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pState: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CPowerBox_Net_QueryProgramTemplate1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_QueryProgramTemplate1(int nCardID ,
byte byFlag , BYTE* pStateBuf , int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set query program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:</p>
<p>Bit0: Whether to query program template status parameter</p>
<p>Bit1:Whether to return the template definition color gray, screen
size information</p>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pStateBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize: The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

"pStateBuf" have the following meanings:：

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x83</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data of query program template
status parameter.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Options</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value of “Options”.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Template mode</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Not program template</p>
<p>1: program template</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Template status</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Bit0~1: template availability</p>
<p>0: the template is not available</p>
<p>1: the template can be used others: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Bit2~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Color gray</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Color and gray。</p>
<p>Same with define“set program template”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen width</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen height</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>High byte first</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Window count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>Play window count。</p>
<blockquote>
<p>Supports up to 10 play windows</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_DeleteProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_DeleteProgram( int nCardID,byte
byConfig , byte byProNum , byte* pDelPro );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byConfig: Bit0: The range of the delete program</p>
<p>0：Delete all the program</p>
<p>1：Delete the specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNum: Program number. Do not need this item when delete all the
program.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDelPro: The list of the program need to be delete.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_SendText

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_SendText( int nCardID, DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byProp , byte
*byShowFormat, char* pText);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send text to the specify window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>nCardID: Card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProp: Property，Bit0~3: Text type 0：Common Text</p>
<p>Bit4: Display format. 0: default format 1:specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byShowFormat: Show format. Do not need this item when the property’s
display format is 0.</p>
<p>Byte0~1: Stay time,High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Font size. See “Font size code”</p>
<p>Byte4: Font color. See “Font color code”</p>
<p>Byte5: Show effect See”Show effect code”</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: Text data, end with ‘0x00’</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_SendPicture

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_SendPicture( int nCardID, DWORD
dwAppendCode , byte byProNo , byte byWndNo , byte byPicType , byte
*byShowFormat , byte* pPicData , long lPicDataLen);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send picture to the specify window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="8">Parameter</td>
<td><blockquote>
<p>nCardID: Control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPicType: Picture type. Bit0~3: Picture type</p>
<p>1: Data of GIF picture file which include the information of the
picture’s width and height so on.</p>
<p>2: The stored GIF filename in the contrl card.</p>
<p>4. Simple picture data, Check the format information at ”Simple
Picture data format”</p>
<p>Bit4: Show format. 0 default format,1 specify format</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byShowFormat: Show format.</p>
<p>Do not need this item when the property’s display format is 0.</p>
<p>Byte0~1: Stay time, High byte previous.</p>
<p>Byte2: Speed. The smaller the faster.</p>
<p>Byte3: Show effect See”Show effect code”</p>
<p>Byte4: Picture style(zoom、tile), see “Picture style code”</p>
<p>Byte5: Reserved</p>
<p>Byte6: Reserved</p>
<p>Byte7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pPicData: Picture data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>lPicDataLen:Picture data length.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CPowerBox_Net_SendClockOrTemperature

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CPowerBox_Net_SendClockOrTemperature( int nCardID,DWORD
dwAppendCode , BYTE byProNo , BYTE byWndNo , BYTE byProgramType , UINT
nPropLen , BYTE* pProgramProp ,byte* pBuf , int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send clock and temperature to special window</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="9">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWndNo: Window No. Valid value:1～10 , Invalid when out of program
template definition.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramType: Program type Bit0~3: Type</p>
<p>2：Clock ; 3：Temperature Bit4: Display format.</p>
<p>0: default format 1:specify format</p>
<p>Bit5~7: Reserved, fill in 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPropLen: Property length</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pProgramProp：Program property</p>
<p>The meaning of the attribute data according to different types</p>
<p>Type = 2 , see <u>Clock/Calendar type</u> proprtey</p>
<p>Type = 3 , see <u>Temperature and Humidity type</u> proprtey</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x87</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to show
clock/temperature in the specified window of the specified program</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>The user’s append code, high byte previous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Program No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><p>The same value with send value “Program no”.</p>
<blockquote>
<p>Valid value:1~100</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Window No</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The same value with send value “Window no”. Valid value:1~10,Invalid
when out of program template definition.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Packet loss number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>The number of packets that have not yet received. Sends the first
packet loss number is the total number of packets minus one.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>The packet number of the packet loss</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Packet loss packet number. Always in accordance with small to large;
the first packet packet number is 0. Each package a byte.</p>
</blockquote></td>
</tr>
</tbody>
</table>

CPowerBox_Net_SetAloneProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_Net_SetAloneProgram(int nCardID,DWORD
dwAppendCode , BYTE byProgramNo ,</p>
<p>BYTE byWindowCnt ,BYTE* pWndParam, BYTE* pWndData)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set alone program</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProNo: Program No.,Valid value:1~255</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byWindowCnt: Window count. Valid value:1～10</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>pWndParam：windows parameter</p>
<p>Every window information table has a 22 bytes length parameter. The
1~16 bytes are window position and property, You can see the detail at
<u>1.13.</u> <u>Window position and property</u>; The 17~19 bytes are
window data offset; The 20~22 bytes are window data length. High byte
first.</p>
<p>If no data ,then window data offset and window data length all are
0.</p>
<p>The total length of the data is: the number of the window*22.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pWndData：Window play data:“Text”、“Picture”…</p>
<p>Byte 1：Data Type(1 Text；4 Picture)</p>
<p>Byte 2：Data Format（Like “Text type” in command 0x85 and “Picture
type” in command 0x86）</p>
<p>Byte 3：Text data or picture data。</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_QueryProgram

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Int CPowerBox_Net_QueryProgram( int nCardID ,byte byFlag
, byte* pParam , BYTE* pBuf , int nBufSize );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Query program information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID:Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:Special which program info will to be query 1: Query valid
programs count and program number 2: Query specifies program
information.</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>pParam:</p>
<p>If “byFlag” is 1：byte1~5，resvered，fill 0</p>
<p>If “byFlag” is 2：：byte1，program number；byte2~5，resvered，fill
0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings：

 Query"valid program count and program number"

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Valid program count</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Valid program number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>Each byte identifies an effective program。</p>
<p>Valid value 1～100。</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag

 Query specifies program information

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th><blockquote>
<p>Lenght(byte)</p>
</blockquote></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x89</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data packet of query program
info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Info flag</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”info flag”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>parameters</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Same with send value ”parameters”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Now only return one information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>count</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Program number</td>
<td></td>
<td>1</td>
<td><blockquote>
<p>Program number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>User append</p>
<p>code</p></td>
<td></td>
<td>4</td>
<td><blockquote>
<p>User append code</p>
</blockquote></td>
</tr>
</tbody>
</table>

- The meaning of \"return value\" in the return packet:

> 0x01 Controller not running in program template mode
>
> 0x10 Unknown info flag
>
> 0x11 Invalid programs
>
> 0x12 Can't get program information
>
> CPowerBox_Net_SetProgramProperty

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_SetProgramProperty( int nCardID, byte
byOption , byte byProgramCnt , byte* pPrograms , byte byPropertyID1 ,
byte byPropertyID2 , byte byProgramLevel , USHORT nLoopCnt , USHORT
nTime , byte* pDuetime , byte* pTimeInterval);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set program property</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>nCardID: The control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byOption:</p>
<p>Bit0: Set the range of the program property</p>
<p>0: All programes</p>
<p>1: Specify program</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramCnt:The count of the program</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pPrograms: The list of the programes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ByPropertyID1：Property ID 1, marked which property you want to set
by</p>
<p>byte, set 0 if the data not exist.</p>
<p>Bit0: The level of the program.</p>
<p>Bit1: The cycle count.</p>
<p>Bit2: Valid time. How long will the program be valid from now on.</p>
<p>Bit3: Interval time</p>
<p>Bit4~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>ByPropertyID2: Property ID 2。Bit0~4: valid time. &gt;0 the count of
the valid time.&lt;=4</p>
<p>Bit5~7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byProgramLevel: The program level. 1～3 level, The high level of the
program is priority.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nLoopCnt: Loop count, High byte previous(big-endian).</p>
<p>0: Do not play the program, use to shield program temporarily.</p>
<p>1~255: The loop count of the program.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>nTime: Valid time. High byte previous (big-endian). In minute.</p>
<p>0: Not limit play time</p>
<p>&gt;0: Specify play time in minute.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDuetime: time limit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTimeInterval:The interval time. The start tag
“Hour/Minute/Second”and the end tag “Hour/Minute/Second” both represent
by one byte.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_SetSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_Net_SetSchedule(int nCardID, DWORD
dwAppendCode, BYTE byScheduleNo, const</p>
<p>BYTE* pProperty, const BYTE* pBoxes, BYTE byBoxCnt)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>byScheduleNo: Schedule number，Valid value 1~100。Total support 100
plans, For each plan No, the new data cover the old data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pProperty: play property，total 14 bytes： byte 0：Format and level：
Bit0~3: Data format，fill in 0x01</p>
<p>Bit4~7: Indicates the priority level. The priority level the greater
the value, the more priority to play, 0 is the lowest priority.。。</p>
<p>byte 1：Weekday：Bit0~6: 7-bit logo Sunday to Saturday byte 2~4：
Begin date ， 3 bytes: Byte1:Year,Valid value0~99,means</p>
<p>2000~2999; Byte2:Month ;Byte3:Day</p>
<p>byte 5~7：End date，3 bytes: Byte1:Year,Valid value0~99,means
2000~2999;</p>
<p>Byte2:Month ;Byte3:Day</p>
<p>byte 8~10：Begin time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second
byte 11~13：End time, 3 bytes:Byte1:Hour；Byte2:Minute；Byte3:Second</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBoxes: program number , each byte represents a program. Numbered
in</p>
<p>ascending order, do not repeat.....</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>byBoxCnt:program number count, Valid value:1～100,</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_DeleteSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CPowerBox_Net_DeleteSchedule(int nCardID, DWORD
dwAppendCode, const BYTE* pSchs,</p>
<p>BYTE bySchCnt)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pSchs: schedule number, Valid value 1~100。Each byte represents a
play schedule。</p>
<p>When delete all play schedule, the length of this data is one , value
is 0xff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bySchCnt: The number of play schedule will to be delete。0 means
delete all play plans.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CPowerBox_Net_GetSchedule

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CPowerBox_Net_GetSchedule(int nCardID, DWORD
dwAppendCode, BYTE byType, BYTE byScheduleNo , byte* pBuf , int nBufSize
)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get play schedule</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwAppendCode: The user’s append code, high byte first.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byType：0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byScheduleNo: Valid value:1~100。When query type is 0，this data fill
in 0。</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pBuf: The results data buffer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nBufSize：The size of results data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Can not generate command data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-2: The command data package error</p>
<p>-3: Can not connect controller</p>
<p>-4: Wrong data subcontract</p>
<p>-5: Timeout not receive the return data</p>
<p>-6: The length of return data is not enough, or wrong data
identified</p>
<p>-7: Data validation error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

"pBuf" have the following meanings:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Data Item</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
<th>Lenght(byte)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>0x8d</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Describe the package is the return data which to query play plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Append code</p>
</blockquote></td>
<td></td>
<td>4</td>
<td>The user’s append code, high byte previous.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Query type</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0: Query all valid play plan.</p>
<p>1: Query specified play plan no</p>
<p>Other: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Count /Number</p>
</blockquote></td>
<td></td>
<td>1</td>
<td><p>When query type is 0，this value is valid play schedule count</p>
<blockquote>
<p>When query type is 1，this value is play schedule number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Play schedule number table/ play schedule content</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Variable-length</p>
</blockquote></td>
<td><blockquote>
<p>When query type is 0，this value is valid play schedule number
table</p>
<p>When query type is 1，this value is play schedule content. Data
format like command</p>
<p>0x8B.</p>
</blockquote></td>
</tr>
</tbody>
</table>

You must deal with the return data according to the different query
type.

The meaning of \"return value\" in the return packet:

> 0x01 program template is invalid 0x11 Don't support the query type.
>
> 0x12 Invalid play plan no.
>
> 0x80 currently is not program template way

# Simple use API function  {#simple-use-api-function}

12.1、Overview of RS232 simple use API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 43%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No.</p>
</blockquote></th>
<th>Function name</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_UploadFile</p>
</blockquote></td>
<td><blockquote>
<p>Upload file to controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>CP5200_RS232_DownloadFile</td>
<td><blockquote>
<p>Download file from controller</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>CP5200_RS232_RemoveFile</td>
<td><blockquote>
<p>Delete controller file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>CP5200_RS232_TestController</td>
<td><blockquote>
<p>Test whether controller has connected to PC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>CP5200_RS232_TestCommunication</td>
<td><blockquote>
<p>Test whether controller communication is normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>CP5200_RS232_GetTime</td>
<td><blockquote>
<p>Get controller time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>CP5200_RS232_SetTime</td>
<td><blockquote>
<p>Set controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td>CP5200_RS232_GetTempHumi</td>
<td><blockquote>
<p>Get controller temperature and humidity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>CP5200_RS232_RestartApp</td>
<td><blockquote>
<p>Restart controller app</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>CP5200_RS232_RestartSys</td>
<td><blockquote>
<p>Restart controller system</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>CP5200_RS232_GetTypeInfo</td>
<td><blockquote>
<p>Get controller type information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><p>CP5200_RS232_SendInstantMessage</p>
<p>CP5200_RS232_SendInstantMessage1</p></td>
<td><blockquote>
<p>Send Instant Message</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>CP5200_RS232_ReadHWSetting</td>
<td><blockquote>
<p>Read scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>CP5200_RS232_WriteHWSetting(</td>
<td><blockquote>
<p>Write scan param</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>CP5200_RS232_ReadSoftwareSwitchInfo</td>
<td><blockquote>
<p>Read software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>CP5200_RS232_WriteSoftwareSwitchInfo</td>
<td><blockquote>
<p>Write software switch info</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_ReadNetworkParam</p>
</blockquote></td>
<td><blockquote>
<p>Read network parameter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_WriteNetworkParam</p>
</blockquote></td>
<td><blockquote>
<p>Write network parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_Upgrade</p>
</blockquote></td>
<td><blockquote>
<p>Upgrade controller</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize serial port parameters
>
> Only record the serial parameter initialization parameter information,
> not the actual serial port operation。 Step 2: Use the simple use API
> function

Note: This category interface need\'t to consider whether the serial
port has been open , as long as the serial port parameters have been
initialized.。

12.2、Detail of RS232 simple use API function

> CP5200_RS232_UploadFile
>
> int CP5200_RS232_UploadFile(int nCardID, const char\* pSourceFilename,
> const char
>
> \*pTargetFilename);

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Upload file to controller</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pSourceFilename: Sourse file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pTargetFilename: Purpose file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Error reading source file</p>
<p>-2: Can not generate the command data</p>
<p>-3: Production start file upload data error or the return data of
start file upload errors</p>
<p>-5: Can not open the serial port</p>
<p>-7: Return data of file upload error</p>
<p>-8: File upload does not return data</p>
<p>-9: Production end file upload data errors</p>
<p>-10: Start or end file upload does not return data</p>
<p>-11: Return data of the end file upload errors</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_DownloadFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_RS232_DownloadFile(int nCardID, const
char* pSourceFilename, const char</p>
<p>*pTargetFilename);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Download file from controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSourceFilename: Sourse file name，If the file in the system disk,
name needs coupled with the “S:”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTargetFilename: Purpose file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: failed</p>
<p>-2: Can not generate the command data</p>
<p>-3: Can’t Open controller file</p>
<p>-4: Can’t get controller file information</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-5: Can not open the serial port</p>
<p>-6: Allocation file buffer failed</p>
<p>-7: Read controller file data error -8: Save file error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_RemoveFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_RemoveFile(int nCardID, const char*
pFilename );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete controller file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename : file name，If the file in the system disk, name needs
coupled with the “S:”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Can’t delete file</p>
<p>-1: Incorrect data object handle</p>
<p>-2: Return data type error</p>
<p>-3: Return data length not enough</p>
<p>-4: The buffer length not enough</p>
<p>-5: Can not open the serial port</p>
<p>-6: Can not generate the command data</p>
<p>-7: Can’t get controller file information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_TestController

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_TestController(int nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Test whether controller has connected to PC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: The controller has been connected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_TestCommunication

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_TestCommunication(int nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Test whether controller communication is normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: The communication is normal.</p>
<p>0: The communication is not normal.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>This function is not responsible the opening and closure for the
serial port , can be used as test whether the port is turned on..</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_RS232_GetTime

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_GetTime(int nCardID, BYTE *pBuf, int
nBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: time information buffer, the meaning is</p>
</blockquote>
<ol type="1">
<li><p>byte: second</p></li>
<li><p>byte: minute</p></li>
<li><p>byte: time</p></li>
<li><p>bytes: week</p></li>
<li><p>bytes: day</p></li>
<li><p>bytes: month</p></li>
<li><p>bytes: year (2 digits, together with 2000 is the actual year
value)</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: The length of time information buffer to require no less
than 7 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SetTime

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_SetTime(byte nCardID, const BYTE
*pInfo);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfo: time information buffer, the meaning is</p>
</blockquote>
<ol type="1">
<li><p>byte: second</p></li>
<li><p>byte: minute</p></li>
<li><p>byte: time</p></li>
<li><p>bytes: week</p></li>
<li><p>bytes: day</p></li>
<li><p>bytes: month</p></li>
<li><p>bytes: year (2 digits, together with 2000 is the actual year
value)</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_GetTempHumi

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_GetTempHumi(int nCardID, BYTE * pBuf,
int nBufSize , byte byFlag)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller temperature and humidity</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>pBuf: temperature and humidity information buffer, length is 8 bytes
, the meanings :</p>
<p>byte 0：Query flag. The same as send package byte 1~2：temperature
(degress Celsius)：</p>
<p>Byte 1：Bit7: numeric symbols。1 negative，0 positive。</p>
<p>Bit6~0: the high 7 bit of the integer part of temperature
absolute</p>
</blockquote>
<p>Byte 2：Bit7~4: the lower 4 bit of the integer part of</p>
<blockquote>
<p>temperature absolute</p>
<p>Bit3~0: fractional part ，unit is 1/16(0.0625)</p>
<p>byte 3~4：temperature (degress Fahrenheit)： byte 5：temperature
adjustment value，</p>
<p>Bit7: 1 degress Fahrenheit，0 degress Celsius</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the temperature adjustment</p>
<p>byte 6：humidity。Valid values 0～100 byte 7：humidity adjustment
value</p>
<p>Bit7: reserved</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the humidity adjustment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Temperature information buffer length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:Query flag</p>
<p>Bit0: Is query temperature (0 No,1Yes)</p>
<p>Bit1: Is query humidifier (0 No,1Yes)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_RestartApp

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_RestartApp(byte nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Restart controller app</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_RestartSys

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_RestartSys(byte nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Restart controller system</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_GetTypeInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_GetTypeInfo(byte nCardID, BYTE *pBuf,
int nBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller type information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: control card type information, information means the
following:</p>
<p>byte 0: Control Card Type byte 1: FPGA version bytes 2-5: BIOS
version bytes 6-9: APP version</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: control card type information length, At least 10 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendInstantMessage

int CP5200_RS232_SendInstantMessage( byte nCardID, byte byPlayTimes ,
int x , int

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">y , int cx , int cy , byte byFontSizeColor , int nEffect
, byte nSpeed , byte byStayTime ,const char* pText );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send instant message</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="11">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byFontSizeColor: Font size and color.</p>
<p>Bit0~3: Font size.</p>
<p>Bit4: The weight of the red color</p>
<p>Bit5: The weight of the green color</p>
<p>Bit6: The weight of the blue color</p>
<p>Bit 7: Reserved</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_SendInstantMessage1
>
> CP5200_RS232_SendInstantMessage1( BYTE nCardID, BYTE byPlayTimes , int
> x , int y , int cx , int cy , int nFontSize , byte byColorAlign , int
> nEffect , BYTE nSpeed , BYTE byStayTime ,const char\* pText )

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Send instant message</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="12">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byColorAlign：color and alignment</p>
<p>Bit0: Red flag</p>
<p>Bit1: Green flag</p>
<p>Bit2: Blue flag</p>
<p>Bit3: Resvered</p>
<p>Bit4~5: Horizontal alignment. 0 Left, 1 Middle, 2 right</p>
<p>Bit6~7: Vertical alignment. 0 Top , 1 Middle , 2 Bottom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_ReadHWSetting

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_ReadHWSetting(byte nCardID, BYTE *pBuf,
int nBufSize , int nPassword);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read controller scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>pBuf: Scan param buffer，at least 16 bytes ,see the meaning of each
byte</p>
<p><u>1.14、The meaning of each byte of the scan parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Scan param buffer，at least 16 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_WriteHWSetting

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_WriteHWSetting(byte nCardID, BYTE
*pSetting, int nPassword);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write controller scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSetting: Scan param buffer，16 bytes，see the meaning of each
byte</p>
<p><u>1.14、The meaning of each byte of the scan parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_ReadSoftwareSwitchInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_ReadSoftwareSwitchInfo(BYTE nCardID,
BYTE * pBuf, int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: software switch info buffer, refrence to:</p>
<p><u>CP5200_ParseReadSoftwareSwitchInfoRet</u> pSoftwareSwitchInfoBuf’s
description</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>nBufSize: software switch info’s len, at least 9 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_RS232_WriteSoftwareSwitchInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_RS232_WriteSoftwareSwitchInfo(BYTE
nCardID,const BYTE *pBuf )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: software switch info buffer, refrence to:</p>
<p><u>CP5200_MakeWriteSoftwareSwitchInfoData</u>
pSoftwareSwitchInfoBuf’s description</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_ReadNetworkParam

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_RS232_ReadNetworkParam(BYTE nCardID, BYTE *pBuf,
int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read network connection parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The network connection parameters buffer, meaning each byte is
as follows:</p>
<p>Byte 0 ~ 3: IP address</p>
<p>Byte 4 ~ 7: gateway</p>
<p>Byte 9 ~ 11: the subnet mask</p>
<p>Byte 12 ~ 13: IP port number</p>
<p>Byte 14 ~ 17: network identification code</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>nBufSize: The length of the network connection parameters
information, for not less than 18 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_WriteNetWorkParam

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_RS232_WriteNetworkParam(BYTE nCardID,DWORD dwIP ,
DWORD dwGateway , DWORD dwIPMast , WORD nPort , DWORD dwIDCode )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Setting up the network connection parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIP：IP address</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwGateway：gateway</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIPMast：the subnet mask</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPort：IP port number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIDCode：network identification code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_RS232_Upgrade

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_RS232_Upgrade(int nCardID, int nProgramType ,
const char* pProgramFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Upgrade controller program</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nProgramType: Upgrad program type</p>
<p>3：BIOS</p>
<p>4：APP</p>
<p>5：SCAN</p>
<p>6：NET</p>
<p>8：BAS</p>
<p>9：GRAPH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pProgramFilename: Upgrade program file path name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Error reading source file or program type error</p>
<p>-2: Can not generate the command data</p>
<p>-3: Production start file upload data error or the return data of
start file upload errors</p>
<p>-4: Make upload file data error</p>
<p>-5: Can not open the serial port</p>
<p>-7: Return data of file upload error</p>
<p>-8: File upload does not return data</p>
<p>-9: Production end file upload data errors</p>
<p>-10: Start or end file upload does not return data</p>
<p>-11: Return data of the end file upload errors</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

12.3、Overview of network simple use API function

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 40%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No.</p>
</blockquote></th>
<th>Function name</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_UploadFile</p>
</blockquote></td>
<td><blockquote>
<p>Upload file to controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_DownloadFile</p>
</blockquote></td>
<td><blockquote>
<p>Download file from controller</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_RS232_RemoveFile</p>
</blockquote></td>
<td><blockquote>
<p>Delete controller file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_TestController</p>
</blockquote></td>
<td><blockquote>
<p>Test whether controller is connected to the PC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_TestCommunication</p>
</blockquote></td>
<td><blockquote>
<p>Test whether controller communication is</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>normal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>CP5200_Net_GetTime</td>
<td><blockquote>
<p>Get controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>CP5200_Net_SetTime</td>
<td><blockquote>
<p>Set controller time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td>CP5200_Net_GetTempHumi</td>
<td><blockquote>
<p>Get controller temperature and humidity</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>CP5200_Net_RestartApp</td>
<td><blockquote>
<p>Restart controller app</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>CP5200_Net_RestartSys</td>
<td><blockquote>
<p>Restart controller system</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>CP5200_Net_GetTypeInfo</td>
<td><blockquote>
<p>Get controller type information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><p>CP5200_Net_SendInstantMessage</p>
<p>CP5200_Net_SendInstantMessage1</p></td>
<td><blockquote>
<p>Send instant message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>CP5200_Net_ReadHWSetting</td>
<td><blockquote>
<p>Read scan param</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>CP5200_Net_WriteHWSetting(</td>
<td><blockquote>
<p>Write scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>CP5200_Net_ReadSoftwareSwitchInfo</td>
<td><blockquote>
<p>Read software switch info</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>CP5200_Net_WriteSoftwareSwitchInfo</td>
<td><blockquote>
<p>Write software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_QueryControllerInfo</p>
</blockquote></td>
<td><blockquote>
<p>Query controller information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_ReadNetworkParam</p>
</blockquote></td>
<td><blockquote>
<p>Read network parameter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_WriteNetworkParam</p>
</blockquote></td>
<td><blockquote>
<p>Write network parameter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_Net_Upgrade</p>
</blockquote></td>
<td><blockquote>
<p>Upgrade controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Usage:
>
> Step 1: Initialize network parameters
>
> Only record the network parameter initialization parameter
> information, not the actual network operation。 Step 2: Use the simple
> use API function

Note: This category interface need\'t to consider whether the network
has been connected, as long as the network parameters have been
initialized.。

12.4、Detail of network simple use API function

> CP5200_Net_UploadFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Net_UploadFile(int nCardID, const char*
pSourceFilename, const char</p>
<p>*pTargetFilename);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Upload file to controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSourceFilename: Sourse file name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTargetFilename: Purpose file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Error reading source file</p>
<p>-2: Can not generate the command data</p>
<p>-3: Production start file upload data error or the return data of
start file upload errors</p>
<p>-5: Can not connect controller</p>
<p>-7: Return data of file upload error</p>
<p>-8: File upload does not return data</p>
<p>-9: Production end file upload data errors</p>
<p>-10: Start or end file upload does not return data</p>
<p>-11: Return data of the end file upload errors</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Net_DownloadFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_Net_DownloadFile(int nCardID, const char*
pSourceFilename, const char</p>
<p>*pTargetFilename);</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Download file from controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSourceFilename: Sourse file name，If the file in the system disk,
name needs coupled with the “S:”</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pTargetFilename: Purpose file name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: failed</p>
<p>-2: Can not generate the command data</p>
<p>-3: Can’t Open controller file</p>
<p>-4: Can’t get controller file information</p>
<p>-5: Can not connect controller</p>
<p>-6: Allocation file buffer failed</p>
<p>-7: Read controller file data error -8: Save file error</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Net_RemoveFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_RemoveFile(int nCardID, const char*
pFilename );</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Delete controller file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename : file name，If the file in the system disk, name needs
coupled with the “S:”</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Can’t delete file</p>
<p>-1: Incorrect data object handle</p>
<p>-2: Return data type error</p>
<p>-3: Return data length not enough</p>
<p>-4: The buffer length not enough</p>
<p>-5: Can not connect controller</p>
<p>-6: Can not generate the command data</p>
<p>-7: Can’t get controller file information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Net_TestController

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_TestController(int nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Test whether controller is connected to the PC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;0: The controller has been connected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_Net_TestCommunication

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_TestCommunication(int nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Test whether controller communication is normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: The communication is normal.</p>
<p>0: The communication is not normal.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>This function is not responsible the opening and closure for the
serial port , can be used as test whether the port is turned on..</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CP5200_Net_GetTime

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_GetTime(int nCardID, BYTE *pBuf, int
nBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: time information buffer, the meaning is</p>
</blockquote>
<ol type="1">
<li><p>byte: second</p></li>
<li><p>byte: minute</p></li>
<li><p>byte: time</p></li>
<li><p>bytes: week</p></li>
<li><p>bytes: day</p></li>
<li><p>bytes: month</p></li>
<li><p>bytes: year (2 digits, together with 2000 is the actual year
value)</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: The length of time information buffer to require no less
than 7 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SetTime

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_SetTime(byte nCardID, const BYTE
*pInfo);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Set controller time</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pInfo: time information buffer, the meaning is</p>
</blockquote>
<ol type="1">
<li><p>byte: second</p></li>
<li><p>byte: minute</p></li>
<li><p>byte: time</p></li>
<li><p>bytes: week</p></li>
<li><p>bytes: day</p></li>
<li><p>bytes: month</p></li>
<li><p>bytes: year (2 digits, together with 2000 is the actual year
value)</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_GetTemperature

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_GetTemperature(int nCardID, BYTE *pBuf,
int nBufSize , byte byFlag)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller temperature and humidity</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>pBuf: temperature and humidity information buffer, length is 8 bytes
, the meanings :</p>
<p>byte 0：Query flag. The same as send package byte 1~2：temperature
(degress Celsius)：</p>
<p>Byte 1：Bit7: numeric symbols。1 negative，0 positive。</p>
<p>Bit6~0: the high 7 bit of the integer part of temperature
absolute</p>
</blockquote>
<p>Byte 2：Bit7~4: the lower 4 bit of the integer part of</p>
<blockquote>
<p>temperature absolute</p>
<p>Bit3~0: fractional part ，unit is 1/16(0.0625)</p>
<p>byte 3~4：temperature (degress Fahrenheit)： byte 5：temperature
adjustment value，</p>
<p>Bit7: 1 degress Fahrenheit，0 degress Celsius</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the temperature adjustment</p>
<p>byte 6：humidity。Valid values 0～100 byte 7：humidity adjustment
value</p>
<p>Bit7: reserved</p>
<p>Bit6: 1 negative，0 positive</p>
<p>Bit5~0: The absolute value of the humidity adjustment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Temperature information buffer length</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFlag:Query flag</p>
<p>Bit0: Is query temperature (0 No,1Yes)</p>
<p>Bit1: Is query humidifier (0 No,1Yes)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_RestartApp

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_RestartApp(byte nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Restart controller app</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_RestartSys

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_RestartSys(byte nCardID);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Restart controller system</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_GetTypeInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_GetTypeInfo(byte nCardID, BYTE *pBuf, int
nBufSize);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Get controller type information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: control card type information, information means the
following:</p>
<p>byte 0: Control Card Type byte 1: FPGA version bytes 2-5: BIOS
version bytes 6-9: APP version</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: control card type information length, At least 10 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendInstantMessage
>
> int CP5200_Net_SendInstantMessage( byte nCardID, byte byPlayTimes ,
> int x , int y , int cx , int cy , byte byFontSizeColor , int nEffect ,
> byte nSpeed , byte byStayTime ,const char\* pText );

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Description</th>
<th><blockquote>
<p>Send instant message</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byFontSizeColor: Font size and color.</p>
<p>Bit0~3: Font size.</p>
<p>Bit4: The weight of the red color</p>
<p>Bit5: The weight of the green color</p>
<p>Bit6: The weight of the blue color</p>
<p>Bit 7: Reserved</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_SendInstantMessage1

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_Net_SendInstantMessage1( BYTE nCardID, BYTE
byPlayTimes , int x , int y , int cx , int cy , int nFontSize , byte
byColorAlign , int nEffect , BYTE nSpeed , BYTE byStayTime ,const char*
pText )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Send instant message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="8"></td>
<td><blockquote>
<p>byPlayTimes: Play times, from 0 to 255. 0 means continue play until
new commands arrive.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>x: Display start point x,the upper left corner of the abscissa.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>y: Display start point y, the upper left corner of the ordinate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cx: Display width. 0 means set to maximum width.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cy: Display height. 0 means set to maximum height.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nFontSize: font size and style，see <u>1.7. Font size code and font
style</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byColorAlign：color and alignment</p>
<p>Bit0: Red flag</p>
<p>Bit1: Green flag</p>
<p>Bit2: Blue flag</p>
<p>Bit3: Resvered</p>
<p>Bit4~5: Horizontal alignment. 0 Left, 1 Middle, 2 right</p>
<p>Bit6~7: Vertical alignment. 0 Top , 1 Middle , 2 Bottom</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nEffect: Display effect.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>nSpeed: Display speed,0~255.The smaller the faster. Invalid when set
to display immediately.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>byStayTime: Stay time. High byte previous(big endian).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: The text data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_ReadHWSetting

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_ReadHWSetting(byte nCardID, BYTE *pBuf,
int nBufSize , int nPassword);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read controller scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: Scan param buffer，at least 16 bytes ,see the meaning of each
byte</p>
<p><u>1.14、The meaning of each byte of the scan parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: Scan param buffer，at least 16 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_WriteHWSetting

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_WriteHWSetting(byte nCardID, BYTE
*pSetting, int nPassword);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write controller scan param</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: Controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pSetting: Scan param buffer，16 bytes，see the meaning of each
byte</p>
<p><u>1.14、The meaning of each byte of the scan parameters</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPassword: Parsing code, depending on the control card filled with
different passwords, or not to accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_ReadSoftwareSwitchInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_ReadSoftwareSwitchInfo(BYTE nCardID, BYTE
* pBuf, int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: software switch info buffer, refrence to:</p>
<p><u>CP5200_ParseReadSoftwareSwitchInfoRet</u> pSoftwareSwitchInfoBuf’s
description</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize: software switch info’s len, at least 9 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_WriteSoftwareSwitchInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_WriteSoftwareSwitchInfo(BYTE
nCardID,const BYTE *pBuf )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Write software switch info</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: software switch info buffer, refrence to:</p>
<p><u>CP5200_MakeWriteSoftwareSwitchInfoData</u>
pSoftwareSwitchInfoBuf’s description</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_QueryControllerInfo

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_Net_QueryControllerInfo(BYTE nCardID, byte
byInfoFlag, byte *pInfoBuf, int nInfoBufLen, const char *szSavePath
)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Query controller information</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: controller ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>byInfoFlag：Query flag , currently only support 0x0b</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"></td>
<td><blockquote>
<p>pInfoBuf：Query result buffer byte 0~1: program number. High byte in
the front, the first program starting from 1, 0 means no program in play
or broadcast information temporarily byte 2~3: Play item number.</p>
<p>Byte 4~7: The program has been broadcast time, the unit is 1/10 of a
second, high byte in the front.</p>
<p>Byte 8~11: Play the item have play time, unit is 1/10 of a second,
high byte in the front.</p>
<p>Byte 12~13: image width, high byte in the front</p>
<p>Byte 14~15: image height, high byte in the front</p>
<p>Byte 16: color and gray level</p>
<p>Byte 17~20: image data length, high byte in the front</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nInfoBufLen：Query result buffer lenrth，must bigger than 21
bytes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>szSavePath：The path of save the display screen images.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Successful</p>
<p>0: Failed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_ReadNetworkParam

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_Net_ReadNetworkParam(BYTE nCardID, BYTE *pBuf,
int nBufSize )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Read network connection parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pBuf: The network connection parameters buffer, meaning each byte is
as follows:</p>
<p>Byte 0 ~ 3: IP address</p>
<p>Byte 4 ~ 7: gateway</p>
<p>Byte 9 ~ 11: the subnet mask</p>
<p>Byte 12 ~ 13: IP port number</p>
<p>Byte 14 ~ 17: network identification code</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>nBufSize: The length of the network connection parameters
information, for not less than 18 bytes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_WriteNetWorkParam

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_Net_WriteNetworkParam(BYTE nCardID,DWORD dwIP ,
DWORD dwGateway , DWORD dwIPMast , WORD nPort , DWORD dwIDCode )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Setting up the network connection parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6">Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIP：IP address</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>dwGateway：gateway</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIPMast：the subnet mask</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nPort：IP port number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dwIDCode：network identification code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>1: Success</p>
<p>0: Fail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_Net_Upgrade

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">CP5200_Net_Upgrade(int nCardID, int nProgramType , const
char* pProgramFilename)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Upgrade controller program</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Parameter</td>
<td><blockquote>
<p>nCardID: control card ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>nProgramType: Upgrad program type</p>
<p>3：BIOS</p>
<p>4：APP</p>
<p>5：SCAN</p>
<p>6：NET</p>
<p>8：BAS</p>
<p>9：GRAPH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pProgramFilename: Upgrade program file path name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Success</p>
<p>-1: Error reading source file or program type error</p>
<p>-2: Can not generate the command data</p>
<p>-3: Production start file upload data error or the return data of
start file upload errors</p>
<p>-4: Make upload file data error</p>
<p>-5: Can not connect controller</p>
<p>-7: Return data of file upload error</p>
<p>-8: File upload does not return data</p>
<p>-9: Production end file upload data errors</p>
<p>-10: Start or end file upload does not return data</p>
<p>-11: Return data of the end file upload errors</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

# Other API  {#other-api}

13.1、Overview of other API

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 35%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>No.</p>
</blockquote></th>
<th>Function name</th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_CalcImageDataSize</p>
</blockquote></td>
<td><blockquote>
<p>Image data size calculation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>CP5200_MakeImageDataFromFile</p>
</blockquote></td>
<td><blockquote>
<p>Image data obtained from the image file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>CP5200_TextToImage</td>
<td><blockquote>
<p>Image file generates from formatted text</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>CP5200_TextToImageW</td>
<td><blockquote>
<p>Image file generates from formatted text(wide character)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>CP5200_TextToImageEx</td>
<td><blockquote>
<p>Image file generates from extent formatted text</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

13.2、Detail of other API

> CP5200_CalcImageDataSize

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_CalcImageDataSize(WORD imgw, WORD imgh, BYTE
color)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Image data size calculation</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Parameter</td>
<td><blockquote>
<p>imgw: Image width</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>imgh: Image height</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>color: Image color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Image data size</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_MakeImageDataFromFile

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_MakeImageDataFromFile(WORD imgw, WORD
imgh, BYTE color, BYTE</p>
<p>*pDatBuf, int nBufSize, const char* pFilename, int nMode)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Image data obtained from the image file</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7">Parameter</td>
<td><blockquote>
<p>imgw: Image width</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>imgh: Image height</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>color: Image color</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pDatBuf：Image data buffer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nBufSize：Image data buffer size</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pFilename：Picture file path name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nMode:Picture mode,see<u>1.9. Picture effect code</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>&gt;=0: Image data size</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>-1: Image file not found or load failed</p>
<p>-2: Image conversion failed</p>
<p>-3: Picture mode is wrong</p>
<p>-4: Image data buffer length is not enough</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_TextToImage

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>int CP5200_TextToImage( const char *pSavePath, const
char *pText, const char</p>
<p>*pFontFaceName, const byte *pFormatData, const byte *pScreenData
)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Image file generates from formatted text</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>pSavePath：Path to save</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pFontFaceName：Font face name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pformatData：<u>Formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pScreenData：<u>Screen data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Successful</p>
<p>-1：Failed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

> CP5200_TextToImageW

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_TextToImageW( const char *pSavePath, const
wchar_t *pText, const char *pFontFaceName, const byte *pFormatData,
const byte *pScreenData )</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Image file generates from formatted text(wide character)</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5">Parameter</td>
<td><blockquote>
<p>pSavePath：Path to save</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pText: Text string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pFontFaceName：Font face name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pformatData：<u>Formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pScreenData：<u>Screen data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Return</td>
<td><blockquote>
<p>0: Successful</p>
<p>-1：Failed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>

CP5200_TextToImageEx

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">int CP5200_TextToImageEx(const char *pSavePath, const
byte *pTextContent, const byte *pFormatData, const byte *pScreenData
);</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><blockquote>
<p>Image file generates from extent formatted text</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4">Parameter</td>
<td><blockquote>
<p>pSavePath：Path to save</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pTextContent: <u>Extent formatted text content</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>pFormatData：<u>Extent formatted text control data</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pScreenData：<u>Extent screen data</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Return</td>
<td><blockquote>
<p>0: Successful</p>
<p>-1：Failed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Note</td>
<td></td>
</tr>
</tbody>
</table>
