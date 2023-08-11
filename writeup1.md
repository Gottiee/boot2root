## Find ip address of BornToSeeHackMe 

Scan lan network:

nmap -sn 192.168.1.0/24
Nmap scan report for BornToSecHackMe (192.168.1.119)
Host is up (0.00076s latency).

ping 192.168.1.146
64 bytes from 192.168.1.146: icmp_seq=1 ttl=64 time=163 ms
4 packets transmitted, 4 received, 0% packet loss, time 3020ms


## Ssh Brut Force attack

### Scan with nmap

To determine if ssh is running and the ssh port, I can run nmap on the ip address:

nmap 192.168.1.119
Nmap scan report for BornToSecHackMe (192.168.1.119)
Host is up (0.00024s latency).
Not shown: 994 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps

As we can see, shh running on port 22.

### Hydra

