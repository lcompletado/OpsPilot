# OpsPilot Learning Notes

# Phase 0 - Engineering Workspace ✅

## Python Environment

```text
.venv
→ isolated Python environment

pip
→ installs packages

requirements.txt
→ records project dependencies
```

## Git Flow

```text
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Local Repository
      ↓ git push
GitHub
```

Common workflow:

```cmd
git pull
git status
git diff
git add <file>
git diff --staged
git commit -m "message"
git push
```

---

# Phase 1 - Python and CLI Foundation ✅

## Function Flow

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
→ communicate with user

return
→ send value to caller

sys.exit()
→ report program status to OS
```

## Data Structures

```text
List
→ multiple items

Dictionary
→ key/value data

List of dictionaries
→ multiple structured objects
```

## Exceptions

```text
try
→ attempt operation

except
→ handle expected failure

finally
→ always run cleanup
```

---

# Phase 2 - Network Diagnostics ✅

## Network Basics

```text
IPv4 address
→ network interface address

Subnet/CIDR
→ determines what is local

Routing table
→ directions for network traffic

Default gateway
→ next hop used by default route

Router
→ forwards traffic between networks
```

## Network Layers

```text
Hostname
   ↓
DNS
   ↓
IP Address
   ↓
TCP
   ↓
Port
```

Useful tools:

```text
nslookup
→ DNS

ping
→ ICMP

route print
→ routing

Test-NetConnection
→ TCP
```

## TCP Results

```text
CONNECTED
REFUSED
TIMEOUT
ERROR
```

Important:

```text
DNS success ≠ TCP success
TCP success ≠ application health
```

## Python Socket

```text
AF_INET
→ IPv4

SOCK_STREAM
→ TCP
```

```text
Create
 ↓
Configure
 ↓
Connect
 ↓
Handle result
 ↓
Close
```

---

# Phase 3 - Configuration and Data ✅

## Code vs Configuration

```text
Code
→ how OpsPilot works

Configuration
→ what OpsPilot operates on
```

## JSON Mapping

```text
JSON object  → Python dict
JSON array   → Python list
JSON string  → Python str
JSON number  → Python int/float
JSON boolean → Python bool
JSON null    → Python None
```

## Loading Configuration

```python
with open("config.json", "r") as file:
    config = json.load(file)
```

```text
open()
→ opens file

with
→ manages resource lifecycle

json.load()
→ parses JSON file into Python data
```

## Multi-Target Flow

```text
config.json
    ↓
targets list
    ↓
for target in targets
    ↓
validate
    ↓
diagnose
    ↓
results.append(diagnostics)
    ↓
run summary
```

## Failure Isolation

```text
Global configuration failure
→ stop run

Individual target failure
→ record failure
→ continue
```

```text
continue
→ next loop iteration

return
→ leave entire function
```

---

# Phase 4 - HTTP and REST API Checks ✅

## HTTP

```text
Client
   ↓ request
Server
   ↓ response
Client
```

OpsPilot currently acts as the HTTP client.

## URL

```text
https://api.example.com:443/health

https
→ scheme

api.example.com
→ hostname

443
→ port

/health
→ path
```

## HTTP Response

```text
Status
→ high-level result

Headers
→ response metadata

Body
→ returned content
```

Example:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"status": "healthy"}
```

## Status Codes

```text
2xx → success
3xx → redirect
4xx → client/request-side response
5xx → server/service-side response
```

OpsPilot classification:

```text
200 → HEALTHY
301 → REDIRECT
404 → CLIENT_ERROR
503 → SERVER_ERROR
```

## API Concepts

```text
API
→ interface for software interaction

REST API
→ web API style using HTTP resources,
  URLs, methods, and responses

HTTP
→ request/response protocol

JSON
→ structured data format
```

Important:

```text
JSON ≠ REST API

application/json
→ response body uses JSON
```

## HTTP Methods

```text
GET
→ retrieve

POST
→ create/submit

PUT
→ replace/update

PATCH
→ partially update

DELETE
→ remove
```

OpsPilot currently mainly uses `GET` because it observes systems rather than modifying them.

## Manual HTTP Check

```cmd
curl.exe -I https://www.google.com/
```

Used to inspect HTTP response status and headers.

## Python HTTP

```text
check_http(url)
→ makes HTTP request
→ handles timeout/errors
→ reads response
→ optionally parses JSON
→ returns structured result
```

