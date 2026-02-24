# HRMS Lite - Human Resource Management System

A lightweight Django-based HRMS for managing employees, attendance, and departments.

## Project Structure

```
HRMS_project/
├── backend/               # Django backend application
│   ├── main/              # Main app (models, views, templates)
│   ├── mysite/            # Django project config (settings, urls, wsgi)
│   ├── manage.py
│   ├── requirements.txt
│   ├── build.sh           # Render.com build script
│   └── Procfile           # Process file for deployment
├── render.yaml            # Render.com blueprint
└── .gitignore
```

## Local Development

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access at: http://127.0.0.1:8000/  
Admin at:  http://127.0.0.1:8000/admin/

## Render.com Deployment

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set **Root Directory** to `backend`
5. Set **Build Command**: `./build.sh`
6. Set **Start Command**: `gunicorn mysite.wsgi:application`
7. Add environment variables:
   - `SECRET_KEY` → (generate a strong random key)
   - `DEBUG` → `False`
   - `ALLOWED_HOSTS` → `your-app-name.onrender.com`

## Tech Stack

- **Backend**: Django 5.x + Django REST Framework
- **Database**: SQLite (local) 
- **Static Files**: WhiteNoise
- **Deployment**: Render.com
