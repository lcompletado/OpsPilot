# OpsPilot

OpsPilot is a personal learning project for building practical skills in Python, networking, Linux, Git, cloud, automation, and infrastructure troubleshooting.

The project grows incrementally while applying clean, production-style engineering practices.

## Progress

### Phase 0 - Engineering Workspace ✅

- Python virtual environment
- Git and GitHub workflow
- `.gitignore`
- `requirements.txt`
- Multi-PC development workflow
- Project structure

### Phase 1 - Python + CLI Foundation ✅

- Python fundamentals
- Input and validation
- Functions and return values
- Lists, dictionaries, and loops
- Exception handling
- Modules and imports
- Exit codes
- Separation of responsibilities

### Phase 2 - Network Diagnostics ✅

- IPv4, subnet, gateway, and routing fundamentals
- DNS resolution
- ICMP and ping
- TCP and ports
- TCP connection states
- Python sockets
- Timeouts and network exceptions
- Structured diagnostic results

## Current Structure

```text
OpsPilot/
├── src/
│   ├── main.py
│   ├── validation.py
│   └── network.py
├── tests/
├── Documentation.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Current Capability

OpsPilot accepts:

```text
Target Name
Target Host
Target Port
```

It then performs:

```text
Input Validation
      ↓
DNS Resolution
      ↓
Resolved IPv4 Address
      ↓
TCP Connection Attempt
      ↓
Diagnostic Result
```

Example:

```text
Target Host: google.com
Target Port: 443

DNS Check: PASS
Resolved IP: <IPv4 address>
TCP Check: CONNECTED
```

Possible TCP results currently include:

```text
CONNECTED
REFUSED
TIMEOUT
ERROR
```

## Modules

```text
main.py
→ CLI and application flow

validation.py
→ input validation and normalization

network.py
→ DNS resolution and TCP diagnostics
```

## Run

```cmd
.venv\Scripts\activate
python src\main.py
```

## Exit Codes

```text
0 = diagnostic succeeded
1 = validation or diagnostic failure
```

## Next

### Phase 3

OpsPilot will continue building on the Python and networking foundation established in Phases 0-2.