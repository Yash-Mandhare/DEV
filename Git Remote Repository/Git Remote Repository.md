

---

# **Q1. Create a simple project and push on a remote server (GitHub) using Git, perform operations, and display commit history**

---

# **1. Create a GitHub Repository**

Create a GitHub repository named **simplecalculator** (empty).

---

# **2. Open Git Bash**

Right-click inside your desired folder →
**Show more options → Open Git Bash here**

---

# **3. Clone the GitHub repository to local system**

```
git clone https://github.com/Yash-Mandhare/simplecalculator.git
```

---

# **4. Go inside the project folder**

```
cd simplecalculator
```

---

# **5. Create a simple project file**

```
echo "Hello Smile" > example.txt
```

---

# **6. View the file content**

```
cat example.txt
```

---

# **7. Add the file to staging and commit**

```
git add example.txt
git commit -m "Initial commit: added example.txt with sample text"
```

---

# **8. Create a new branch**

```
git branch example2
```

---

# **9. Switch to the new branch**

```
git checkout example2
```

---

# **10. Confirm remote origin (already set automatically after clone)**

```
git remote -v
```

(No need to add origin again because git clone already configures it.)

---

# **11. Modify the file (perform an operation)**

```
echo "Multiplication feature added" >> example.txt
```

---

# **12. Add and commit the update**

```
git add example.txt
git commit -m "Update: added multiplication text to example.txt"
```

---

# **13. Push the branch to GitHub**

```
git push origin example2
```

---

# **14. View the last commit**

```
git log -1
```

---

# **15. View all commits in chronological order (short format)**

```
git log --oneline
```

---

