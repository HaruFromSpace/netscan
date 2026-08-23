#!/usr/bin/env python3
"""
quick and dirty threaded port scanner. 
wrote this because nmap is sometimes too loud/slow for quick local checks.
"""
import socket
import threading
import time
import argparse
from queue import Queue

# TODO: add udp scanning later
# TODO: maybe add banner grabbing if I get bored

def worker(target, q, open_ports, timeout):
    while not q.empty():
        port = q.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            # 0 means success
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
            s.close()
        except Exception:
            pass # whatever, just skip it
        finally:
            q.task_done()

def main():
    parser = argparse.ArgumentParser(description="fast threaded port scanner")
    parser.add_argument("target", help="target IP or hostname")
    parser.add_argument("-t", "--threads", type=int, default=100, help="number of threads (default: 100)")
    parser.add_argument("-p", "--ports", type=int, default=1024, help="scan ports 1 to N (default: 1024)")
    parser.add_argument("--timeout", type=float, default=0.5, help="socket timeout (default: 0.5s)")
    
    args = parser.parse_args()

    print(f"[*] scanning {args.target} (1-{args.ports}) with {args.threads} threads...")
    start_time = time.time()
    
    q = Queue()
    open_ports = []
    
    for port in range(1, args.ports + 1):
        q.put(port)
        
    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(args.target, q, open_ports, args.timeout))
        t.daemon = True
        t.start()
        threads.append(t)
        
    q.join()
    end_time = time.time()
    
    print(f"[*] scan finished in {end_time - start_time:.2f} seconds")
    
    if open_ports:
        print("\n[+] OPEN PORTS:")
        for p in sorted(open_ports):
            print(f"  -> {p}")
    else:
        print("\n[-] no ports open.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] cancelled by user.")
