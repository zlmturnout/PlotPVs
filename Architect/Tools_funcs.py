from re import T
import time, random, sys, os, math, datetime, traceback
import requests,socket,struct
from bs4 import BeautifulSoup

# def getIP(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     IP = socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15].encode('utf-8'))
#     )[20:24])
#     s.close()
#     return IP

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
 
    return ip


def download_url(url, num_retries=5):
    """
    download url
    :param url:
    :param num_retries:
    :return: html in text
    """
    headers = {'User-Agent': 'SSRF_test', 'Connection': 'close'}
    try:
        with requests.Session() as s:
            resp = s.get(url, headers=headers, proxies=None, timeout=10)
            html = resp.text
            s.close()
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download_url(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e)
        html = None
    return html

def get_datetime():
    """ get current date time, as accurate as milliseconds

        Args: None

        Returns:
            str type '%Y-%m-%d %H:%M:%S.%f'
            eg: "2018-10-01 00:32:39.993176"

    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

def SSRFBeamStatus(SSRF_http='http://159.226.222.249/ssrf/beam/'):
    """ get the SSRF Beam Status by internet

    Args:
        http_address (str, optional):  Defaults to 'http://159.226.222.249/ssrf/beam/'.

    Returns:
        current,beam_status(str,dict): beam current and all info in dict format
        
        return ('error',{}) if connection failed
    """
    SSRF_http='http://159.226.222.249/ssrf/beam/'
    beam_html = download_url(SSRF_http, num_retries=5)
    if beam_html:
        soup = BeautifulSoup(beam_html, 'html.parser')
        # title = soup.title.text
        text_info = soup.text.split('\n')
        text_info = [t for t in text_info if t != '']
        # find the current and other information
        Current = text_info[text_info.index('Current:') + 1]
        try: 
            float(Current.split('mA')[0]),2
        except Exception as e:
            error_info = traceback.format_exc() + str(e) + '\n'
            print(error_info)
            Current_num=0.0
        else:
            Current_num=round(float(Current.split('mA')[0]),2)
        #print('Current:' + Current)
        Operation_info = text_info[text_info.index('Orbit(rms)x/y:') + 2]
        #print(Operation_info)
        [plan, light] = [Operation_info.split('light:')[0].split(':')[-1], Operation_info.split('light:')[-1]]
        #print([plan, light])
        # full beam_info
        beam_status={}
        beam_status['Operator']=Operation_info.split('shift plan:')[0].split(':')[-1]
        beam_status['Light']=light
        beam_status['ShiftPlan']=plan
        for idx in range(2,24):
            if idx%2==1:
                name=text_info[idx].split(':')[0]
                beam_status[name]=text_info[idx+1]
        beam_status['Current']=f'{Current_num}mA'
    else:
        Current_num,beam_status = 0.0,dict()
    return Current_num,beam_status

if __name__ == '__main__':
    SSRF_http='http://159.226.222.249/ssrf/beam/'
    current,beam_info = SSRFBeamStatus(SSRF_http)
    print(f'Current: {beam_info["Current"]},\nPlan: {beam_info["ShiftPlan"]},\nLight: {beam_info["Light"]}')
    print(beam_info)
    print(f'IP:{get_host_ip()}')