Example:

```python
{
    "status_code": 200,
    "result": "SUCCESS",
    "data": None
}
```

## HTTP Errors

```text
HTTPError
→ HTTP response such as 404/503 was received

URLError
→ request failed before a normal HTTP response

TIMEOUT
→ response did not arrive within configured limit
```

## JSON HTTP Body

```text
HTTP response
    ↓
response.read()
    ↓
bytes
    ↓
decode()
    ↓
str
    ↓
json.loads()
    ↓
Python dict/list
```

Remember:

```text
json.load(file)
→ JSON from file

json.loads(text)
→ JSON from string
```

## HTTP Health

```text
HTTP result
→ what happened during the request

HTTP health
→ classification of the response
```

Example:

```text
HTTP Result: SUCCESS
HTTP Status: 200
HTTP Health: HEALTHY
```

## Full Diagnostic Stack

```text
Configuration
     ↓
Validation
     ↓
DNS
     ↓
TCP
     ↓
TLS / HTTPS
     ↓
HTTP
     ↓
Status Code
     ↓
HTTP Health
     ↓
Overall Status
```

Important:

```text
DNS PASS
does not guarantee TCP PASS.

TCP CONNECTED
does not guarantee HTTP HEALTHY.

HTTP failure
does not automatically mean network failure.
```

---

# Reinforcement Checklist

## Phase 0

- [ ] Working directory → staging → commit → push
- [ ] `git diff` vs `git diff --staged`
- [ ] `git clone` vs `git pull`
- [ ] Virtual environment vs dependency

## Phase 1

- [ ] Argument vs parameter
- [ ] `print()` vs `return`
- [ ] Follow values across function calls
- [ ] Local vs global scope
- [ ] List vs dictionary
- [ ] List of dictionaries
- [ ] `continue` vs `return`
- [ ] `try / except / finally`
- [ ] `main()` as orchestrator

## Phase 2

- [ ] Subnet/CIDR boundaries
- [ ] Routing table vs default gateway
- [ ] Router terminology
- [ ] Listening vs connected
- [ ] TCP SYN → SYN-ACK → ACK
- [ ] DNS vs TCP failure
- [ ] Socket lifecycle
- [ ] TCP timeout does not identify root cause

## Phase 3

- [ ] JSON object → `dict`
- [ ] JSON array → `list`
- [ ] `json.load()` and parsing
- [ ] Valid JSON vs valid configuration
- [ ] `continue` vs `return`
- [ ] `results.append(diagnostics)`
- [ ] Tracking state across loops
- [ ] Global vs individual-target failures

## Phase 4

- [ ] API vs REST API
- [ ] HTTP vs HTTPS/TLS
- [ ] PUT vs PATCH
- [ ] Status vs headers vs body
- [ ] `application/json` means JSON content, not REST API
- [ ] `HTTPError` vs `URLError`
- [ ] `check_http()` returns a dictionary
- [ ] HTTP result vs HTTP health
- [ ] `json.load()` vs `json.loads()`
- [ ] DNS → TCP → TLS → HTTP layering
- [ ] TCP CONNECTED ≠ application HEALTHY

---

# Highest-Priority Review

If concepts start feeling fuzzy, review these first:

1. **Argument → Parameter → Logic → Return**
2. **List vs Dictionary vs List of Dictionaries**
3. **`continue` vs `return`**
4. **JSON → Parse → Python structures**
5. **Subnet → Routing → Default Gateway**
6. **DNS → IP → TCP → Port**
7. **Listening vs Connected**
8. **HTTP Request → Response**
9. **Status → Headers → Body**
10. **API vs REST API vs HTTP vs JSON**
11. **DNS ≠ TCP ≠ HTTP**
12. **One successful layer does not prove every higher layer is healthy**

---

# Progress

```text
Phase 0 - Engineering Workspace             ✅
Phase 1 - Python and CLI Foundation         ✅
Phase 2 - Network Diagnostics               ✅
Phase 3 - Configuration and Data            ✅
Phase 4 - HTTP and REST API Checks          ✅
Phase 5 - Linux Systems Diagnostics         NEXT
```

> Passing a phase means the concepts are understood well enough to continue. It does not mean every concept is permanently mastered. Future OpsPilot phases should continue reinforcing earlier concepts through real use.