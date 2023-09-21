# Reconnaissance

## Find ip address of BornToSeeHackMe 

Scan lan network:

```bash
$> nmap -sn 192.168.1.0/24
Nmap scan report for BornToSecHackMe (192.168.1.119)
Host is up (0.00076s latency).
```

## Scan with nmap

To determine if ssh is running and the ssh port, I can run nmap on the ip address:

```bash
$> nmap 192.168.1.120 -sV -sC -v

PORT    STATE SERVICE    VERSION
21/tcp  open  ftp        vsftpd 2.0.8 or later
|_ftp-anon: got code 500 "OOPS: vsftpd: refusing to run with writable root inside chroot()".
22/tcp  open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 07:bf:02:20:f0:8a:c8:48:1e:fc:41:ae:a4:46:fa:25 (DSA)
|   2048 26:dd:80:a3:df:c4:4b:53:1e:53:42:46:ef:6e:30:b2 (RSA)
|_  256 cf:c3:8c:31:d7:47:7c:84:e2:d2:16:31:b2:8e:63:a7 (ECDSA)
80/tcp  open  http       Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Hack me if you can
143/tcp open  imap       Dovecot imapd
|_imap-capabilities: LOGIN-REFERRALS OK Pre-login more have listed post-login SASL-IR LITERAL+ ENABLE LOGINDISABLEDA0001 IMAP4rev1 ID IDLE capabilities STARTTLS
|_ssl-date: 2023-08-12T12:57:53+00:00; +8s from scanner time.
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
993/tcp open  ssl/imaps?
|_ssl-date: 2023-08-12T12:57:53+00:00; +8s from scanner time.
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### FTP:21

Don't find any exploit.

```bash
Anonymous connection closed:
|_ftp-anon: got code 500 "OOPS: vsftpd: refusing to run with writable root inside chroot()".
```

- [Good exploit of ftp](https://medium.com/@kubotortech/pentesting-exploiting-ftp-cba8ec81968e)

### SSH:22

?

### HTTP:80

Google: 192.168.1.119:80

[Writeup exploit http connection port 80](/writeup_http.md)

![website img](/README/hackme.png)

### IMAP:143

?

### SSL/HHTP:443

?

### SSL/IMAPS:993

?
