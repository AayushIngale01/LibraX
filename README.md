# LibraX — Smart Campus Library

> **Find. Borrow. Read. Return.**

LibraX is a dynamic Smart Campus Library web application built using **Python Flask**. It allows students to discover books, search the library collection, view book details, borrow and return books, and submit ratings.

The project was developed as an individual **Cloud Computing and DevOps (CSE30040) CCA 2** project at MIT World Peace University, Pune.

---

## 🚀 Features

- 📚 Dynamic library book catalogue
- 🔎 Search books by title, author, or genre
- 📖 Detailed book information
- 📥 Add new books with input validation
- 📗 Borrow and return books
- ⭐ Submit and calculate book ratings
- 📊 Available and borrowed book statistics
- 🔗 JSON API for books
- ❤️ Health-check endpoint
- 🆔 Live deployment commit ID displayed in the footer
- 🐳 Docker containerization
- ⚙️ Automated CI/CD using GitHub Actions
- ☁️ Deployment on Render

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.12 |
| Web Framework | Flask |
| Templates | Jinja2 |
| Testing | pytest |
| Linting | flake8 |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
LibraX/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── book_details.html
│
├── static/
│   └── style.css
│
└── .github/
    └── workflows/
        └── ci-cd.yml