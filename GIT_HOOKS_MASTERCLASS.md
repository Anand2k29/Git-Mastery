# 🪝 Git Hooks: The Ultimate Masterclass

Welcome to the hidden engine room of Git. If you want to automate your workflow, enforce code quality, or just make Git do cool things automatically, you need to understand Git Hooks.

## 🧠 What is a Git Hook?
A Git Hook is simply a custom script that Git automatically runs **before** or **after** an event happens (like committing, pushing, or merging). 

Think of them as invisible bouncers at a club. Before Git lets a commit into the history, the bouncer (the hook) checks the commit. If the hook throws an error, the commit is rejected.

---

## 📍 Where Do They Live?
Every Git repository has a hidden folder called `.git`. This is Git's brain. 
Inside that folder is a subfolder called `hooks`.

**Path:** `your-project/.git/hooks/`

If you look in that folder right now, you will see a bunch of files ending in `.sample` (e.g., `pre-commit.sample`). Git generates these automatically to show you how they work. To activate one, you just delete the `.sample` extension.

### ⚠️ The Golden Rule of Hooks
**Hooks are completely local.** Because the `.git` folder is never uploaded to GitHub, your hooks stay on your computer. If your friend clones your repository, they **do not** get your hooks automatically. 

*(Note: Senior teams solve this by using tools like `Husky` (for Node.js) or `pre-commit` (for Python) to manage and share hooks across a team).*

---

## ⚙️ How to Create a Hook

1. **Navigate to the folder:** `cd .git/hooks`
2. **Create a file:** Name it exactly after the Git event you want to trigger (e.g., `pre-commit` or `commit-msg`). **Do not add an extension like .py or .sh.**
3. **Write the script:** You can write hooks in Python, Bash, Ruby, or Node.js. Just make sure the very first line tells the computer what language to use (e.g., `#!/usr/bin/env python3`).
4. **Make it executable (Mac/Linux only):** If you are on Mac or Linux, you must run `chmod +x .git/hooks/<hook-name>` in the terminal to give your computer permission to run it. Windows does this automatically.

---



## 🔄 The 4 Most Important Hooks

### 1. `pre-commit`
* **When it runs:** The exact second you type `git commit`, but *before* you even type your message.
* **What it’s used for:** Checking the code itself. Did you leave debugging `print()` statements in? Does the code format correctly? If this script fails, the commit is aborted.

### 2. `commit-msg`
* **When it runs:** After you type your message, but before the commit is finalized.
* **What it’s used for:** Enforcing rules on your message. (e.g., Making sure it's longer than 10 characters, or ensuring it includes a Jira ticket number like "PROJ-123: Fixed login").

### 3. `post-commit`
* **When it runs:** Immediately *after* the commit is successfully saved.
* **What it’s used for:** Notifications. It cannot abort the commit because it already happened. It is used to trigger an email, send a Slack message saying "Anand just committed code!", or back up files.

### 4. `pre-push`
* **When it runs:** When you type `git push`, right before the code is sent to GitHub.
* **What it’s used for:** Running heavy, time-consuming automated tests. You don't want to run massive tests on every single local commit, but you *definitely* want to run them before uploading broken code to the team's server.

---

## 🚪 The Escape Hatch: Bypassing Hooks

Sometimes, production is on fire. You have a hook that requires 10 minutes of testing, but you just need to push a 1-line typo fix right now. 

You can tell Git to completely ignore the `pre-commit` and `commit-msg` hooks by adding the `--no-verify` flag:

```bash
git commit -m "Emergency fix" --no-verify