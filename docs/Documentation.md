# OpsPilot Learning Notes

## Phase 0: Engineering Workspace ✅

### Virtual environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

```text
.venv
→ isolated Python environment

pip
→ installs Python packages

requirements.txt
→ records required dependencies
```

### Git workflow

```text
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Local Repository
      ↓ git push
GitHub
```

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
Before switching PCs     → commit and push
```

---

## Phase 1: Python and CLI Foundation ✅

### Function data flow

```text
Argument
   ↓
Parameter
   ↓
Function logic
   ↓
Return value
```

```text
print()
→ communicates with the user

return
→ sends a value to the caller

sys.exit()
→ sends the final status to the operating system
```

### Collections

```text
List
→ multiple items
→ accessed by index

Dictionary
→ key/value data
→ accessed by key

for loop
→ processes every item
```

### Exceptions and validation

```text
Exception
→ operation could not be completed

Validation failure
→ value was understood but rejected by program rules
```

```python
try:
    ...
except ValueError:
    ...
```

### Modules

```text
main.py
→ orchestration

validation.py
→ input validation
```

---

## Phase 2: Network Diagnostics ✅

### Network basics

```text
IPv4 address
→ address assigned to a network interface

Subnet/CIDR
→ helps determine which destinations are local

Routing table
→ directions for network traffic

Default gateway
→ next-hop router used by the default route

Router
→ forwards traffic between networks
```

### Diagnostic layers

```text
Hostname
   ↓
DNS
   ↓
IPv4 address
   ↓
TCP connection
   ↓
Port
   ↓
Application layer later
```

```text
nslookup
→ DNS resolution

ping
→ ICMP Echo Request/Reply

route print
→ routing information

Test-NetConnection
→ TCP connection attempt
```

### TCP results

```text
CONNECTED
→ TCP connection established

REFUSED
→ connection attempt was refused

TIMEOUT
→ connection did not complete within the timeout

ERROR
→ another OS/network failure
```

### Python sockets

```text
AF_INET
→ IPv4

SOCK_STREAM
→ TCP
```

```text
Create socket
    ↓
Set timeout
    ↓
Connect
    ↓
Handle result
    ↓
Close socket
```

### Network functions

```text
resolve_host(host)
→ returns IPv4 address or None

check_tcp(ip_address, port)
→ returns CONNECTED, REFUSED, TIMEOUT, or ERROR
```

Important:

```text
DNS success does not prove TCP works.

TCP success does not prove the application is healthy.
```

---

## Phase 3: Configuration and JSON ✅

### Code versus configuration

```text
Code
→ how OpsPilot works

Configuration
→ which targets OpsPilot diagnoses
```

### JSON mapping

```text
JSON object  → Python dict
JSON array   → Python list
JSON string  → Python str
JSON number  → Python int/float
JSON boolean → Python bool
JSON null    → Python None
```

### File loading

```python
with open("config.json", "r") as file:
    config = json.load(file)
```

```text
open()
→ opens the file

with
→ manages and closes the file

json.load()
→ parses JSON into Python data
```

### Current flow

```text
config.json
    ↓
load_config()
    ↓
config dictionary
    ↓
targets list
    ↓
for target in targets
    ↓
run_diagnostics(target)
    ↓
diagnostic dictionary
    ↓
results.append(diagnostics)
    ↓
run summary
```

### Failure handling

```text
Missing config file
→ stop entire run

Broken JSON
→ stop entire run

Empty/invalid targets list
→ stop entire run

One invalid target
→ record failure
→ continue to remaining targets
```

### `continue` versus `return`

```text
continue
→ skip the current loop iteration
→ process the next target

return
→ leave the entire function
```

### Results

```text
results
→ list of diagnostic dictionaries

all_successful
→ True only if every target succeeded
```

Example summary:

```text
Total: 3
Successful: 2
Failed: 1
```

---

# Topics to Reinforce

Phases 0–3 are complete, but these should be reviewed during future development.

## Python

- argument versus parameter
- `print()` versus `return`
- values returned by nested functions
- local versus global scope
- indentation and block structure
- `continue` versus `return`
- updating dictionaries
- lists of dictionaries
- state tracking across loops
- `results.append(diagnostics)`

## JSON and Configuration

- JSON object versus array
- Python `dict` versus `list`
- parsing with `json.load()`
- valid JSON versus valid OpsPilot configuration
- file-level failure versus individual-target failure

## Networking

- subnet and CIDR boundaries
- routing table versus default gateway
- router terminology
- listening versus connected
- TCP three-way handshake
- DNS failure versus TCP failure
- TCP success versus application health
- socket as a program's interface to OS networking

## Git

- continue using the normal pull, inspect, stage, commit, and push workflow
- branches, merge conflicts, and pull requests remain future topics

---

# Progress

```text
Phase 0: Engineering Workspace                  ✅
Phase 1: Python and CLI Foundation              ✅
Phase 2: Network Diagnostics                    ✅
Phase 3: JSON and Multi-Target Configuration    ✅
Next Phase                                      NEXT
```

Completion means the concepts were implemented successfully. It does not mean every concept is permanently mastered. The review list should be reinforced through continued OpsPilot development.