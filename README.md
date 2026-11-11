# OpsPilot

OpsPilot is a personal learning project for developing practical skills in Python, networking, Git, configuration, automation, and infrastructure troubleshooting.

The project is built incrementally. Each phase adds a working capability while reinforcing clean code, troubleshooting, and production-style engineering habits.

## Progress

### Phase 0: Engineering Workspace ✅

- Python virtual environment
- Git and GitHub workflow
- `.gitignore` and `requirements.txt`
- Multi-PC development workflow
- Project structure and reproducibility

### Phase 1: Python and CLI Foundation ✅

- Variables and data types
- Input, conditions, and validation
- Functions, parameters, arguments, and returns
- Lists, dictionaries, and loops
- Exception handling
- Modules, imports, and exit codes

### Phase 2: Network Diagnostics ✅

- IPv4, subnet, gateway, and routing fundamentals
- DNS resolution
- ICMP and ping
- TCP, ports, and listening services
- Python sockets
- TCP results: connected, refused, timeout, and error
- Structured diagnostic results

### Phase 3: JSON Configuration and Multiple Targets ✅

- JSON fundamentals
- Reading and parsing files
- Configuration validation
- Multiple configured targets
- Failure isolation with `continue`
- Results collection and run summaries
- Overall batch exit status

## Current Architecture

```text
config.json
    ↓
config.py
    ↓
main.py
   ├── validation.py
   └── network.py
```

```text
config.json
→ configured targets

config.py
→ loads and parses configuration

main.py
→ orchestrates the diagnostic run

validation.py
→ validates and normalizes target data

network.py
→ performs DNS resolution and TCP checks
```

## Current Capability

OpsPilot can:

1. Load multiple targets from `config.json`.
2. Validate each target.
3. Resolve each hostname to an IPv4 address.
4. Attempt a TCP connection to the configured port.
5. Classify the result.
6. Continue when an individual target fails.
7. Collect and summarize all results.
8. Return an overall exit code.

Possible results include:

```text
SUCCESS
INVALID
FAILED

DNS: PASS / FAILED
TCP: CONNECTED / REFUSED / TIMEOUT / ERROR
```

## Project Structure

```text
OpsPilot/
├── config.json
├── src/
│   ├── main.py
│   ├── config.py
│   ├── validation.py
│   └── network.py
├── tests/
├── Documentation.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Run

```cmd
.venv\Scripts\activate
python src\main.py
```

## Exit Codes

```text
0 = all configured targets succeeded
1 = configuration, validation, DNS, or TCP failure
```

## Current Learning Status

Phases 0–3 are complete, but some concepts still need reinforcement through continued use:

- argument versus parameter
- return values and data flow
- `continue` versus `return`
- lists of dictionaries
- JSON object/array mapping
- tracking state across loops
- subnet, gateway, and routing terminology
- listening versus connected TCP states
- layered DNS, TCP, and application troubleshooting

These are not blockers for the next phase. They should be reviewed naturally while OpsPilot continues to grow.