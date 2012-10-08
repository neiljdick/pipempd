#!/usr/bin/python -tt

import sys
import os
import mpd
import pprint
import socket


PROGDIR="/.config/openbox/pipempd"

HOST = 'localhost'
PORT = '6600'

CON_ID = {'host':HOST, 'port':PORT}

def mpdConnect(client, con_id):
  """ Simple wrapper to connect to mpd
  """
  try:
    client.connect(**con_id)
  except SocketError:
    return False
  return True

def obPrintOptions():
  print "<openbox_pipe_menu>"
  print '<item label="Play"> <action name="Execute"><execute>'+str(os.getcwd())+PROGDIR+"/pipempd.py -play</execute></action></item>"
  print '<item label="Stop"> <action name="Execute"><execute>'+str(os.getcwd())+PROGDIR + "/pipempd.py -stop</execute></action></item>"
  print "</openbox_pipe_menu>"


def main():
  client = mpd.MPDClient()
  if not mpdConnect(client, CON_ID):
    #print 'Got Connected!'
    #print 'failedto connect to MPD Server'
    sys.exit(1)

  if(len(sys.argv) == 2):
     if(sys.argv[1] == "-play"):
       client.play()
     if(sys.argv[1] == "-stop"):
       client.stop()

  else:
     obPrintOptions()

  client.disconnect()
  sys.exit(0)
    




if __name__ == "__main__":
  main()
