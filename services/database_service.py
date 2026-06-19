import sqlite3


class DatabaseService:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/apex.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        # Users Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE,
                name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Memories Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                memory TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        #knowledge base table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                category TEXT,
                key_name TEXT,
                value TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    def create_user(self, user_id, name):

        self.cursor.execute(
            """
            INSERT OR IGNORE INTO users (user_id, name)
            VALUES (?, ?)
            """,
            (user_id, name)
        )

        self.connection.commit()

    def get_user(self, user_id):

        self.cursor.execute(
            """
            SELECT *
            FROM users
            WHERE user_id = ?
            """,
            (user_id,)
        )

        return self.cursor.fetchone()

    def save_memory(self, user_id, memory):

        self.cursor.execute(
            """
            INSERT INTO memories (user_id, memory)
            VALUES (?, ?)
            """,
            (user_id, memory)
        )

        self.connection.commit()

    def get_memories(self, user_id):

        self.cursor.execute(
            """
            SELECT memory
            FROM memories
            WHERE user_id = ?
            """,
            (user_id,)
        )

        return self.cursor.fetchall()


    def save_knowledge(
        self,
        user_id,
        category,
        key_name,
        value
    ):

        self.cursor.execute(
            """
            INSERT INTO knowledge
            (
                user_id,
                category,
                key_name,
                value
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                category,
                key_name,
                value
            )
        )

        self.connection.commit()


    def get_knowledge(self, user_id):

        self.cursor.execute(
            """
            SELECT
                category,
                key_name,
                value
            FROM knowledge
            WHERE user_id = ?
            """,
            (user_id,)
        )

        return self.cursor.fetchall()