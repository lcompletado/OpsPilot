# OpsPilot

OpsPilot is a personal, production-style learning project focused on infrastructure diagnostics, monitoring, automation, cloud operations, and software engineering.

The project starts as a small Python command-line application and will grow through short, working iterations. Each phase introduces technical concepts only when OpsPilot needs them.

## Project Goals

- Build practical skills in Python, Linux, networking, Git, APIs, cloud, DevOps, and SRE concepts.
- Apply professional engineering habits at a realistic personal-project scale.
- Learn through implementation, testing, troubleshooting, documentation, and iteration.
- Produce a portfolio project that can be explained clearly during interviews.

## Current Status

**Phase 0: Engineering Workspace — Complete**

Completed topics:

- Initial project structure
- Python virtual environment
- Package and dependency fundamentals
- Git repository initialization
- Working directory and staging area
- Commits and commit history
- Inspecting staged and unstaged changes
- Restoring and unstaging changes
- Reverting a committed change
- Git identity and configuration
- Basic dependency reproducibility
- First Python source file

Current application output:

```text
OpsPilot is running.
```

## Current Project Structure

```text
opspilot/
├── .venv/              # Local Python virtual environment; ignored by Git
├── src/
│   └── main.py         # Current OpsPilot entry point
├── tests/              # Automated tests will be added later
├── Documentation.md    # Personal learning notes
├── README.md           # Project-facing documentation
├── requirements.txt    # Python dependencies; currently empty
├── .gitignore          # Files and folders Git should ignore
└── .git/               # Local Git repository metadata and history
```

## Requirements

- Python
- Git
- Windows Command Prompt or PowerShell
- Visual Studio Code, recommended

No third-party Python package is required yet.

## Local Setup

From the project root, create a virtual environment if one does not already exist:

```cmd
python -m venv .venv
```

Activate the environment in Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

Verify that the environment's Python and pip are being used:

```cmd
where python
where pip
```

The first result should point inside:

```text
opspilot\.venv\Scripts\
```

## Run OpsPilot

From the project root:

```cmd
python src\main.py
```

Expected output:

```text
OpsPilot is running.
```

## Dependencies

`requirements.txt` records the third-party Python dependencies needed by OpsPilot.

The file is currently empty because OpsPilot does not require any third-party packages yet.

When dependencies exist, a new environment will eventually be recreated using:

```cmd
pip install -r requirements.txt
```

The `.venv` directory is not committed because each machine should create its own local environment.

## Git Workflow

The normal workflow for this project is:

```text
Edit files
    ↓
Inspect repository state
    ↓
Inspect unstaged changes
    ↓
Stage intentional files
    ↓
Inspect staged changes
    ↓
Commit
    ↓
Verify clean state and history
```

Useful commands:

```cmd
git status
git diff
git add <file>
git diff --staged
git commit -m "Meaningful message"
git log --oneline
git log --stat
```

## Learning Method

OpsPilot follows an Agile, project-based learning approach:

```text
Define a small capability
    ↓
Learn the required concepts
    ↓
Practice manually
    ↓
Implement
    ↓
Test success and failure cases
    ↓
Refactor
    ↓
Document
    ↓
Commit
    ↓
Move to the next capability
```

## Next Phase

**Phase 1: Python and CLI Foundation**

The next milestone is to turn the current one-line Python program into a small, understandable command-line application while learning Python fundamentals through actual OpsPilot features.

## Scope Note

OpsPilot aims to use production-style practices without pretending to operate at enterprise scale. The focus is on sound engineering, reproducibility, testing, security, documentation, troubleshooting, and clear technical understanding.