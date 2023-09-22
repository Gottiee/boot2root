# HTTP port 80

### Reminder

```bash
80/tcp  open  http       Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Hack me if you can
443/tcp open  ssl/http   Apache httpd 2.2.22
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=BornToSec
| Issuer: commonName=BornToSec
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2015-10-08T00:19:46
| Not valid after:  2025-10-05T00:19:46
| MD5:   3f63 02ca 0bb1 e732 9987 6887 3623 86a3
|_SHA-1: eebc f8de 3422 dd63 5314 9d47 811f f6d1 8f77 c98d
|_ssl-date: 2023-08-12T12:57:53+00:00; +8s from scanner time.
```

## Metasploit

```bash
use auxiliary/scanner/http/dir_scanner
run
[*] Detecting error code
[*] Using code '404' as not found for 192.168.1.120
[+] Found http://192.168.1.120:80/cgi-bin/ 404 (192.168.1.120)
[+] Found http://192.168.1.120:80/doc/ 404 (192.168.1.120)
[+] Found http://192.168.1.120:80/forum/ 404 (192.168.1.120)
[+] Found http://192.168.1.120:80/icons/ 404 (192.168.1.120)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

We found 4 directories, but we can't access them : 403 forbidden.

## HTTPS listing with dirb command

http page return 403 forbidden so i try with https:443

```bash
dirb https://192.168.1.120:443
```

Most interesting result are: 

```bash
+ https://192.168.1.120:443/cgi-bin/ (CODE:403|SIZE:290) 
==> DIRECTORY: https://192.168.1.120:443/forum/
==> DIRECTORY: https://192.168.1.120:443/phpmyadmin/   
+ https://192.168.1.120:443/server-status (CODE:403|SIZE:295) 
==> DIRECTORY: https://192.168.1.120:443/webmail/
```

There is 5 directory to exploit.

- [Exploit the Forum](/http-https/forum.md)