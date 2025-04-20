# 🎙️ PodStream - AI-Powered Podcast Platform

A Django-based web application that allows users to upload, view, and manage podcast videos with support for Google Gemini chatbot integration.

---

## 🚀 Features

- 🎧 Upload and manage podcasts (video-based)
- 🖼️ Automatic thumbnail generation
- 💬 Gemini API Chatbot integration (Google Generative AI)
- 🔒 Authentication system (Signup/Login)
- 📁 Media file handling (podcasts & thumbnails)
- 🌐 Static files for styling and interactivity

---

## 🗂️ Project Structure

```
podcast/
├─ authentication/         # User authentication (login/signup)
├─ features/               # Podcast upload, form handling, models
├─ media/                  # Uploaded videos and thumbnails
├─ podcast/                # Main Django config (settings, urls, views)
├─ static/                 # CSS, JS, and background images
├─ templates/              # HTML templates
├─ db.sqlite3              # Default SQLite database
├─ manage.py               # Django management script
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/podstream.git
cd podstream
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 📦 **requirements.txt** includes:

```text
Django>=5.0.2
google-generativeai>=0.3.0
python-dotenv>=1.1.0
requests>=2.31.0
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_google_generative_ai_key_here
```

---

## 🛠️ Run the Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📷 Media Handling

- Podcasts are stored under `media/podcasts/`
- Thumbnails are stored under `media/thumbnails/`

Ensure you have these settings in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 🧠 Gemini Chatbot Integration

- Gemini Chatbot integration powered by `google-generativeai`
- Set your API key in `.env` file
- Backend connects to Gemini for smart podcast suggestions or replies

---

## 📌 To-Do / Upcoming

- ✅ Add repeatable notifications for podcast reminders
- ✅ Enhance UI for chatbot interactions
- ⏳ Add user profile and dashboard
- ⏳ Add Like/Comment/Share functionality
- ⏳ Add Gemini-generated show notes or summaries

---

## 🧑 Author

**Mratyunjay Saxena**  
[LinkedIn](https://www.linkedin.com/in/mratyunjay-saxena-963176226/) | [GitHub](https://github.com/innocentprogrammer)

---
