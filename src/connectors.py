import socket
import paramiko
import requests
import urllib.parse as parse
import httplib2
conn = httplib2.HTTPConnectionWithTimeout(host=, port=)
conn.connect()
resp = conn.getresponse()
resp.status, resp.reason
ssh = paramiko.SSHClient()
ssh.connect()
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.connect(("", 22))

_transport = paramiko.Transport(proxy_socket)
_transport.connect()
# ssh.connect(hostname="", port=22, username="", password="", sock=proxy_socket)

