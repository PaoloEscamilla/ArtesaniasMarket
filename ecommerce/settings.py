from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-)08j@_fts*_(ft5rw!+@r^2^=ihhoq4(qd(s21*y6qep#p(=b7'

# Activar solo para desarrollo, desactivar para producción
DEBUG = True  

ALLOWED_HOSTS = []  # Si despliegas en producción, agrega tus hosts permitidos (e.g., ['example.com'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda',  # Tu aplicación principal
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Usa esta carpeta para tus plantillas personalizadas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necesario para acceder a `request` en las plantillas
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'es-mx'  # Configuración para idioma español (México)
TIME_ZONE = 'America/Mexico_City'  # Ajustado al huso horario de México
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Carpeta para tus archivos estáticos personalizados
]

# Media files (archivos subidos por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de inicio/cierre de sesión y redirecciones
LOGIN_URL = '/login/'  # Página de inicio de sesión
LOGIN_REDIRECT_URL = '/redirect/'  # Redirige a la vista que decide a dónde enviar al usuario tras iniciar sesión
LOGOUT_REDIRECT_URL = '/'  # Página de redirección después de cerrar sesión

# Configuración adicional
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Solución a la advertencia de directorios estáticos inexistentes
import os
if not os.path.exists(STATICFILES_DIRS[0]):
    os.makedirs(STATICFILES_DIRS[0])  # Crea automáticamente la carpeta si no existe
