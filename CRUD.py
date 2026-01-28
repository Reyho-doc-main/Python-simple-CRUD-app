import sqlite3
from database import get_connection

def create_user(username: str, password: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO id_and_passwd (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def verify_user(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM id_and_passwd WHERE username = ? AND password = ?",
        (username, password)
    )

    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


def create_post(user_id: int, content: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO posts (user_id, content, likes) VALUES (?, ?, 0)",
            (user_id, content)
        )

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def read_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            posts.id, posts.user_id, posts.content, COUNT(likes.post_id) AS likes FROM posts
        LEFT JOIN likes ON posts.id = likes.post_id
        GROUP BY posts.id ORDER BY likes DESC LIMIT 10""")

    rows = cursor.fetchall()
    conn.close()
    return rows


def update_post(post_id: int, new_content: str, user_id:int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE posts SET content = ? WHERE id = ? AND user_id = ?",
            (new_content, post_id, user_id)
        )

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_post(post_id: int, user_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM posts WHERE id = ? AND user_id = ?",
        (post_id, user_id)
    )

    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

def like_post(post_id: int, user_id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO likes (user_id, post_id) VALUES (?, ?)",
            (user_id, post_id)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False  # already liked or invalid post

    finally:
        conn.close()

def unlike_post(post_id: int, user_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM likes WHERE user_id = ? AND post_id = ?",
        (user_id, post_id)
    )

    conn.commit()
    removed = cursor.rowcount > 0
    conn.close()
    return removed


def read_own_posts(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT posts.id, posts.user_id, posts.content, COUNT(likes.post_id) AS likes
FROM posts
LEFT JOIN likes ON posts.id = likes.post_id
WHERE posts.user_id = ?
GROUP BY posts.id
ORDER BY likes DESC
""", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    return rows

