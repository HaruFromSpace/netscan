# netscan

A small multi-threaded TCP port scanner in pure Python. Use it when you want to know which ports are open on a machine and nmap feels like too much.

No dependencies beyond the Python standard library.

## Usage

```bash
python netscan.py 192.168.1.10
```

## Options

| Option | What it does | Default |
| --- | --- | --- |
| `target` | IP address or hostname to scan | required |
| `-t`, `--threads` | how many ports to check at the same time | 100 |
| `-p`, `--ports` | scan ports 1 up to this number | 1024 |
| `--timeout` | seconds to wait for each port | 0.5 |

## Example

```
$ python netscan.py 192.168.1.1 -t 200 -p 5000
[*] scanning 192.168.1.1 (1-5000) with 200 threads...
[*] scan finished in 2.14 seconds

[+] OPEN PORTS:
  -> 22
  -> 80
  -> 443
```

Only scan machines you own or have permission to scan.

## Ideas for later

- UDP scanning
- show which service is running on each open port

## License

MIT
