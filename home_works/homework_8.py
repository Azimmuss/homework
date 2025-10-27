import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, name_book TEXT, author TEXT, genre TEXT, year INTEGER, pages INTEGER, copies INTEGER)
    """)


def add_books(conn, name_book, author, genre, year, pages, copies):
    conn.execute("""
    INSERT INTO books (name_book, author, genre, year, pages, copies)
    VALUES (?, ?, ?, ?, ?, ?) """,
    (name_book, author, genre, year, pages, copies))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("../databooks.db")
    create_tables(conn)
    add_books(conn, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 384, 25000)
    add_books(conn, 'To Kill a Mockingbird','Harper Lee', 'Historical Drama', 1960, 320, 22000)
    add_books(conn, '1984', 'George Orwell', 'Dystopian Science fiction', 1949, 336, 20000)
    add_books(conn, 'The Great Gatsby', 'Scott Fitzgerald', 'Classic Fiction', 1925, 180, 18000)
    add_books(conn, 'Fahrenheit 451', 'Ray Bradbury', 'Dystopian Science fiction', 1953, 176, 16000)
    add_books(conn, 'The Hobbit', 'J.R.R Tolkien', 'Fantasy', 1937, 310, 21000)
    add_books(conn, 'Dune', 'Frank Herbert', 'Epic Science fiction', 1965, 576, 19000)
    add_books(conn, 'The Catcher in the Rye', 'J.D Salinger', 'Novel of education', 1951, 277, 17000)
    add_books(conn, 'The Design of Everyday Things', 'Don Norman', 'Design', 1988, 369, 5000)
    add_books(conn, 'The Da Vinci Code', 'Dan Brown', 'Mystery', 2003, 489, 12000)
    conn.close()




import sqlite3


def get_books_by_author(conn, author):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name_book, author, genre, year, pages, copies
        FROM books
        WHERE author = ?
        ORDER BY name_book ASC
    """, (author,))
    results = cursor.fetchall()
    return results

if __name__ == "__main__":
    conn = sqlite3.connect("../databooks.db")


    books = get_books_by_author(conn, "George Orwell")

    # Выводим красиво
    for book in books:
        print(book)

    conn.close()