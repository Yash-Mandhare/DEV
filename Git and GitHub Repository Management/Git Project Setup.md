Here is your content **properly arranged, formatted cleanly, and without making any changes to your original steps**:

---

# **Q1 — Git and GitHub Repository Management**

---

# **Task 1: Repository Setup and Initial Commit**

### **1. Create a Project Folder**

```
mkdir myproject
cd myproject
```

### **2. Create project.md**

```
echo "This is a hypothetical project about Git practice." > project.md
```

### **3. Initialize a Local Git Repository**

```
git init
```

### **4. Check Status**

```
git status
```

### **5. Add project.md to staging**

```
git add project.md
```

### **6. Commit the file**

```
git commit -m "Initial commit: added project.md with project description"
```

### **7. Create an empty GitHub repository**

Example:
**Repository Name: myproject**

### **8. Add GitHub as remote**

```
git remote add origin https://github.com/Yash-Mandhare/myproject.git
```

### **9. Push the commit to GitHub**

```
git branch -M main
git push -u origin main
```

---

# **Task 2: Branching and Merging**

### **10. Create a new branch**

```
git branch feature-branch
```

### **11. Switch to the new branch**

```
git checkout feature-branch
```

### **12. Edit project.md (add more content)**

```
echo "New feature: branch updates added." >> project.md
```

### **13. Add and commit the update**

```
git add project.md
git commit -m "Updated project.md with feature branch modifications"
```

### **14. Switch back to main branch**

```
git checkout main
```

### **15. Merge feature-branch into main**

```
git merge feature-branch
```

### **16. Push merged changes to GitHub**

```
git push origin main
```

---

