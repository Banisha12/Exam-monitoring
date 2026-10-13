# Smart Exam Monitor

Offline Examination Workflow & Integrity Monitoring System.

A Flask-based platform that monitors candidates during offline exams using cameras, detects malpractice signals, and generates integrity reports for invigilators.

---

## 🎯 Problem Statement

In offline exams, manual invigilation is:
- Error-prone
- Inconsistent
- Hard to audit

This system provides **automated monitoring** with **evidence-based integrity reports**.

---

## ✨ Features

- **Candidate Registration** — with validated face photo (exactly one face)
- **Secure Authentication** — hashed passwords, one active session per candidate
- **Session Lifecycle** — start, idle timeout, max duration, logout
- **Event Logging** — timestamped events for each malpractice type
- **Integrity Reports** — per-session summary for invigilators (later sprint)

---

## 🚨 Monitored Malpractice Types

| Type | Event Name |
|------|-----------|
| Looking away | `looking_away` |
| Phone use | `phone_detected` |
| Leaving seat | `left_seat` |
| Extra person | `multiple_persons` |
| Talking | `talking` |
| Impersonation | `impersonation` |
| Credential sharing | `new_login` |

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Computer Vision:** OpenCV
- **Data Analysis:** Pandas
- **Frontend:** HTML, CSS, Bootstrap
- **Version Control:** Git + GitHub

---

## 📋 Requirements

- Python 3.10+
- pip
- Git

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Banisha_Mallick/smart-exam-monitor.git
cd smart-exam-monitor