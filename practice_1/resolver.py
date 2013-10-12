import socket, struct
def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]
def ipEnterSafe(str):
  ip = ""
  while not ip2long(ip):
    ip = input(str)
  return ip

d = {}
fname = 'text.txt'
f = open(fname, 'r')
for line in f:
  x = line.split(' ')
  d[x[0]]=x[1]
f.close()
for key in d:
    print key, 'corresponds to', d[key]
host = input('Enter a host name: ')
ip = ipEnterSafe('Enter a ip ')
f = open(fname, 'a')
f.write(line + '\n')
f.close()
host = input('Enter a host to find ip: ')
print d.get(host)
ip = ipEnterSafe('Enter a ip to find host: ')
for key, value in d.iteritems():
  if value == ip:
    print key