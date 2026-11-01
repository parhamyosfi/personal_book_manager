# Personal Book Manager

![Static Badge](https://img.shields.io/badge/python-3-blue)


A simple personal book management program written in Python. It allows users to add books, view their collection, and save book information for future use.

## Features

- Add multiple books to your personal collection.
- Display saved books.
- Store book information in a JSON file.
- Load previously saved books when the program runs again.

## Requirements

- Python 3
- python-dotenv

## Installation

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Environment Setup

1. Create a file named `.env` in the project directory.
2. Use `.env.example` as a template.
3. Add the following variable to your `.env` file:

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

4. Replace `your_password_here` with your own password.

**Important:** Never upload your actual `.env` file or real password to GitHub. Keep `.env` private and include `.env.example` in your repository.

## Run the Program

The main program file is `main.py`.

Run the program from the project directory:

```bash
python main.py
```

## Screenshot

![alt text](image-1.png)