Here is your **same content**, **properly arranged**, **properly formatted**, and **without changing anything** in your steps or wording:

---

# **Q1 — Applying CI/CD Principles to Web Development Using Jenkins & Git**

---

# **STEP 1 — Install Jenkins & Apache in AWS**

### **1. Login into AWS account**

### **2. Search EC2 > EC2**

### **3. Click Instance**

### **4. Click on Launch Instance**

### **5. Add Name (example)**

### **6. Select Ubuntu**

### **7. Create new key pair**

* Give the name
* Check the location of download of key pair

### **8. In Network Settings tab**

1. Edit
2. Add subnet Random
3. Auto-assign public IP – enable
4. Add security group rule

   * Type: custom TCP
     Port range: 8080
     Source Type: anywhere
   * Type: HTTP
     Port range: 80
     Source Type: anywhere

### **9. Go back Instances panel**

### **10. Click Instance ID**

### **11. Click Connect > click SSH Client**

### **12. Go to folder download location of key pair**

Open Terminal → paste:

```
ssh -i "siddhi.pem" ubuntu@ec2-13-202-78-235.ap-south-1.compute.amazonaws.com
```

### **13. Go to Chrome > search Jenkins Download > click first link > click Ubuntu**

### **14. Copy Installation of Java**

```
sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version
```

### **15. Long Term Support release**

```
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install Jenkins
```

### **16. Start Jenkins**

```
sudo systemctl enable Jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

In Terminal press:
**Ctrl + C**

### **17. Install Apache**

```
sudo apt install apache2 -y
sudo systemctl status apache2
sudo systemctl start apache2
```

### **18. Go to EC2 Instance Connect**

Copy **Public IPv4 address**
Example: **13.202.78.235**

### **19. New tab in Chrome > paste**

```
13.202.78.235:8080
```

### **20. If it asks for admin password**

There is a red line showing location of admin password:
`Var/lib/jenkins/Adminpassword`

### **21. Go to terminal > type**

```
sudo cat Var/lib/jenkins/Adminpassword
```

### **23. Copy the text**

Example: **uye8qw7129383**

### **24. Paste it as admin password**

### **25. Click Install Suggested Plugins**

### **26. Add your username, password, name, and email ID**

---

# **STEP 2 — Create Personal Token & Webhook in GitHub**

### **Personal Token in GitHub**

1. Log into GitHub
2. Right top corner → Click Profile → Settings
3. At bottom of settings → Developer settings
4. Personal token → Token (classic) → Generate new token → Token (classic)
5. Select first: **Repo**
6. Generate and copy the personal token and save it

---

### **Webhook in GitHub**

7. Create a new repository
8. Add `index.html` or download an HTML website from Chrome
9. Go to repository
10. Select repository settings
11. Left side click Webhook
12. Top right → Add WebHook
13. In **Payload URL** paste Jenkins URL

```
http://65.1.121.140:8080/
```

Add in front:

```
http://65.1.121.140:8080/github-webhook/
```

14. Under “Which events would you like to trigger this webhook?”
    Select **Send me everything**

15. Add WebHook

---

# **STEP 3 — Deploy the Website**

### **1. Go to Jenkins**

```
http://65.1.121.140:8080
```

### **2. Click Create New Item / Create a Job**

### **3. Add name example or project**

### **4. Select Freestyle Project**

### **5. In Source Code Management → Select Git**

### **6. Enter Repository URL**

```
https://github.com/SiddhiIngale/jenkins
```

### **7. Credentials → + Add → Jenkins**

### **8. Kind → Secret Text**

* In Secret: paste personal token
* ID: example or project
* Add

### **9. Branch to build**

Change:

```
*/master → */main
```

### **10. Trigger**

Select:

```
GitHub hook trigger for GITScm polling
```

### **11. Build Step → Execute Shell**

### **12. Add shell code**

```
echo "Deploying website..."
rm -rf /var/www/html/*
cp -r * /var/www/html/
echo "✅ Deployment Complete"
```

### **13. Save**

### **14. Click Build Now**

### **15. Check builds at the bottom**

### **16. If Red (error) add this code in terminal:**

```
sudo chown -R jenkins:jenkins "/var/www/html"
```

### **17. Again Build Now**

### **18. Open your public IP**

```
http://65.1.121.140
```

### **19. You will see your website 🎉**

---


