import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q8oz7zb$zr^ptqwr2j(w6ivdvfu%dcrh8y8tje#*)h3hwci&px'  # os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # True
ALLOWED_HOSTS = ['192.168.2.190', 'localhost', '127.0.0.1']  # []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'known',
    'user',
    # 第三方验证码
    'captcha',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    # caches
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # caches
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 在模板中使用{{ MEDIA_URL }}
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'known',
        'USER': 'remote_user',
        'PASSWORD': 'phwphw',
        'HOST': '192.168.0.14',
        'PORT': 8925,
    }
}

# Password validation
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
LANGUAGE_CODE = 'zh-hans'  # 'en-us'
TIME_ZONE = 'Asia/Shanghai'  # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False  # True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# 静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 自定用户模型
AUTH_USER_MODEL = 'user.User'

# 分页
ANSWER_PER_PAGE = 10
QUESTION_PER_PAGE = 5
COMMENT_PER_PAGE = 5
TOPIC_PER_PAGE = 4
TREND_PER_PAGE = 5
USER_PER_PAGE = 5
SEARCH_PER_PAGE = 5

# 边缘显示页数
MARGIN_PAGES = 2
# 中间显示页数
PAGE_RANGE = 4

# 自定认证后端
AUTHENTICATION_BACKENDS = [
    'user.views.CustomModelBackend',
]

# login_required重定向url
LOGIN_URL = '/login/'

# 用户上传文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 富文本编辑器上传文件保存目录, 在media下
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    }
}

# cache django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'CONNECTION_POOL_KWARGS': {'max_connections': 100},
        },

    }
}

# celery settings
# celery中间人, 使用redis数据库
BROKER_URL = 'redis://127.0.0.1:6379/2'
# celery结果返回，跟踪结果
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

# celery内容消息的格式设置
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# celery时区设置
CELERY_TIMEZONE = TIME_ZONE
