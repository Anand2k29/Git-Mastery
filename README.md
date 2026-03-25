# 🚀 Git & GitHub Mastery: The Ultimate Revision Guide

Welcome to the complete, workflow-based guide to mastering Git and version control. This repository is designed as a quick-reference cheat sheet and interactive revision tool for developers moving from basic saves to advanced history management.

## 🗺️ The Master Map

### 1. SETUP & CLONING (Two ways to start)
**Method A: Start from scratch**
* `git init` (Initialize local repo)
* `git remote add origin URL` (Link to empty GitHub repo)

**Method B: Clone existing project**
* `git clone URL` (Downloads repo & auto-links origin)
* `cd folder-name` (CRITICAL: Move into the new folder!)

### 2. DAILY WORKFLOW (The Loop)
* `git status` (Check what changed)
* `git add .` (Stage all changes)
* `git commit -m "message"` (Save snapshot locally)
* `git pull origin main` (Download updates from team)
* `git push origin main` (Upload to GitHub)

### 3. TEAM BRANCHING
* `git switch -c feature-branch` (Create & isolate new workspace)
* `git push origin feature-branch` (Upload branch to GitHub)
* `git merge feature-branch` (Combine into main locally if needed)

### 4. ADVANCED (History Rewriting)
* `git commit --amend` (Fix the last commit message or add a forgotten file)
* `git rebase -i HEAD~3` (Squash/clean up your last 3 commits)
* `git push --force-with-lease` (Safely push rewritten history without erasing team code)

### 5. EMERGENCIES (Undo & Save)
* `git restore .` (Destroy unsaved bad code)
* `git stash` (Hide half-finished work temporarily)
* `git stash pop` (Bring hidden work back)
* `git reflog` (The ultimate undo: find & recover deleted commits)

### 6. HEAVY LIFTING
* `git lfs` (Use Large File Storage for files >100MB)

---

## 🐍 Interactive Python Revision Tools
Forget scrolling through documentation. This repo includes custom Python CLI tools to help you find the right command instantly or test your knowledge!

### 1. The Git Guide (Cheat Sheet & Revision)
An interactive terminal menu that helps you find the exact workflow commands you need.
**How to run it:**
1. Open your terminal in this folder.
2. Run: `python git_guide.py`

### 2. Git Survival Mode (The Game)
Test your skills under pressure! Production is on fire. Can you type the correct Git commands to save the project and earn the rank of Git Master?
**How to run it:**
1. Open your terminal in this folder.
2. Run: `python git_survival_game.py`