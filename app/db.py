import aiosqlite

DB_NAME = "bot.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            is_done INTEGER DEFAULT 0
        )
        """)
        await db.commit()

async def add_task(user_id: int, title: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO tasks (user_id, title) VALUES (?, ?)",
            (user_id, title)
        )
        await db.commit()

async def get_tasks(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT id, title, is_done FROM tasks WHERE user_id=?",
            (user_id,)
        )
        return await cursor.fetchall()
