# OpsPilot Learning Documentation

This file contains personal notes from building OpsPilot. It records the concepts learned, the commands practiced, and the reasoning behind the project structure.

# Phase 0: Engineering Workspace

## Phase Goal

Create and understand a clean local workspace for OpsPilot.

The phase is complete when the project can:

- use its own Python environment;
- run a Python source file;
- track changes using Git;
- distinguish working, staged, and committed changes;
- ignore local generated files;
- explain how dependencies will be recreated on another machine.

---

## Project Structure

```text
opspilot/
├── .venv/
├── src/
│   └── main.py
├── tests/
├── Documentation.md
├── README.md
├── requirements.txt
├── .gitignore
└── .git/
```

### Purpose of Each Item

- `.venv/` — OpsPilot's isolated local Python environment. Installed Python packages for this environment are stored here.
- `src/` — contains the application's source code.
- `src/main.py` — the current entry point of OpsPilot.
- `tests/` — will contain automated tests later.
- `Documentation.md` — personal learning notes.
- `README.md` — explains the project to users, reviewers, and other developers.
- `requirements.txt` — lists the Python dependencies needed to recreate the environment.
- `.gitignore` — tells Git which untracked files or folders should normally be ignored.
- `.git/` — contains the local Git repository's metadata and history.

---

## Virtual Environment

A virtual environment is an isolated Python environment for one project.

OpsPilot uses `.venv` so that its Python packages do not need to be installed into the computer's global Python environment.

### Create the Environment

This is normally done once for a project or when recreating the environment:

```cmd
python -m venv .venv
```

It does not need to be recreated every time OpsPilot is opened.

### Activate the Environment

```cmd
.venv\Scripts\activate
```

Activation tells the current terminal to prioritize the Python and Python tools inside `.venv\Scripts`.

The prompt normally changes to:

```text
(.venv) C:\...\opspilot>
```

The prompt is a useful indicator, but the executable paths can be verified using:

```cmd
where python
where pip
```

The first results should point inside:

```text
opspilot\.venv\Scripts\
```

### Deactivate the Environment

```cmd
deactivate
```

Deactivation stops the current terminal from using the virtual environment. It does not delete `.venv`.

### When to Activate

Activate `.venv` when working on OpsPilot with Python, including:

- running its Python code;
- installing a required Python package;
- running Python-based development tools;
- running tests later.

It is fine to keep `.venv` active while using commands such as `git`, `dir`, or `cd`.

---

## Python, Packages, Dependencies, and pip

### Python

Python is the programming language and runtime used to execute OpsPilot.

### Package

A package is reusable Python software that can be installed and imported.

Examples that may be used later include `pytest`, `requests`, and `FastAPI`.

### Dependency

A dependency is something the project requires in order to work. A Python package becomes an OpsPilot dependency when OpsPilot relies on it.

### pip

`pip` installs Python packages into the selected Python environment.

Example:

```cmd
pip install <package-name>
```

When `.venv` is active, its `pip` installs packages into the OpsPilot environment.

### Installed Packages

List installed packages:

```cmd
pip list
```

Show installed packages in requirements-style format:

```cmd
pip freeze
```

The current OpsPilot environment has no third-party project dependencies, so `pip freeze` may show no output.

---

## requirements.txt and Reproducibility

The actual `.venv` directory is local and is not committed to Git.

Instead, `requirements.txt` records the Python dependencies required by OpsPilot.

Conceptual flow:

```text
Computer A
    ↓
Installed dependencies in .venv
    ↓
pip freeze
    ↓
requirements.txt
    ↓
Git repository
    ↓
Computer B
    ↓
Create a new .venv
    ↓
Activate it
    ↓
pip install -r requirements.txt
    ↓
Dependencies installed into the new environment
```

Install packages listed in a requirements file:

```cmd
pip install -r requirements.txt
```

The file remains empty until OpsPilot genuinely needs a third-party dependency.

---

## .gitignore

The `.gitignore` file contains patterns for untracked files and folders that Git should normally ignore.

Current rule:

```gitignore
.venv/
```

This does not delete `.venv`. It prevents Git from normally treating the local environment as project content to be committed.

Verify the rule:

```cmd
git check-ignore -v .venv/
```

`-v` means verbose. It shows which ignore rule matched and where that rule came from.

The main reasons for ignoring `.venv` are:

- it is generated locally;
- it may contain many files;
- it can be recreated;
- it may contain machine-specific environment files;
- dependency information belongs in `requirements.txt`, not in a committed virtual environment.

---

## Git Repository

Initialize a local Git repository:

```cmd
git init
```

Git creates a hidden `.git/` directory in the project root.

Running `git init` multiple times in the same project does not create several repositories. It reinitializes the repository represented by the same `.git/` directory.

Different folders with their own `.git/` directories are separate repositories.

Git and GitHub are not the same:

