# Django + Tailwind CSS Integration

This project uses [django-tailwind](https://github.com/timonweb/django-tailwind) to integrate [Tailwind CSS](https://tailwindcss.com/) into a Django project.

## 🚀 Features

- Easy Tailwind CSS integration with Django
- Hot-reload development with `npm run dev`
- Customizable templates and CSS
- Works seamlessly with Django templates

---

## 🛠️ Installation Steps

### 1. Install the required packages

```bash
pip install django-tailwind
```

### 2. Add 'tailwind' and your custom theme app to INSTALLED_APPS

Edit your settings.py:

```python
INSTALLED_APPS = [
    ...
    'tailwind',
    'theme',  # your Tailwind theme app
    ...
]
```

##🧾 Configuration
### 3. Define your Tailwind app name
In settings.py, add:
```
python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']  # Needed for hot reloading
```

## 📦 Create the Tailwind app
```bash
python manage.py tailwind init theme
```
This creates a new Django app named theme.

## ⚙️ Install Node modules
Navigate to the newly created Tailwind app and install dependencies:

```bash
cd theme
npm install
You can modify Tailwind configuration in theme/tailwind.config.js.
```

##👷 Development
### 4. Run Tailwind in development mode
```bash
npm run dev
```
This starts Tailwind CLI in watch mode for hot reload on changes.

### 5. Run Django server
In another terminal:

```bash
python manage.py runserver
```

##✅ Usage in Templates
In your base.html or any template file:

``` html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="{% static 'css/dist/styles.css' %}" rel="stylesheet">
</head>
<body class="bg-gray-100 text-gray-900">
    <h1 class="text-4xl font-bold text-center">Hello, Tailwind!</h1>
</body>
</html>
```

Make sure theme/static/css/dist/styles.css is generated and collected correctly.

## 📦 Production Build
To build CSS for production:

```bash
npm run build
Then collect static files:
```
python manage.py collectstatic

## 📁 File Structure
```
project/
│
├── theme/                    # Tailwind app
│   ├── static/
│   │   └── css/dist/styles.css  # Compiled Tailwind CSS
│   ├── templates/
│   ├── tailwind.config.js
│   └── ...
│
├── your_django_app/
├── manage.py
└── ...
``` 

## 🧹 Optional Tips
You can customize the theme via tailwind.config.js

Use @apply directive in input.css for reusable styles

Use npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch if manually working with Tailwind CLI

## 📚 Resources
Django-Tailwind Docs

Tailwind CSS Docs