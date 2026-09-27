# LibraX — Smart Campus Library

LibraX is a Flask-based Smart Campus Library web application developed for the Cloud Computing and DevOps course at MIT World Peace University.

The project demonstrates dynamic web pages, book management operations, validation, REST API functionality, automated testing, linting, Docker containerization, GitHub Actions CI/CD, and deployment on Render.

## Features

- 📚 Dynamic library book catalogue
- 🔎 Search books by title, author, and genre
- 📖 View detailed book information
- ➕ Add new books using a POST form
- ✅ Input validation for book creation
- 📕 Borrow books
- 🔄 Return borrowed books
- ⭐ Rate books from 1–5 stars
- 📊 Book rating statistics
- 🔌 JSON API for books
- ❤️ Health check endpoint
- 🐳 Docker containerization
- ⚙️ Automated GitHub Actions CI/CD
- 🚀 Automatic deployment to Render through a Deploy Hook
- 🆔 Live website displays the deployed Git commit ID

## Technology Stack

- Python 3.12
- Flask
- HTML5
- CSS3
- JavaScript
- Pytest
- Flake8
- Docker
- Git & GitHub
- GitHub Actions
- Render

## Project Structure

```text
LibraX/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── book_details.html
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md