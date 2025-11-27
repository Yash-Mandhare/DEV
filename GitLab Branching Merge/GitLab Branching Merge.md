Here is your answer **properly arranged, formatted clearly, and without changing any of your original steps or wording**:

---

# **Q1. Create a simple project, push to GitLab, create a branch, merge it, view commit history, and pull changes locally**

---

# **1. Create a Simple Project Locally**

Create a folder
Create a simple file:

```
echo "This is my GitLab project." > project.text
```

---

# **2. Initialize a Local Git Repository**

```
git init
```

Check status:

```
git status
```

---

# **3. Add and Commit the File**

```
git add project.md
git commit -m "Initial commit: added project.md"
```

---

# **4. Create a New Empty Repository on GitLab**

Go to: [https://gitlab.com](https://gitlab.com) → **New Project** →
Name: **gitlab-project** (empty)

Copy the repository URL, e.g.:

```
https://gitlab.com/your-username/gitlab-project.git
```

---

# **5. Add GitLab as Remote & Push**

```
git remote add origin https://gitlab.com/your-username/gitlab-project.git
git branch -M main
git push -u origin main
```

---

# **6. Create a New Branch**

```
git branch feature-branch
```

Switch to the new branch:

```
git checkout feature-branch
```

---

# **7. Make Changes in the New Branch**

```
echo "Update: Added a new feature." >> project.txt
```

Stage & commit:

```
git add project.md
git commit -m "Feature update added to project.md"
```

Push the branch:

```
git push origin feature-branch
```

---

# **8. Merge feature-branch into main (using local)**

Switch back to main:

```
git checkout main
```

Merge:

```
git merge feature-branch
```

Push merged result to GitLab:

```
git push origin main
```

---

# **9. Display Commit History (Chronological)**

Short one-line format:

```
git log --oneline
```

---

# **10. Pull Changes to Local Machine**

```
git pull origin main
```

---

