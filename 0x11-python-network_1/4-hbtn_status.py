#!/usr/bin/python3
"""
same as 0-hbtn_status with requests model
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(url.text)))
    print('\t- content: {}'.format(url.text))
