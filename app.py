import os
from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "genre": "Business",
        "status": "Available"
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "status": "Available"
    },
    {
        "id": 3,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self Help",
        "status": "Borrowed"
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "genre": "Technology",
        "status": "Available"
    }
]


@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()

    if search:
        filtered_books = [
            book for book in books
            if search in book["title"].lower()
            or search in book["author"].lower()
            or search in book["genre"].lower()
        ]
    else:
        filtered_books = books

    total_books = len(books)
    available_books = sum(
        1 for book in books if book["status"] == "Available"
    )
    borrowed_books = sum(
        1 for book in books if book["status"] == "Borrowed"
    )

    commit_id = os.getenv("RENDER_GIT_COMMIT", "local")

    return render_template(
        "index.html",
        books=filtered_books,
        total_books=total_books,
        available_books=available_books,
        borrowed_books=borrowed_books,
        commit_id=commit_id,
        search=search,
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/books/add", methods=["POST"])
def add_book():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    genre = request.form.get("genre", "").strip()

    if not title or not author or not genre:
        return {"success": False, "message": "All fields are required"}, 400

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "genre": genre,
        "status": "Available"
    }

    books.append(new_book)

    return {
        "success": True,
        "message": "Book added successfully!",
        "book": new_book
    }


@app.route("/books/<int:book_id>")
def book_details(book_id):
    book = next((book for book in books if book["id"] == book_id), None)

    if book is None:
        return "Book not found", 404

    return render_template("book_details.html", book=book)


@app.route("/api/books")
def api_books():
    return {"books": books}


@app.route("/books/<int:book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                return {
                    "success": False,
                    "message": "Book is already borrowed"
                }, 400

            book["status"] = "Borrowed"

            return {
                "success": True,
                "message": "Book borrowed successfully!"
            }

    return {
        "success": False,
        "message": "Book not found"
    }, 404


@app.route("/books/<int:book_id>/return", methods=["POST"])
def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                return {
                    "success": False,
                    "message": "Book is already available"
                }, 400

            book["status"] = "Available"

            return {
                "success": True,
                "message": "Book returned successfully!"
            }

    return {
        "success": False,
        "message": "Book not found"
    }, 404


if __name__ == "__main__":
    app.run(debug=True)
