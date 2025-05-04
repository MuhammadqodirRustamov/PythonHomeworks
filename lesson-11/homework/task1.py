import sqlite3

table_name = "Roster"

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name}(
    Name TEXT,
    Species TEXT,
    Age INT
);
"""
insert_list = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
rank_list = [("Captain", "Benjamin Sisko"), ("Lieutenant", "Ezri Dax"), ("Major", "Kira Nerys")]

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    # 1
    cursor.execute(create_table_query)
    # 2
    cursor.executemany(f"INSERT INTO {table_name} VALUES(?, ?, ?)", insert_list)
    # 3
    cursor.execute(f"UPDATE {table_name} SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
    # 4
    cursor.execute(f"SELECT Name, Age FROM {table_name} WHERE Species = 'Bajoran'")
    # 5
    cursor.execute(f"DELETE FROM {table_name} WHERE Age > 100")
    # 6
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN Rank")
    cursor.executemany(f"UPDATE {table_name} SET Rank = ? WHERE Name = ?", rank_list)
    # 7
    cursor.execute(f"SELECT * FROM {table_name} ORDER BY Age DESC")
    rows = cursor.fetchall()
    print(rows)
