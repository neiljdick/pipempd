#!/usr/bin/python -tt

import sys
import os
import mpd
import pprint
import socket


# This is the directory where the script resides. 
# We need to know this path in order to call our controls..
PROGDIR="/.config/openbox/pipempd"

# mpd server details
HOST = 'localhost'
PORT = '6600'

CON_ID = {'host':HOST, 'port':PORT}

stats = {}
status = {}
def mpdConnect(client, con_id):
  """ Simple wrapper to connect to mpd
  """
  try:
    client.connect(**con_id)
  except SocketError:
    return False
  return True

def obPrintMenu(client):
  status = client.status()
  stats = client.stats()
  songs =  client.currentsong()
  print "<openbox_pipe_menu>"
  print "<item label=\"Playing: "+songs["title"]+" By "+songs["artist"]+"\">"
  print "</item>"
  print "<item label=\"Status: "+status["state"]+"\">"
  print "</item>"
  print '<item label="Play"> <action name="Execute"><execute>'+str(os.getcwd())+PROGDIR+"/pipempd.py -play</execute></action></item>"
  print '<item label="Pause"> <action name="Execute"><execute>'+str(os.getcwd())+PROGDIR + "/pipempd.py -pause</execute></action></item>"
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
    elif(sys.argv[1] == "-stop"):
      client.stop()
    elif(sys.argv[1] == "-pause"):
      client.pause()
    else:
      print "unknown option"
      
  else:
    # call a function to fill in some strings
    # Print the openbox pipe menu
    obPrintMenu(client)

  client.disconnect()
  sys.exit(0)

if __name__ == "__main__":
  main()
