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