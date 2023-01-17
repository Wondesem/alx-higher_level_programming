#!/usr/bin/python3
"""What's my status?"""
import urllib.request

with uri.urlopen('https://intranet.hbtn.io/status') as res:
    res = res.read()

print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(res), res))
print('\t- utf8 content: {}'.format(str(res, 'utf-8')))
