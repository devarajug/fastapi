from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "sciece"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "Maths"},
    {"title": "Title Five", "author": "Author Five", "category": "Maths"},
    {"title": "Title Six", "author": "Author Six", "category": "Physics"},
]


@app.get("/books")
async def get_all_books():
    return BOOKS


# Path Params
@app.get("/books/{book_title}")
async def get_book(book_title: str):
    return [
        book
        for book in BOOKS
        if book.get("title").casefold() == book_title.casefold()
    ]


# Query Params
@app.get("/books/")
async def get_book_by_query_param(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/author/")
async def get_book_by_author_query(author_name: str):
    return [
        book
        for book in BOOKS
        if book.get("author").casefold() == author_name.casefold()
    ]


@app.get("/books/{book_author}/")
async def get_author_category_by_query_param(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for index, book in enumerate(BOOKS):
        if (
            book.get("title").casefold()
            == updated_book.get("title").casefold()
        ):
            BOOKS[index] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for index, book in enumerate(BOOKS):
        if book.get("title").casefold() == book_title.casefold():
            BOOKS.pop(index)
            break


# assignement
@app.get("/books/author/{author_name}")
async def get_book_by_author_name(author_name: str):

    return [
        book
        for book in BOOKS
        if book.get("author").casefold() == author_name.casefold()
    ]
