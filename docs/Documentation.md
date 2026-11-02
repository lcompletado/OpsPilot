# OpsPilot Learning Notes

Personal notes from building OpsPilot.

---

# Phase 0 - Engineering Workspace ✅

## Virtual Environment

`.venv` is an isolated Python environment for OpsPilot.

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Verify:

```cmd
where python
where pip
```

Deactivate:

```cmd
deactivate
```

### Packages and Dependencies

```text
Package
→ reusable Python code

Dependency
→ package required by OpsPilot

pip
→ installs Python packages

requirements.txt
→ lists project dependencies

.venv
→ contains the local Python environment/packages
```

`.venv` is ignored by Git because each machine creates its own.

---

## Git

Main flow:

```text
Working Directory
      ↓ git add
Staging Area
      ↓ git commit
Repository History
      ↓ git push
GitHub
```

Important commands:

```cmd
git status
git diff
git diff --staged
git add <file>
git commit -m "message"
git log --oneline
git pull
git push
```

Undo:

```cmd
git restore <file>
```

Discard unstaged changes.

```cmd
git restore --staged <file>
```

Unstage while keeping changes.

```cmd
git revert <commit>
```

Undo a committed change while preserving history.

### GitHub Workflow

```text
First time on another PC
→ git clone

Before working
→ git pull

After committing
→ git push
```

---

# Phase 1 - Python + CLI Foundation ✅

## Python Basics

Main types:

```text
str   → text
int   → whole number
float → decimal
bool  → True / False
None  → no usable value
```

`input()` always returns a string.

```python
target = input("Enter target: ").strip()
```

---

## Conditions

```python
if
elif
else
```

Useful operators:

```text
==  !=  <  >  <=  >=
and  or  not
```

---

## Functions

Mental model:

```text
Argument
   ↓
Parameter
   ↓
Function Logic
   ↓
Return Value
```

Example:

```python
validate_target(target)
                ↑ argument
```

```python
def validate_target(target):
                    ↑ parameter
```

Remember:

```text
print()
→ show information to user

return
→ send value back to caller
```

---

## Lists, Dictionaries, Loops

List:

```python
targets = ["web01", "web02"]
```

Dictionary:

```python
target = {
    "name": "web01",
    "host": "192.168.1.10",
    "port": 443
}
```

Loop:

```python
for target in targets:
    print(target)
```

```text
List       → multiple items
Dictionary → key/value properties
Loop       → process each item
```

---

## Validation and Exceptions

Port starts as text:

```text
"443"
```

Converted:

```text
443
```

using:

```python
int(port_text)
```

Invalid conversion such as:

```python
int("hello")
```

raises:

```text
ValueError
```

Handled using:

```python
try:
    ...
except ValueError:
    ...
```

Current port validation:

```text
Valid 1-65535 → return integer
Invalid       → return None
```

`validate_target()` returns:

```text
True  → target valid
False → target invalid
```

---

## Modules

Current source structure:

```text
src/
├── main.py
└── validation.py
```

```text
main.py
→ CLI/application flow

validation.py
→ validation logic
```

Import:

```python
from validation import validate_target
```

---

## Current Program Flow

```text
User Input
    ↓
input_target()
    ↓
Target Dictionary
    ↓
validate_target()
    ↓
validate_target_port()
    ↓
True / False
    ↓
main()
    ↓
0 / 1
    ↓
sys.exit()
```

Before successful validation:

```python
"port": "443"
```

After:

```python
"port": 443
```

---

## Exit Codes

```text
0 → success
1 → failure
```

Remember:

```text
print()
→ user

return
→ functions

sys.exit()
→ operating system / automation
```

---

# Progress

```text
Phase 0 - Engineering Workspace       ✅
Phase 1 - Python + CLI Foundation     ✅
Phase 2 - Network Diagnostics         NEXT
```