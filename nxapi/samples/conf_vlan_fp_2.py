#! /usr/bin/python

import requests
import json
import sys

username = "admin"
password = "c15c0123!"


def add_vlan (ip_addr, vl_num):
    myheaders = {'content-type': 'application/json-rpc'}
    url = "http://"+ip_addr+"/ins"
    payload=[
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vl_num,"version": 1},"id": 2},
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()


print "enter vlan to be configured"
vlanId=raw_input()

with open("switch_list.txt") as fobj:
    for line in fobj:
        ip = line
        print "adding  vlan id %s  to %s" % (vlanId, ip)
        myheaders = {'content-type': 'application/json-rpc'}
        url = "http://"+ip+"/ins"
        payload=[
            {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
            {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vlanId,"version": 1},"id": 2},
            {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
        ]
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()






