import sqlite3

def setup_database():
    connection = sqlite3.connect("todo.db")
    cursor_obj = connection.cursor()

    create_task_query = """CREATE table IF NOT EXISTS task(
    ID INTEGER PRIMARY KEY NOT NULL,
    title VARCHAR,
    description VARCHAR,
    priority VARCHAR,
    is_done BOOL,
    user_id INTEGER);
    """

    create_user_query = """CREATE table IF NOT EXISTS user(
    ID INTEGER PRIMARY KEY NOT NULL,
    username VARCHAR,
    tg_nick VARCHAR);
    """

    cursor_obj.execute(create_task_query)
    cursor_obj.execute(create_user_query)

    connection.commit()

    print("Database is already setup")