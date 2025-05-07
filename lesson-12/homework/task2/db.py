import sqlite3


def add_new_jobs(jobs: list):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS jobs(
        title TEXT,
        company TEXT,
        location TEXT,
        desc TEXT,
        link TEXT
    )
    """

    with sqlite3.connect("job.db") as connection:
        cursor = connection.cursor()
        # Create table if it does not exist already
        cursor.execute(create_table_query)
        # Add jobs
        cursor.executemany("INSERT INTO jobs VALUES(?, ?, ?, ?, ?)", jobs)


def get_jobs():
    with sqlite3.connect("job.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM jobs")
            jobs = cursor.fetchall()
            return jobs
        except sqlite3.OperationalError:
            return []


def update_jobs(updated_jobs: list):
    shuffled_list = [[job[3], job[4], job[0], job[1], job[2]] for job in updated_jobs]
    with sqlite3.connect("job.db") as connection:
        cursor = connection.cursor()
        cursor.executemany("UPDATE jobs SET desc=?, link=? WHERE title = ? AND company = ? AND location = ?",
                           shuffled_list)
