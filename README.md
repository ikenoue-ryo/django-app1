## 概要  
カーシェアサービス  
CtoC型の車のシェアサービスとなります。  
車を所有しているユーザーが、車を使わない期間に他人に貸し出すサービスのことで、貸し出す側のユーザーは自分の車をどれぐらいの期間、いくらで貸し出すのかを投稿します。その際に駐車場自体の貸し出しOKや乗り心地などもPRできます。  
これにより、これまで手の届かなかった高級車や乗ったことのない車に乗ることができるようになり、レンタカーやBtoC向けのカーシェアリングにはない、体験価値を提供することができます。  

一方、課題としては事故の際の補償やユーザー同士のトラブルをどのように解決できるかという点で試行錯誤中です。  

## 使用技術  
### フロントエンド  
レスポンシブ対応  
- Vue.js: 2.6.11
- Vue CLI: 3.5.2
- Vuex: 3.5.1
- Vuetify: 2.2.11
- Sass(scss)
- HTML/CSS

### バックエンド  
- Python: 3.8.3
- Django: 3.1.2
- Django Rest Framework: 3.11.1

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

## 実行
pipenv shell  
pipenv install  
docker-compose up -d --build  


## コマンド集
本番起動用  
docker-compose -f docker-compose.prod.yml down -v  
docker-compose -f docker-compose.prod.yml up -d --build  
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput  
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear  
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:1337/api/v1/  

開発起動用  
docker-compose -f docker-compose.yml exec django python manage.py makemigrations  
docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput  
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:8000/api/v1/  

## インフラ構成
- インフラ構成図(構成予定のものを含んで記載)
<img src="https://user-images.githubusercontent.com/61681360/99186009-bfb4c080-2790-11eb-903a-b38a7359f15a.png">

- AWS
    - EC2 / VPC / S3 / CroudFront / Route53 / CloudWatch / ALB

- Docker
    - Docker: 19.03.8
      - ボリュームによるコンテナ間のデータ共有
    - docker-compose: 1.25.5
      - ローカル環境構築

- CircleCI
    - 自動テスト
      - masterブランチ以外へマージしてテストを開始
    - 自動デプロイ
      - masterブランチへマージしてEC2/S3へデプロイ

- Nginx(Webサーバー)

- Gunicorn(アプリケーションサーバー)

- PostgreSQL: 11.4(データベース)

## 画面イメージ
<img src="https://user-images.githubusercontent.com/61681360/98380895-8abbb600-208c-11eb-8a17-963ce000e40c.png">
<img src="https://user-images.githubusercontent.com/61681360/98381026-aa52de80-208c-11eb-87b7-be1c4f4a7ad4.png">
<img src="https://user-images.githubusercontent.com/61681360/98381070-b5a60a00-208c-11eb-85bf-91f9e9b32f1d.png">
<img src="https://user-images.githubusercontent.com/61681360/98381126-ca829d80-208c-11eb-949d-cfb4f77a76c7.png">


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
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:1337/api/v1/

開発起動用
docker-compose -f docker-compose.yml exec django python manage.py makemigrations
docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput
VUE_APP_ROOT_API=http://127.0.0.1:8000/api/v1/

コンテナ未使用時
python manage.py runserver --setting=config.settings.local

CircleCIのローカル実行
※workflowは対応していないためjobを指定して実行
例：circleci build --job build_test .circleci/config.yml
 -->