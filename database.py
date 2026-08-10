import sqlite3
from datetime import datetime


DATABASE_NAME = "chatbot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_chat(user_message, bot_response):
    connection = get_connection()

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO chat_history
        (user_message, bot_response, timestamp)
        VALUES (?, ?, ?)
    """, (
        user_message,
        bot_response,
        timestamp
    ))

    connection.commit()
    connection.close()


def get_chat_history():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM chat_history
        ORDER BY id DESC
    """)

    chats = cursor.fetchall()

    connection.close()

    return chats
