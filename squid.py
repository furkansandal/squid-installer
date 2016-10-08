#!/usr/bin/env python
import subprocess, time
print "Otomatik Squid Proxy Kurulumu, 3128 stock port üzerine.\n"
print "https://github.com/furkansandal https://fb.me/Par4noiD"
s=subprocess
s.call(["sudo", "apt-get", "update"])
time.sleep(1)
s.call(["sudo", "apt-get", "install", "squid"])
time.sleep(1)
yol="/etc/squid3/squid.conf"

dosya=open(yol).read()

a=dosya.replace("http_access allow localhost manager", "http_access allow all")
b=a.replace("http_access deny manager", "http_access allow all")
c=b.replace("http_access allow localhost\n", "http_access allow all\n")

dosya_port=dosya.split("\nhttp_port ")[1].split("\n")[0]
print "mevcut portunuz", dosya_port
port=raw_input("Degisecek port numarasini girin: ")
c_port=c.replace("\nhttp_port "+dosya_port+"\n", "\nhttp_port "+port+"\n")
open("/etc/squid3/squid.conf", "w").write(c_port)
s.call(["sudo", "service", "squid3", "restart"])
print "gerekli ayarlariniz yapildi, squid proxy'i kullanabilirsiniz."