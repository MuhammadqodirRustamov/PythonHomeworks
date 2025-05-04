import sqlite3

db_name = "library.db"
table_name = "Books "

create_query = f"""
CREATE TABLE IF NOT EXISTS {table_name}(
    Title TEXT,
    Author TEXT,
    Year_Published INT,
    Genre TEXT
)
"""
books_list = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
rating_list = [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby"),
]
with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # 1
    cursor.execute(create_query)

    # 2
    cursor.executemany(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?)", books_list)

    # 3
    cursor.execute(f"UPDATE {table_name} SET Year_Published = 1950 WHERE Title = '1984'")

    # 4
    cursor.execute(f"SELECT Title, Author FROM {table_name} WHERE Genre = 'Dystopian'")
    print(cursor.fetchall())

    # 5
    cursor.execute(f"DELETE FROM {table_name} WHERE Year_Published < 1950")

    # 6
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN Rating")
    cursor.executemany(f"UPDATE {table_name} SET Rating = ? WHERE Title = ?", rating_list)

    # 7
    cursor.execute(f"SELECT * FROM {table_name} ORDER BY Year_Published")
    print(cursor.fetchall())
