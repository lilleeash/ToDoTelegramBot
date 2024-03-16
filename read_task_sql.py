import sqlite3

def read_task_sql():
    connection = sqlite3.connect("todo.db")
    cursor_obj = connection.cursor()

    cursor_obj.execute("""SELECT * FROM task""")
    tasks = cursor_obj.fetchall()

    result = "\n".join([f"{ index + 1 }. { task[1], task[2], task[3], task[4] }" for index, task in enumerate(tasks)])

    return result