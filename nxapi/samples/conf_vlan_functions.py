#!/usr/bin/python

import requests
import json


my_headers = {'content-type': 'application/json-rpc'}
username = "admin"
password = "c15c0123!"
done = "no"


menu = (

"""
c - create new vlan
d - delete vlan
e - exit

"""
)

def configure_vlan(ip, vlanId):
    url = "http://"+ip+"/ins"
    
    payload=[
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vlanId,"version": 1},"id": 2},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
    ]

    response = requests.post(url,data=json.dumps(payload), headers=my_headers,auth=(username,password)).json()

def delete_vlan(ip, vlanId):
    url = "http://"+ip+"/ins"
    
    payload=[
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "no vlan "+vlanId,"version": 1},"id": 2},
      {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
    ]

    response = requests.post(url,data=json.dumps(payload), headers=my_headers,auth=(username,password)).json()


def print_vlans(ip):
    url = "http://"+ip+"/ins"
    vlans = []
    payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "show vlan brief",
                     "version": 1},
          "id": 1}
         ]
    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()
    vlan_table = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']
    print ("\n"+"="* 35)
    print "printing configured vlans on %s"%ip
    for iter in vlan_table:
        print iter["vlanshowbr-vlanid-utf"],
    print ("\n"+"="*35)
    
def print_vlan_info(ip):
  pass
    
def exit():
    global done
    done = "yes"
    
choices = {
"c": configure_vlan,
"d": delete_vlan,
"e": exit
}

def main():
    print "enter ip address"
    ip=raw_input()
    print_vlans(ip)
    choice = raw_input(menu)
    while(done != "yes"):
        if choice != "e":
            vlanId = raw_input("Enter VLAN to create or delete:\n")
            try:
                choices[choice](ip,vlanId)
            except KeyError:
                print "Unrecognized command ", choice
            print_vlans(ip)
            choice = raw_input(menu)
        else:
            choices[choice]()
    print " End of vlan script"
    
if __name__ == "__main__":
    main()
 
