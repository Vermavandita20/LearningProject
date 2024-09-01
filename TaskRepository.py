import psycopg2
from psycopg2 import sql
from Task import Task
from Config import DATABASE

class TaskRepository:
    def __init__(self):
        self.conn = psycopg2.connect(**DATABASE)
        self.create_table()

    def create_table(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        due_date DATE,
                        status TEXT DEFAULT 'Pending'
                    )
                ''')
                self.conn.commit()

    def add_task(self, task: Task):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO tasks (title, description, due_date, status)
                    VALUES (%s, %s, %s, %s) RETURNING id
                ''', (task.title, task.description, task.due_date, task.status))
                task.id = cur.fetchone()[0]
                self.conn.commit()
        return task

    def get_task(self, task_id: int):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
                row = cur.fetchone()
                if row:
                    return Task(id=row[0], title=row[1], description=row[2], due_date=row[3], status=row[4])
        return None

    def update_task(self, task: Task):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('''
                    UPDATE tasks SET title = %s, description = %s, due_date = %s, status = %s
                    WHERE id = %s
                ''', (task.title, task.description, task.due_date, task.status, task.id))
                self.conn.commit()
        return task

    def delete_task(self, task_id: int):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
                self.conn.commit()

    def list_tasks(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute('SELECT * FROM tasks')
                rows = cur.fetchall()
                return [Task(id=row[0], title=row[1], description=row[2], due_date=row[3], status=row[4]) for row in rows]
