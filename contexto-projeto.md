This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
atendimentos/
  migrations/
    __init__.py
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
config/
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py
images/
  Django-Logo.png
  docker-icon-logo.png
  IEEE_Computer.png
  iff_logo.png
  postgre_logo.png
miscellaneous/
  meetings_and_notations/
    r001.md
pacientes/
  migrations/
    __init__.py
  templates/
    pacientes/
      test.html
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  urls.py
  views.py
.dockerignore
.gitignore
docker-compose.yml
Dockerfile
manage.py
pyproject.toml
README.md
```

# Files

## File: pacientes/templates/pacientes/test.html
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Teste</title>
</head>
<body>
    <h1>Template funcionando</h1>
    <p>Olá, {{ nome }}!</p>

    <ul>
        {% for item in itens %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## File: pacientes/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test, name="test"),
]
```

## File: atendimentos/migrations/__init__.py
```python

```

## File: atendimentos/__init__.py
```python

```

## File: atendimentos/admin.py
```python
from django.contrib import admin

# Register your models here.
```

## File: atendimentos/apps.py
```python
from django.apps import AppConfig


class AtendimentosConfig(AppConfig):
    name = 'atendimentos'
```

## File: atendimentos/models.py
```python
from django.db import models

# Create your models here.
```

## File: atendimentos/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

## File: atendimentos/views.py
```python
from django.shortcuts import render

# Create your views here.
```

## File: config/__init__.py
```python

```

## File: config/asgi.py
```python
"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
```

## File: config/urls.py
```python
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
]
```

## File: config/wsgi.py
```python
"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
```

## File: miscellaneous/meetings_and_notations/r001.md
```markdown
# Perguntas para definição de escopo do projeto SUA (sistema unificado de atendimento)


## 1: Quais são os processos que vocês realizam atualmente ?
->
## 2: Quais são os participantes desse processo ?
-> 
## 3: Como voces armazenam os dados de voces e quais são esses dados ? (Visão geral)
->
## 3: O que voces buscam melhorar ou resolver com um sistema ?
->
## 4: O que é essencial e indispensável ter em um novo sistema ?
-> 
## 5: Vai ter integração com outros sistemas ?
->
## 6: O que não será feito nesse projeto ?
->
```

## File: pacientes/migrations/__init__.py
```python

```

## File: pacientes/__init__.py
```python

```

## File: pacientes/admin.py
```python
from django.contrib import admin

# Register your models here.
```

## File: pacientes/apps.py
```python
from django.apps import AppConfig


class PacientesConfig(AppConfig):
    name = 'pacientes'
```

## File: pacientes/models.py
```python
from django.db import models

# Create your models here.
```

## File: pacientes/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

## File: pacientes/views.py
```python
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def test(request):
    context = {
        "nome": "Asafe",
        "itens": ["triagem", "enfermaria", "médico"],
    }
    return render(request, "templates/pacientes/test.html", context)
```

## File: .dockerignore
```
.venv
.git
__pycache__
.env
```

## File: .gitignore
```
.env
```

## File: manage.py
```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

## File: config/settings.py
```python
import os

"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 6.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vyy=*gc^!-+espp-a%ymeo%75hn_s%+e#7u*7q79^1d=#x3=2%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "sua"),
        "USER": os.environ.get("POSTGRES_USER", "sua"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'


# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
```

## File: docker-compose.yml
```yaml
services:
  web:
    build: .
    container_name: sua-web
    depends_on:
      db:
        condition: service_healthy
    env_file: .env
    environment:
      POSTGRES_HOST: db
      POSTGRES_PORT: "5432"
    ports:
      - "127.0.0.1:8000:8000"
    volumes:
      - .:/app
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

  db:
    image: postgres:17
    container_name: sua-db
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-sua}
      POSTGRES_USER: ${POSTGRES_USER:-sua}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?defina POSTGRES_PASSWORD no .env}
    ports:
      - "127.0.0.1:5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-sua} -d ${POSTGRES_DB:-sua}"]
      interval: 5s
      timeout: 3s
      retries: 10

volumes:
  pgdata:
```

## File: Dockerfile
```dockerfile
FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## File: pyproject.toml
```toml
[project]
name = "sua"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "asafe fernandes", email = "177295792+asafe-fernandes@users.noreply.github.com" }
]
requires-python = ">=3.13"
dependencies = [
    "django>=6.1.2",
    "psycopg[binary]>=3.3.6",
]

[dependency-groups]
dev = [
    "pytest>=9.2.0",
    "ruff>=0.17.3",
]
```

## File: README.md
```markdown

```
