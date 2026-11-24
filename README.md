# OpsPilot

OpsPilot is a personal infrastructure diagnostics learning project built to develop practical skills in Python, networking, APIs, Linux, cloud, automation, DevOps, and SRE.

The project grows incrementally, with each phase adding a new capability while reinforcing previous concepts.

## Progress

### Phase 0 - Engineering Workspace ✅

- Python virtual environment
- Git and GitHub workflow
- `.gitignore`
- `requirements.txt`
- Project structure
- Multi-PC development workflow

### Phase 1 - Python and CLI Foundation ✅

- Variables and data types
- Input and validation
- Functions and return values
- Lists, dictionaries, and loops
- Exception handling
- Modules and imports
- Exit codes

### Phase 2 - Network Diagnostics ✅

- IPv4, subnet, gateway, and routing fundamentals
- DNS resolution
- ICMP and ping
- TCP and ports
- Python sockets
- Connection states and timeouts
- Structured diagnostic results

### Phase 3 - Configuration and Data ✅

- JSON configuration
- File handling and parsing
- Multiple targets
- Configuration validation
- Failure isolation
- Results collection
- Run summaries

### Phase 4 - HTTP and REST API Checks ✅

- HTTP and HTTPS fundamentals
- URLs
- HTTP requests and responses
- Status codes
- Headers and response bodies
- API and REST API fundamentals
- Manual HTTP testing with curl
- Python HTTP requests
- HTTP timeout/error handling
- JSON API responses
- HTTP health classification
- Layered application diagnostics

## Current Architecture

```text
config.json
    ↓
config.py
    ↓
main.py
   ├── validation.py
   ├── network.py
   └── http_check.py
```

### Responsibilities

```text
config.json
→ configured diagnostic targets

config.py
→ loads and parses configuration

main.py
→ orchestrates the diagnostic workflow

validation.py
→ validates and normalizes target data

network.py
→ DNS and TCP diagnostics

http_check.py
→ HTTP requests and health classification
```

## Current Diagnostic Flow

```text
Target
  ↓
Validation
  ↓
DNS Resolution
  ↓
IPv4 Address
  ↓
TCP Connection
  ↓
HTTP/HTTPS Request
  ↓
Status Code
  ↓
HTTP Health
  ↓
Diagnostic Result
  ↓
Run Summary
```

Example:

```text
DNS: PASS
TCP: CONNECTED
HTTP Status: 200
HTTP Health: HEALTHY
Status: SUCCESS
```

OpsPilot reports each layer separately instead of simply reporting a target as working or broken.

## Run

```cmd
.venv\Scripts\activate
python src\main.py
```

Run from the project root so OpsPilot can locate `config.json`.

## Exit Codes

```text
0 = all configured targets succeeded
1 = one or more configuration or diagnostic failures
```

## Learning Status

Phases 0-4 are complete.

Some concepts still require reinforcement through continued development:

- parameters, arguments, and return values
- `continue` versus `return`
- lists of dictionaries
- JSON type mapping and parsing
- routing and default gateway terminology
- TCP listening versus connected
- API versus REST API
- `HTTPError` versus `URLError`
- HTTP result versus HTTP health
- layered DNS → TCP → HTTP troubleshooting

These are not blockers for the next phase. They will continue to be reinforced as OpsPilot grows.