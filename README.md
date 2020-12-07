## 概要  
CtoC型のカーシェアサービス  

このポートフォリオ の開発理由は、  
市場規模(成長性)、需要（購買力）、リソース（資源）があると想定・確保しているからです。  

・2019年のレンタカー市場規模が約9500億円、BtoC型カーシェアリングが約550億円あり、カーシェアの会員数は前年比較で23%増で急成長しております。  
この市場にCtoC型の個人間カーシェアを持ち込むことで、一定の杯を確保できる上、BtoCカーシェアやレンタカー市場にはない、新規の顧客を獲得できると想定します。  

従来、企業側が提供するレンタカーには在庫の制限があり、車を借りる側はその中で選択を迫られていました。そこには取りに行く手間や乗りたい車に乗れない、すぐに借りれないなどの問題点がありました。  
それを解消するサービスがCtoC型のカーシェアリング（ポートフォリオ ）です。ガレージシェアリングというドメインは、車の所有者が車を使わない期間に駐車場ごと貸す、というイメージで考案しました。  

・その他、リソースについてはいくつかありますが有力なものは、すでにWPでSEO集客した月間5000人の、「移動手段に車を使っているが、お金をかけたくない」、もしくは「今から車を買おうか悩んでいるがお金をかけたくない」というユーザーがおりまして、ポートフォリオに流し込むという想定です。  

以上のことから、3つのビジネス観点を持ち込み、ポートフォリオ として開発致しました。  

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
DATABASE_DB=db  
DATABASE_USER=test  
DATABASE_PASSWORD=test  
DATABASE_HOST=postgres  
DATABASE_PORT=5432  
DATABASE=postgres  

## ファイル作成2  
touch .env.db  

<ファイル内記述例>  
POSTGRES_USER=db_user  
POSTGRES_PASSWORD=password  
POSTGRES_DB=db  

## ディレクトリ作成  
npm run build  

## 実行
pipenv shell  
pipenv install  
docker-compose -f docker-compose.prod.yml up -d --build  
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput  
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear  

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

## ペルソナ設計と機能要件定義
### ペルソナ設計例
<img src="https://user-images.githubusercontent.com/61681360/100817666-d7c45980-348b-11eb-849c-906b6c7ed1b4.jpg">

■サービス対象ユーザーの思考（車を借りる側）  
・車を買う必要がないと思っている。  
・車が移動手段だと考えている。  
・まれに遠くにドライブに出かけたいが車を所有したくないと思っている。  
・一度は高級車に乗ってみたいという憧れがある。  
・シェアサービス(チャリチャリなど)を使ったことがありその便利さは知っている。  

■ペルソナ（借り手）のイメージ  
・都内や都心部に住んでいて車を買う必要がないと感じている、20〜30代前半の男性  
・車があると便利だと知りながら、維持費が高いため電車等で移動している30代男性  
・毎度近場でカフェや買い物を楽しんでいるがたまには友人と遠出したいと20代の女性  
・業務用スーパーや自宅周辺の安いスーパーに行くような節約思考の20代後半〜30代主婦  
・あの車に乗りたいという特定のこだわりがある40〜50代の男性  

■対象外ユーザー  
車を毎日使う、車に荷物を積んでおきたい、と考えている層。  
・子供がいて、毎日の送り迎えが必要な主婦  
・通勤として使っていて車が常に必要な人  
・車に何か荷物を積んでおきたい事情がある人（釣具、キャンプなどのアウトドア好き、チャイルドシートなど）  

■ペルソナ（借り手）の疑問や不安  
・近くにある車を探したい  
・少し遠くてもいいけどフェラーリなどの乗りたい車を探す  
・貸し手のユーザーに会いたくない。  
・事故したらどうしよう。保険とかどうなってるの？  
・支払いを電子・スマホ決済にしたい  
・支払い方法ってどうやるの？  
・安心できる支払い方法をとりたい（第三者を介すなど）  
・乗り捨てできる？  

■ペルソナ（買い手）が欲しいと思う機能  
・現在地や車のある場所の位置情報  
・電子決済、スマホ決済  
・保険や保証制度  
・車のグレードや値段検索（絞り込み検索）  
・利用方法、ルールやマナーなどの説明  
・スケジュール管理  
・貸し手とのメッセージのやりとり  
・車にどういう機能や価値があるのか。  
　例：クルーズコントロール、グレード、車種、装備内容(カーナビ、キーレス、障害物センサー、車検)  
・困った時に電話して聞けるようなカスタマーサポート  
・スーパーなどで乗りたい車を見つけた場合乗れないのか？　など。  

■ペルソナ（貸し手）  
・一定期間に車を使わない場合、貸し出したいと思っている個人  
・中古車等の理由から傷がついても良い、と思っているようなユーザー  

■対象外ユーザー  
・傷ができてしまった場合や、過失の損害賠償を目的とする一部の悪用ユーザーへの対応  
・新車や買ったばかりの車  

■ペルソナ（貸し手）が欲しいと思う機能  
・予約のスケジュール管理  
・予約取り消し機能。出品停止機能。  
・鍵をどうやって渡すのか？  
・支払い日の確認、振り込み金額確認  
・投稿時のPR機能の充実　例：車検証登録日、車のオプションなどのPR  
・ツイッターやインスタなどからのシェア機能  
・事故の保証や損害賠償の説明  
・いつ返却されるのか、今どこにあるのか？の確認  
・今借りているユーザーの連絡先（メールアドレスなどの一部の個人情報）  

### 機能定義（実装予定）
以上を踏まえて、作るべき機能要件  

■実装すべき機能要件  
・投稿、編集、削除、出品停止 機能  
・ユーザーの現在地や投稿車のおおよその位置情報（google map）  
・本人確認（免許証提示若しくは年齢設定画面）  
・保証、損害賠償等の説明(LP)  
・ルールや使い方、トラブルの際の説明（LP）  
・Q&A（こんな時どうするLP）  
・決済機能  
・検索機能：グレードや値段、貸し出し期間や用途別、オプション有無、など  
・レコメンド機能（車、ユーザー、現在地）  
・ランキング機能  
・注文履歴の表示  
・入力エラー時の分かりやすいバリデーション  
・フォローやフォロワー機能（今度借りる、などの用途）  
・いいね機能(車、ユーザー)やいいねした車のリスト表示  
・チャット機能（ユーザー間）  
・車種名、その他のタグ付け機能  
・SNSシェア機能  
・SNS連携ログイン  
・リッチテイスト（SPA、無限スクロール、ローディング機能など）  
・予約スケジュール管理画面  
・貸し手の収入金額確認画面  
・貸し手の投稿時の選択機能の充実（車検証登録日や車のオプションPR等）  


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
ログ確認：docker-compose -f docker-compose.prod.yml logs

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