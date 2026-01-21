# Telegram Task Bot 🤖📝

A simple Telegram bot for managing personal tasks.  
Built with **Python** and **aiogram**, using **SQLite** for data storage.

This is a learning-oriented pet project that demonstrates:
- Telegram bot development
- Async Python (asyncio)
- Clean project structure
- Environment variable configuration
- Basic database usage

---

## 🚀 Features

- Add new tasks
- View task list
- Persistent storage using SQLite
- Modular and readable codebase

---

## 🧱 Project Structure

```text
tg-task-bot/
│
├── app/
│   ├── bot.py
│   ├── config.py
│   ├── db.py
│   ├── keyboards.py
│   ├── states.py
│   └── handlers/
│       ├── start.py
│       └── tasks.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
