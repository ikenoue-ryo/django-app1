## インストール  
pipenv install django gunicorn psycopg2 psycopg2-binary Pillow  
pip install python-dotenv libsass django-compressor django-sass-processor

## ファイル作成  
touch .env  

SECRET_KEY=ここにSECRET_KEY  

DATABASE_ENGINE=  
DATABASE_DB=  
DATABASE_USER=  
DATABASE_PASSWORD=  
DATABASE_HOST=  
DATABASE_PORT=  


<!-- 
単体テスト実行
python manage.py test app.test

SCSSファイル変更
python manage.py sass static/app/index.scss static/css/index.css
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear


コンセプト
・車のシェアサービス。（現時点では実現不可の未来サービス）
・乗ったことのない車を個人から一定期間、借りることができるサービス
・貸し出す側は期間と金額、駐車場などのオプションを決定する。
・車にステッカーなどを張り、シェアできることを示す。
・ユーザーがどのような車を希望しているのかを募集することができる。
 -->