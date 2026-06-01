# 🚨 SQL Injection Demo with Flask & SQLite

This repository contains a simple **Flask web application** that demonstrates how **SQL Injection vulnerabilities** can occur when user input is not properly sanitized.  
It is intended **for educational purposes only** — do not use this code in production!

---                  

## 📌 Overview

The app simulates a login form connected to a SQLite database.  
It deliberately uses **unsafe string concatenation** in SQL queries, making it vulnerable to SQL injection attacks.

### Vulnerable Code Example
```python
query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"
c.execute(query)
```

## Setup Instructions
Clone the repository:
```
git clone https://github.com/zeroday-attack/Web-security1.git
cd web-security1/sql-injection
```
Install dependencies:
```
pip install flask
```
Run the application:
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000/
```

## Demonstration of SQL Injection 
Try logging in with the following payloads:
- Bypass authentication:
```
  Username: admin' --
  Password: anything
```
- OR-based injection:
```
Username: ' OR '1'='1
Password: ' OR '1'='1
```
These inputs exploit the vulnerable query to trick the database into returning valid results without correct credentials.

## How to Fix
To prevent SQL injection, always use parameterized queries (prepared statements):
```
query = "SELECT * FROM users WHERE username = ? AND password = ?"
c.execute(query, (user, pwd))
```
This ensures user input is treated as data, not executable SQL.

## ⚠️ Disclaimer
This project is for educational and testing purposes only.
Do not deploy this code in a real-world environment.
Always follow secure coding practices to protect against SQL injection and other vulnerabilities.


