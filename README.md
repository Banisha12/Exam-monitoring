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



## 📁 Project Structure

```text
smart_exam_monitor/
├── app.py                      # Main Flask application (Routes & DB Models)
├── config.py                   # App configuration (MySQL URI, Secret Keys)
├── requirements.txt            # Python dependencies (Flask, Pandas, Faker, etc.)
├── .gitignore                  # Files to ignore (venv, __pycache__, etc.)
│
├── data/
│   └── synthetic/              # Sprint 1: Generated Synthetic Datasets
│       ├── avatars/            # 100 student avatar images (.jpg)
│       ├── ai_reports.csv
│       ├── candidates.csv
│       ├── events.csv
│       ├── risk_data.csv
│       ├── scores.csv
│       └── sessions.csv
│
├── data_science/               # Sprint 2 & 3: Data Science Pipelines
│   ├── generate_data.py        # Sprint 1: Script to generate synthetic data & download avatars
│   ├── pipeline.py             # Sprint 2: Preprocessing pipeline & baseline statistics
│   ├── event_normalizer.py     # Sprint 3: Logic to group AI frames into single valid events
│   ├── test_validation.py      # Sprint 2: Script to test edge cases (missing data, re-run consistency)
│   └── test_zero_events.py     # Sprint 2: Script to prove Left Join handling of 0 events
│
├── database/
│   └── schema.sql              # MySQL Database schema (6 tables including normalized events)
│
├── templates/                  # Flask HTML Templates
│   └── base.html               # Base template layout
│
├── static/                     # Static assets for Flask frontend
│   └── faces/                  # Folder for future live camera snapshots
│
└── venv/                       # Virtual environment (Ignored by Git)