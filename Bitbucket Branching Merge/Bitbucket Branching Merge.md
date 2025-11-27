

---

# **Create a simple project, push it to Bitbucket, create a branch, merge it, and show commit history**

Follow these steps one by one:

---

## **1. Create a Simple Project Locally**

Create a folder and a file inside it:

```bash
mkdir bitbucket-project
cd bitbucket-project
echo "This is my Bitbucket project." > project.txt
```

---

## **2. Initialize a Git Repository**

```bash
git init
```

Check status:

```bash
git status
```

---

## **3. Add and Commit the File**

```bash
git add project.txt
git commit -m "Initial commit: added project.txt"
```

---

## **4. Create an Empty Repository on Bitbucket**

Go to:
👉 [https://bitbucket.org](https://bitbucket.org) → Repositories → Create Repository
Name: **bitbucket-project**
Keep it empty (don’t add README, .gitignore)

Copy the repo URL, example:

```
https://bitbucket.org/your-username/bitbucket-project.git
```

---

## **5. Add Bitbucket as Remote and Push**

```bash
git remote add origin https://bitbucket.org/your-username/bitbucket-project.git
git branch -M main
git push -u origin main
```

---

## **6. Create a New Branch**

Create a new branch:

```bash
git branch feature-branch
```

Switch to it:

```bash
git checkout feature-branch
```

---

## **7. Make Changes in the New Branch**

Modify the file:

```bash
echo "Added a new feature update." >> project.txt
```

Stage and commit:

```bash
git add project.txt
git commit -m "Added feature update in project.txt"
```

Push the branch:

```bash
git push origin feature-branch
```

---

## **8. Merge the Branch into Main (Locally)**

Switch to main:

```bash
git checkout main
```

Merge:

```bash
git merge feature-branch
```

Push merged code to Bitbucket:

```bash
git push origin main
```

---

## **9. Display Commit History (Chronological)**

Compact view:

```bash
git log --oneline
```

Full view:

```bash
git log
```

---

## **10. Pull Latest Changes (If Needed)**

```bash
git pull origin main
```

---


