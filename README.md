# 🎰 NovaSpin

NovaSpin is a web-based casino gaming platform built with **Python** and **Django**. It provides users with an interactive, browser-based casino experience featuring slot machines, roulette, and blackjack.

**Disclaimer:** NovaSpin is intended for entertainment and/or educational purposes only. It does not involve real-money gambling unless explicitly configured and legally licensed to do so. Users are responsible for complying with local laws and regulations regarding online gaming.

---

## Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

## Features

- Interactive casino-style games
- User accounts and authentication
- Virtual currency / balance tracking
- Game history and results tracking
- Responsive web interface
- Django-powered backend for secure session and data handling


---

## Tech Stack

- **Backend:** Python, Django (6.0.3)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Dependencies:** See [`requirements.txt`](./requirements.txt)

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlanQ03/NovaSpin.git
   cd NovaSpin
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Create a superuser** for admin access
   ```bash
   python manage.py createsuperuser
   ```

### Running the Project

Start the local development server:

```bash
python manage.py runserver
```

Then open your browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
NovaSpin/
├── casino/           # Core casino game app (models, views, templates, game logic)
├── config/           # Django project settings and configuration
├── manage.py         # Django's command-line utility
├── requirements.txt  # Python dependencies
└── .gitignore
```

---

## Configuration

Before running in production, make sure to:

- Set `DEBUG = False` in your Django settings
- Configure a secure `SECRET_KEY` (ideally via environment variables)
- Set up `ALLOWED_HOSTS`
- Configure a production-ready database (e.g., PostgreSQL)
- Set up static file handling (`collectstatic`)


---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---


## 📬 Contact

Created by [AlanQ03](https://github.com/AlanQ03). Feel free to reach out with questions or suggestions via GitHub Issues.