- Git is the version-control system used locally.
- GitHub is a remote hosting and collaboration platform that may be introduced later.

---

## Git's Three Main States

```text
Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Repository History
```

### Working Directory

The working directory contains the actual project files currently being edited on disk.

### Staging Area

The staging area contains the selected changes intended for the next commit.

### Commit

A commit is a recorded snapshot of the staged changes in repository history.

---

## Inspecting Git

### Overall Repository State

```cmd
git status
```

This reports the current branch and identifies staged, unstaged, and untracked changes. A clean result includes:

```text
nothing to commit, working tree clean
```

### Inspect Unstaged Changes

```cmd
git diff
```

This compares the working directory with the staging area.

Question answered:

> What did I change but not stage?

### Inspect Staged Changes

```cmd
git diff --staged
```

This compares the staging area with the last commit.

Question answered:

> What is prepared for my next commit?

### Inspect History

```cmd
git log
git log --oneline
git log --stat
```

- `git log` shows detailed commit history.
- `git log --oneline` shows a compact history.
- `git log --stat` shows commit details and file-change statistics.

A commit has a SHA or hash, author information, date, and commit message.

---

## Normal Git Workflow

```text
Edit
  ↓
git status
  ↓
git diff
  ↓
git add <specific-file>
  ↓
git diff --staged
  ↓
git commit
  ↓
git status
  ↓
git log
```

Stage one intentional file:

```cmd
git add README.md
```

Commit staged changes:

```cmd
git commit -m "Document OpsPilot project purpose"
```

Prefer commit messages that explain the meaningful change rather than only naming a file.

`git add .` stages relevant changes under the current directory, while respecting ignore rules for normally ignored untracked content. It should be used only when all included changes are intentionally part of the next commit.

---

## Undoing Uncommitted Changes

### Discard an Unstaged Change

```cmd
git restore <file>
```

This restores the file from the last committed version and discards the current unstaged edit.

Inspect first:

```cmd
git diff
```

### Unstage While Keeping the Edit

```cmd
git restore --staged <file>
```

This removes the change from the staging area but keeps the edited content in the working directory.

### Completely Discard a Staged Change

First unstage it:

```cmd
git restore --staged <file>
```

Then discard the unstaged edit:

```cmd
git restore <file>
```

Conceptually:

```text
Staged
   ↓ git restore --staged
Unstaged
   ↓ git restore
Discarded
```

---

## Reverting a Committed Change

`git revert` creates a new commit containing changes that reverse an earlier commit.

It does not delete the original commit or create a new file automatically.

```text
A → B → C
        ↑
   unwanted commit

A → B → C → D
            ↑
       revert commit
```

This preserves a traceable history.

General form:

```cmd
git revert <commit-sha>
```

---

## Git Identity and Configuration

Git records author information in commits.

View the current configured identity:

```cmd
git config user.name
git config user.email
```

View configuration entries, scopes, and source files:

```cmd
git config --list --show-origin --show-scope
```

Important scopes:

- `global` — applies generally to repositories used by the account.
- `local` — applies only to the current repository and can override the corresponding global value.

---

## First OpsPilot Program

Current source file:

```text
src/main.py
```

Current code:

```python
print("OpsPilot is running.")
```

Run from the project root:

```cmd
python src\main.py
```

Expected output:

```text
OpsPilot is running.
```

The source can also be run as `python main.py` when the terminal is already inside `src`, but using the project root provides a consistent starting location.

---

## Phase 0 Workspace Health Check

From a fresh terminal:

1. Enter the project directory.
2. Activate `.venv`.
3. Verify `python` and `pip` paths.
4. Run `src/main.py`.
5. Verify Git status.
6. Verify `.venv` is ignored.
7. Inspect commit history.

Useful commands:

```cmd
cd <path-to-opspilot>
.venv\Scripts\activate
where python
where pip
python src\main.py
git status
git check-ignore -v .venv/
git log --oneline
```

---

## Phase 0 Lessons Learned

- A virtual environment isolates a project's Python setup.
- Activation changes which Python and pip the current terminal finds first.
- Packages are reusable Python software.
- Dependencies are packages or components the project requires.
- pip installs Python packages.
- `.venv` contains the local Python environment and installed packages.
- `requirements.txt` records dependencies needed to recreate the environment.
- `.gitignore` prevents generated local content from being normally tracked.
- Git tracks project history locally.
- The working directory contains the files being edited.
- The staging area contains changes selected for the next commit.
- A commit records staged changes in history.
- `git diff` shows unstaged changes.
- `git diff --staged` shows staged changes.
- `git restore --staged` unstages while keeping edits.
- `git restore` discards unstaged edits.
- `git revert` creates a new commit that reverses an earlier commit.
- The workspace can now run OpsPilot through the project virtual environment.

---

## Phase 0 Status

**Complete**

Next phase:

```text
Phase 1: Python and CLI Foundation
```