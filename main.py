from fastapi import FastAPI

app = FastAPI(title="Library API")

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Doe",
        "category": "Programming"
    }
]

@app.get("/")
def home():
    return {"message": "Library API is working!"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {"message": "Book added successfully", "book": book}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i] = updated_book
            return {"message": "Book updated", "book": updated_book}
    return {"message": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}