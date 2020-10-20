## ファイル作成  
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