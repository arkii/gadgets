#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Cycle text and detail text</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Arkii</bitbar.author>
# <bitbar.author.github>arkii</bitbar.author.github>
# <bitbar.desc>Plugin to show icinga2 tactical overview, developed by python, in order to use this plugin, you should enable icinga2-api first.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://github.com/arkii/gadgets/Utility/BitBar/icinga2-api-overview.png</bitbar.image>
# <bitbar.abouturl>https://github.com/arkii/gadgets/Utility/BitBar/icinga2-api-overview.py</bitbar.abouturl>

__author__ = 'arkii'
__email__ = 'sun.qingyun@zol.com.cn'
__create__ = '2016.01.25 10:42'
__project__ = 'gadgets'
__filename_in_project__ = 'Utility/BitBar/icinga2-api-overview.py'

import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''
    STATE
    0 : OK
    1 : Warning
    2 : Critical
    3 : Unknown
'''

SERVER = 'your-icinga2-server'
PORT = 5665
API = 'https://{server}:{port}'.format(server=SERVER, port=PORT)
USER = 'your-icinga2-api-user'
PASSWORD = 'your-icinga2-api-pass'
BASE_URL = 'http://{server}/icingaweb2/monitoring/list'.format(server=SERVER)
TPL_DATA = {
    'base_url': BASE_URL,
    'svc_uri': '/services?service_state=',
    'hst_uri': '/hosts?host_state='
}

TEMPLATE = '''OK {n_svc_ok} | color=#44bb77
CR {n_svc_cr} | color=#ff5566 href={base_url}{svc_uri}2
WN {n_svc_wn} | color=#ffaa44 href={base_url}{svc_uri}1
UK {n_svc_uk} | color=#aa44ff href={base_url}{svc_uri}3
---
HOST UP {n_hst_up} | color=#44bb77 href={base_url}{hst_uri}2
HOST DOWN {n_hst_dw} | color=#ff5566 href={base_url}{hst_uri}1
'''
ERR_TPL = '''ERROR | color=#ff5566
---
{errors} | trim=true'''


def main():
    headers = {
        'Accept': 'application/json',
        'X-HTTP-Method-Override': 'GET'
    }
    res = '/v1/status/CIB'
    url = API + res
    req = requests.post(url,
                        headers=headers,
                        auth=(USER, PASSWORD),
                        verify=False)
    # verify='ca.crt')
    if req.status_code == 200:
        data = req.json()
        status = data['results'][0]['status']
        TPL_DATA['n_svc_ok'] = int(status['num_services_ok'])
        TPL_DATA['n_svc_cr'] = int(status['num_services_critical'])
        TPL_DATA['n_svc_wn'] = int(status['num_services_warning'])
        TPL_DATA['n_svc_uk'] = int(status['num_services_unknown'])
        TPL_DATA['n_hst_up'] = int(status['num_hosts_up'])
        TPL_DATA['n_hst_dw'] = int(status['num_hosts_down'])
        print(TEMPLATE.format(**TPL_DATA))
    else:
        print(ERR_TPL.format(errors=req.text))


if __name__ == '__main__':
    main()
