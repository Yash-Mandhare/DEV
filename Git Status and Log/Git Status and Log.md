

---

# **Q1. Create a simple project and use Git commands to check status, view logs, see differences, make commits, and display commit history**

---

# **1. Create a folder**

Make any folder name you like.

---

# **2. Create a Python file**

Inside the folder, create a file named **calculator.py** with a simple add & subtract program.

---

# **3. Check Git Bash**

Make sure Git Bash is installed on your system.

---

# **4. Open Git Bash**

Right-click inside the folder → **Show more options** → **Open Git Bash here**.

---

# **5. Initialize Git repository**

```
git init
```

---

# **6. Check Git status**

```
git status
```

This will show the folder as empty or **calculator.py** in red (untracked).

---

# **7. Add file to staging area**

```
git add calculator.py
```

---

# **8. Commit with a descriptive message**

```
git commit -m "Initial commit: add simple calculator with add and subtract functions and CLI"
```

---

# **9. Check status and log**

```
git status
git log --oneline
```

---

# **10. Add new code (multiply function)**

Add this inside **calculator.py**:

```
def multiply(a, b):
    return a * b
```

---

# **11. Add file again after changes**

```
git add calculator.py
```

---

# **12. Commit the update**

```
git commit -m "Add multiply feature and update CLI menu"
```

---

# **13. View the last commit**

```
git log -1
```

---

# **14. View all commits in chronological order**

```
git log --oneline
```

---

