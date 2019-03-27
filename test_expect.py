#!/usr/local/bin/python3
import pexpect
import sys
import subprocess

child = pexpect.spawn('ssh 106.13.38.59')
fout = open('log.txt', 'wb')
child.logfile = fout

def get_result():
    child.expect(["# "])
    child.sendline('/bin/bash -c "echo {} >/root/log.txt"'.format('nimabi'))
    child.expect("# ")

index = child.expect(["yes/no", "password:", pexpect.EOF, pexpect.TIMEOUT])
try:
  if index == 0: 
      child.sendline("yes")
      child.expect(["password: "])
      child.sendline("Cao8992908@xing")
      get_result()
  elif index == 1: 
      child.sendline("Cao8992908@xing")
      get_result()
except Exception as e:
  print (e)
#child.expect(["password: "])
#child.sendline("Cao8992908@xing")
subprocess.call('cat /home/xingge/log.txt', shell = 'True')
