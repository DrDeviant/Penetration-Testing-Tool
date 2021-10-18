# Penetration Testing Tool
Pentest Tool is a network and pentest utility that I developed so that I could perform different kinds of task using the same suite, instead of jumping from one tool to another.

Currently, this script can perform a good variety of tasks such as:

Port scans, including SYN, TCP, UDP, ACK, comprehensive scan;
Host discovery (scan for up devices on a local network);
MAC address detection (get MAC address of a host IP on a local network);
Banner grabbing;
DNS checks with geolocation information;
Subdomain enumeration;
Vulnerability reconnaissance;
ifconfig (beta);
ping;
traceroute;
IP spoofing;
Packet sniffing;
Deauth attack.
Other features are still being implemented. Future implementations may include WAF (web application firewall) detection, DNS enumeration, static code analysis, traffic analysis, ARP poisoning, MAC spoofing, MAC flooding, ping of death, network disassociation attack (not deauth attack), OSINT, exploits, some automated tasks, Windows support and others.

# Contents
# Installation
Note that currently, this script can only run well on Linux. If you try it in on Windows or macOS, it may run, but numerous errors will appear. It will have Windows support anytime in the future.
## Linux
To install the necessary packages so that the script can run without any problems simply run the setup.sh script with root privileges. Currently, this installation script is only supported on Debian, Red Hat and Arch based distros that has the apt, dnf and pacman package manager respectively (Ubuntu, Kali Linux, Parrot OS, Debian, Pop!_OS, Linux Mint, Deepin, Zorin OS, MX Linux, Elementary OS, Fedora, CentOS, Red Hat Enterprise Linux, Rocky Linux, AlmaLinux, Oracle Linux, ClearOS, Arch, Black Arch, Manjaro etc). On most systems, to install pentest tool simply run the following commands:

`https://github.com/PhanindraSaiBollineni/Penetration-Testing-Tool.git`

`cd medsec`

`sudo . setup.sh`
***
# How to use
## Port scans
Scanning ports helps detect potential security breaches by identifying the hosts connected to your network and the services running.

Multiple scan types are supported, including SYN  (`-scansyn`) , TCP (`-scantcp`) ,UDP (`-scanudp`) , ACK (`-scanack`) and comprehensive scan (`-scan`).

`-scan -host [HOST(s)]`

`-scan -host [HOST(s)] -p [PORT(s)]`

`-scan -host [HOST(s)] -prange [START PORT] [END PORT]`

`-scan -iprange [START IP] [END IP] -p [PORT(s)]`

`-scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

