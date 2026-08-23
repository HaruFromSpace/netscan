# netscan

netscan is a Python port scanner that is fast and multi-threaded but it is dirty.

In cases like this nmap may be excessive.. You may simply want to know what is open on a host without hanging around. I wanted to get it done ASAP, which is why I created netscan.

## Usage

```bash
python netscan.py 127.0.0.1
```

## Options

arguments:

target                target IP or hostname

options:

-h --help            show this help message and exit

A thread is an individual copy of a program. A thread is an instance of a program.

The number of threads (default 100).

Ports.-p PORTS, --ports PORTS

ports 1, to N (default: 1024)

--timeout=TIMEOUT socket time-out (default: 0.5s)

## Example

```
$ python netscan.py 192.168.1.1 -t 200 -p 5000

[] scanning 192.168.1.1 (1-5000) with 200 threads...

[] Scan finished in 2.14 seconds

[+] OPEN PORTS:

-> 22

-> 80

-> 443
```
