import time
import utime
import network
import socket
from machine import Pin

ssid = "ssid"
password = "password"
db_host = "host"
db_port = "port"
err_host = "host"
err_port = "port"

def wifi_connect(): #connect to wifi
    wifi = network.WLAN(network,STA_IF)
    wifi.active(True)
    
    while (wifi.isconnected() == false):
        wifi.connect(ssid,password)
        time.sleep(.5)
    return wifi
    
def read_sensor(): #reading sensors
    
    
def service(): #reading sensors until laundry done
    #figure out how to detect when laundry is done
    return msg #returns sends a message when laundry is done

def status_update(status):
#copy send_message code and edit for status db (post /status)
    
    
def send_message(message): #send message to server\
    post_data = message.encode('utf-8')
    req = f"""\
POST /laundry HTTP/1.1
Host: {db_host}
Content-Type: text/plain
Content-Length: {len(post_data)}

{message}"""
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host,port))
        sock.sendall(req)
    except Exception as e:
        err_log = f"""\
POST /err_log HTTP/1.1
Host: {err_host}
Content-Type: text/plain
Content-Length: {len()}

{err_log}"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((err_host,err_port))
        sock.sendall(err_log)#send exception text
    finally:
        sock.close()
        
        
while(read_sensor != 1):
    time.sleep(.5)
send_message("Laundry is starting")
send_message(service())

    