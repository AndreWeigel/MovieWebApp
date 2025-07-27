
# 🎬 MovieWeb App

Welcome to **MovieWeb App**, a simple Flask-based web application for managing your favorite movies!  
It features user-based movie management, clean routing, and a responsive HTML interface.

## 🚀 Features

- Add, view, and delete movies
- Each user can manage their own movies
- Safe delete operations (users can only delete their own entries)
- Responsive layout with basic styling
- Modular route structure and Jinja2 templating

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3 (with Jinja2 templating)
- **Database**: SQLite (easy to switch to PostgreSQL or others)

## 🧰 Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/movieweb.git
   cd movieweb
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   flask run
   ```

   Then visit [http://localhost:5000](http://localhost:5000) in your browser.

## 📁 File Structure

```
movieweb/
│
├── static/             # CSS and static assets
├── templates/          # Jinja2 HTML templates
├── app.py              # Main Flask app
├── models.py           # SQLAlchemy models
├── services.py         # Services for models
├── requirements.txt    # Dependencies
└── README.md
```


## 📝 License

MIT License. Feel free to fork, modify, and build upon this project.


