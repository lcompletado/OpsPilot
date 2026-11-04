# OpsPilot Learning Notes

## Phase 0 - Engineering Workspace ✅

### Virtual Environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

```text
.venv
→ isolated Python environment

pip
→ package installer

requirements.txt
→ project dependencies
```

### Git

```text
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Local Repository
      ↓ git push
GitHub
```

Useful workflow:

```cmd
git pull
git status
git diff
git add <file>
git diff --staged
git commit -m "message"
git push
```

```text
First time on another PC → git clone
Before working           → git pull
After committing         → git push
```

---

# Phase 1 - Python + CLI Foundation ✅

### Python Types

```text
str   → text
int   → whole number
float → decimal
bool  → True / False
None  → no usable value
```

`input()` returns a string.

### Functions

```text
Argument
   ↓
Parameter
   ↓
Function Logic
   ↓
Return Value
```

```text
print()
→ communicates with user

return
→ sends value back to caller

sys.exit()
→ sends program status to OS
```

### Collections

```text
List
→ multiple items
→ accessed by index

Dictionary
→ key/value pairs
→ accessed by key

for loop
→ process each item
```

### Exceptions

```python
try:
    ...
except ValueError:
    ...
```

```text
Exception
→ operation could not be completed

Validation failure
→ value is understood but unacceptable
```

### Modules

```text
main.py
→ application flow

validation.py
→ validation logic
```

### Entry Point

```python
if __name__ == "__main__":
    sys.exit(main())
```

```text
0 → success
1 → failure
```

---

# Phase 2 - Network Diagnostics ✅

## Network Basics

```text
IPv4 address
→ address of a network interface

Subnet / CIDR
→ helps determine what destinations are local

Routing table
→ directions for where traffic should go

Default gateway
→ next-hop router used by the default route

Router
→ forwards traffic between networks
```

Example:

```text
PC:      192.168.1.10/24
Gateway: 192.168.1.1

192.168.1.20 → local
192.168.2.20 → non-local
8.8.8.8      → non-local
```

## DNS

```text
Hostname
   ↓
DNS
   ↓
IP address
```

Manual tool:

```cmd
nslookup google.com
```

Python:

```python
socket.gethostbyname(host)
```

OpsPilot:

```text
resolve_host(host)

success → IPv4 address
failure → None
```

DNS success does not prove the application is healthy.

## ICMP

```cmd
ping google.com
```

Uses:

```text
ICMP Echo Request
        ↓
Destination
        ↓
ICMP Echo Reply
```

Ping failure does not automatically mean the server or application is down.

## TCP and Ports

```text
IP address
→ destination address

Port
→ network service endpoint
```

Common associations:

```text
22  → SSH
80  → HTTP
443 → HTTPS
```

A listening TCP service is waiting for incoming connection attempts.

### TCP Handshake

```text
Client              Server

SYN       ──────────►
          ◄───────── SYN-ACK
ACK       ──────────►

TCP established
```

## Manual Tools

```text
ipconfig
→ local network configuration

nslookup
→ DNS resolution

ping
→ ICMP reachability

route print
→ routing information

Test-NetConnection
→ TCP connection test
```

## TCP Results

```text
CONNECTED
→ TCP connection established

REFUSED
→ connection attempt was refused

TIMEOUT
→ connection did not complete within timeout

ERROR
→ other network/OS failure
```

A timeout does not automatically mean a firewall caused the problem.

## Python Socket

```python
socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

```text
AF_INET
→ IPv4

SOCK_STREAM
→ TCP

socket
→ software interface used by the program
  for network communication through the OS
```

Socket lifecycle:

```text
Create
  ↓
Set timeout
  ↓
Connect
  ↓
Handle result
  ↓
Close
```

`finally` ensures the socket closes whether the connection succeeds or fails.

## Current Network Functions

```text
resolve_host(host)
→ hostname to IPv4 address

check_tcp(ip_address, port)
→ TCP connectivity result
```

## Current Architecture

```text
User
 ↓
Input
 ↓
Validation
 ↓
Hostname
 ↓
DNS Resolution
 ↓
IPv4 Address
 ↓
TCP Connection
 ↓
Diagnostic Result
 ↓
Exit Code
```

Current modules:

```text
main.py
→ orchestrates OpsPilot

validation.py
→ validates input

network.py
→ performs DNS and TCP operations
```

## Key Troubleshooting Rule

Do not report:

```text
SERVER WORKING
SERVER BROKEN
```

without enough evidence.

Instead identify the layer:

```text
DNS: PASS / FAILED
TCP: CONNECTED / REFUSED / TIMEOUT / ERROR
```

DNS success does not prove TCP works.

TCP success does not prove the application is healthy.

---

# Progress

```text
Phase 0 - Engineering Workspace       ✅
Phase 1 - Python + CLI Foundation     ✅
Phase 2 - Network Diagnostics         ✅
Phase 3                              NEXT
```