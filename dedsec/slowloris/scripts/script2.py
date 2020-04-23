import socket

def makeSocket(site):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(4)
  s.connect((site,80))
  return s

def main():
  site = 'INSERT IP ADDRESS OF YOUR TARGET'
  header = ("GET / HTTP/1.1 \r\n"
            "Host: http//INSERT IP ADDRESS OF YOUR TARGET"
            "User-Agent: python-requests/2.18.1\r\n"
            "Accept-Encoding: gzip, deflate\r\n"
            "Accept: */*\r\n"
            "Connection: keep-alive\r\n"
            "\r\n")
  s = makeSocket(site)
  s.send(header.encode("utf-8"))
  
if __name__ == '__main__':
  main()