
# 🎬 MovieWeb App

Welcome to **MovieWeb App**, a simple Flask-based web application for managing your favorite movies!  
It features user-based movie management, clean routing, and a responsive HTML interface.

## 🚀 Features

- User authentication (optional)
- Add, view, and delete movies
- Each user can manage their own movies
- Safe delete operations (users can only delete their own entries)
- Responsive layout with basic styling
- Modular route structure and Jinja2 templating

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3 (with Jinja2 templating)
- **Database**: SQLite (easy to switch to PostgreSQL or others)
- **API**: OMDb API integration

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

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your OMDb API key:
   ```
   OMDB_API_KEY=[YOUR_API_KEY]
   ```

5. **Run the app**:
   ```bash
   flask run
   ```

   Then visit [http://localhost:5000](http://localhost:5000) in your browser.

## 📁 File Structure

```MovieWebApp/
│
├── app/                     # Main application package
│   ├── __init__.py          # App factory and configuration loading
│   ├── models/              # SQLAlchemy models
│   ├── routes/              # Flask blueprints (views/routes)
│   ├── services/            # External API integrations (e.g., OMDb)
│   ├── templates/           # Jinja2 templates (HTML)
│   └── static/              # CSS, JS, images
│
├── instance/                # Local configuration (e.g. SQLite db)│
├── .env                     # Environment variables (e.g., OMDB_API_KEY)
├── .gitignore               # Ignore venv, .env, etc.
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── run.py                   # Entry point for running the app
```


## 📝 License

MIT License. Feel free to fork, modify, and build upon this project.

---
