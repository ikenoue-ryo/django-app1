## ファイル作成1  
touch .env  

<ファイル内記述例>  
DEBUG=0
SECRET_KEY=hoge
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_DB=django_db
DATABASE_USER=test
DATABASE_PASSWORD=test
DATABASE_HOST=postgres
DATABASE_PORT=5432
DATABASE=postgres

## ファイル作成2
/config/config/settings/
touch .local.py  

<ファイル内記述例>  
from .base import *
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

## 実行
docker-compose up -d --build

<!-- 
コマンド集

単体テスト実行
python manage.py test app.test

SCSSファイル変更
python manage.py sass static/app/index.scss static/css/index.css

本番起動用
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear

開発起動用
docker-compose -f docker-compose.yml exec django python manage.py makemigrations
docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput

コンテナ未使用時
python manage.py runserver --setting=config.settings.local
 -->