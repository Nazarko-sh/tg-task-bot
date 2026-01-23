# Telegram Task Bot 🤖📝

A Telegram bot built with Python to manage tasks and automate simple workflows.

The bot allows users to create and view tasks directly in Telegram,
demonstrating a practical approach to task management and automation.

---

## 🚀 Features

- Add new tasks via Telegram commands
- View and manage task list
- Persistent storage using SQLite
- Async bot logic using aiogram
- Clean and modular project structure

---

## 🧱 Use Cases

- Personal task tracking
- Simple productivity automation
- Telegram-based workflow management
- Foundation for more advanced automation bots

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
