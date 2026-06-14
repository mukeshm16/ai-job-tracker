# AI-Powered Job Tracker with Interview Preparation

## Overview

AI-Powered Job Tracker is a full-stack web application developed using Django and Python that helps job seekers efficiently manage their job applications and prepare for interviews. The platform allows users to track applications, monitor progress, organize opportunities, and generate interview questions for preparation.

The project was developed to solve a common problem faced by students and job seekers: managing multiple job applications while simultaneously preparing for interviews.
---
## Website link:
url: https://ai-job-tracker-omzb.onrender.com
---

## Features

### User Authentication

* User Registration
* Secure Login
* Logout Functionality
* Protected Routes
* User-specific Data Access

### Job Application Management

* Add New Job Applications
* View Applied Jobs
* Update Application Details
* Delete Applications
* Track Application Status

### Dashboard

* Centralized Dashboard
* Application Overview
* User-specific Records
* Quick Access Navigation

### Search and Filtering

* Search Applications
* Filter Job Records
* Faster Job Tracking

### AI Interview Preparation

* Generate Interview Questions
* Role-based Question Suggestions
* Interview Practice Assistance

### Security

* Login Required Authentication
* User Data Isolation
* Session Management

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Backend

* Python
* Django Framework

### Database

* SQLite

### Deployment

* Render

### Version Control

* Git
* GitHub

---

## Project Architecture

```text
AI Job Tracker
│
├── Dashboard Module
│   ├── Home Page
│   ├── Analytics
│   └── User Overview
│
├── User Authentication Module
│   ├── Registration
│   ├── Login
│   └── Logout
│
├── Job Management Module
│   ├── Add Job
│   ├── Edit Job
│   ├── Delete Job
│   └── Search Jobs
│
├── AI Interview Module
│   └── Interview Question Generator
│
└── Database Layer
    └── SQLite
```

---

## Database Design

### JobApplication Model

| Field        | Description                            |
| ------------ | -------------------------------------- |
| Company Name | Name of Company                        |
| Role         | Job Position                           |
| Status       | Applied, Interview, Selected, Rejected |
| Applied Date | Application Date                       |
| Notes        | Additional Notes                       |
| User         | Associated User                        |

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-job-tracker.git
```

### Navigate to Project

```bash
cd ai-job-tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## Usage

### Registration

1. Create a new account.
2. Login with credentials.

### Job Tracking

1. Add job applications.
2. Update status.
3. Track progress.

### Interview Preparation

1. Open AI Questions Module.
2. Enter desired role.
3. Generate interview questions.

---

## Challenges Faced

During development several challenges were encountered:

* Django migration issues
* Authentication implementation
* User-specific data filtering
* Deployment configuration
* Static file management
* Git and GitHub integration
* Render deployment setup

These challenges were resolved through debugging, configuration updates, and proper deployment practices.

---

## Future Enhancements

* OpenAI API Integration
* Resume Upload Feature
* Resume Parsing
* Job Recommendation Engine
* Email Notifications
* Interview Scheduling
* Advanced Analytics Dashboard
* PostgreSQL Integration
* Profile Management
* Dark Mode

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Python Development
* Django Framework
* Authentication Systems
* CRUD Operations
* Database Management
* Git & GitHub
* Deployment using Render
* Full-Stack Web Development
* Problem Solving & Debugging

---

## Project Screenshots

Add screenshots of:

* Login Page
* Registration Page
* Dashboard
* Add Job Page
* AI Interview Question Generator
* Analytics Section

---

## Author

Mukesh M

Aspiring Python Developer | Django Developer | Full-Stack Web Developer

GitHub: https://github.com/mukeshm16

LinkedIn: https://linkedin.com/in/mukeshm16

---

## License

This project is developed for educational and portfolio purposes.
