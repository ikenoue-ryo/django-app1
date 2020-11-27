from django.test import TestCase

from users.models import User, Profile, Tag, Post, Comment, Message


class UserModelTest(TestCase):
    """ユーザーモデル"""

    def test_is_empty(self):
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 0)

    def test_saveing_and_retrieving_user(self):
        # DBに保存されるかの確認
        first_user = User()
        first_user.email = 'test@gmail.com'
        first_user.username = 'test_user'
        first_user.save()

        saves_all_user = User.objects.all()
        self.assertEqual(saves_all_user.count(), 1)

        # 登録したテストユーザーの取得と確認
        saves_first_user = User.objects.get(id=1)
        self.assertEqual(saves_first_user.email, 'test@gmail.com')
        self.assertEqual(saves_first_user.username, 'test_user')


class ProfileModelTest(TestCase):
    """プロフィールモデル"""

    def setUp(self):
        # 初期データ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

    def test_is_empty(self):
        saved_profile = Profile.objects.all()
        self.assertEqual(saved_profile.count(), 0)

    def test_saveing_and_retrieving_profile(self):
        # DBに保存されるかの確認
        first_user_profile = Profile()
        first_user_profile.userpro = self.user
        first_user_profile.introduction = 'テストユーザーです。宜しくお願いします。'
        first_user_profile.address = '福岡県福岡市博多区'
        first_user_profile.save()

        saves_all_user_profile = Profile.objects.all()
        self.assertEqual(saves_all_user_profile.count(), 1)

        # 登録したテストユーザーのプロフィールの取得と確認
        saves_user_proifle = Profile.objects.get(id=self.user.id)
        self.assertEqual(
            saves_user_proifle.introduction, 'テストユーザーです。宜しくお願いします。'
        )
        self.assertEqual(saves_user_proifle.address, '福岡県福岡市博多区')


class CommentModelTest(TestCase):
    """コメントモデル"""

    def setUp(self):
        # 初期ユーザーデータ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

        # 初期プロフィールデータ
        first_user_profile = Profile()
        first_user_profile.userpro = self.user
        first_user_profile.introduction = 'テストユーザーです。宜しくお願いします。'
        first_user_profile.address = '福岡県福岡市博多区'
        first_user_profile.save()
        self.user_profile = Profile.objects.get(id=self.user.id)

    def test_is_empty(self):
        saved_comment = Comment.objects.all()
        self.assertEqual(saved_comment.count(), 0)

    def test_saveing_and_retrieving_comment(self):
        # DBに保存されるかの確認
        user_comment = Comment()
        user_comment.username = self.user
        user_comment.point = 5
        user_comment.profile = self.user_profile
        user_comment.comment = 'ありがとうございました！'
        user_comment.save()

        saves_all_user_comment = Comment.objects.all()
        self.assertEqual(saves_all_user_comment.count(), 1)

        # 投稿されたコメントの取得と確認
        saves_user_comment = Comment.objects.get(id=self.user.id)
        self.assertEqual(saves_user_comment.point, 5)
        self.assertEqual(saves_user_comment.profile, self.user_profile)
        self.assertEqual(saves_user_comment.comment, 'ありがとうございました！')


class TagModelTest(TestCase):
    """タグモデル"""

    def test_is_empty(self):
        saved_tag = Tag.objects.all()
        self.assertEqual(saved_tag.count(), 0)

    def test_saveing_and_retrieving_tag(self):
        # DBに保存されるかの確認
        post_tag = Tag()
        post_tag.name = 'テストタグ'
        post_tag.save()

        saves_all_tag = Tag.objects.all()
        self.assertEqual(saves_all_tag.count(), 1)

        # 投稿されたコメントの取得と確認
        tag = Tag.objects.get(id=post_tag.id)
        saves_tag = Tag.objects.get(id=tag.id)
        self.assertEqual(saves_tag.name, 'テストタグ')


class PostModelTest(TestCase):
    """投稿モデル"""

    def setUp(self):
        # 初期ユーザーデータ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

        # 初期プロフィールデータ
        first_user_profile = Profile()
        first_user_profile.userpro = self.user
        first_user_profile.introduction = 'テストユーザーです。宜しくお願いします。'
        first_user_profile.address = '福岡県福岡市博多区'
        first_user_profile.save()
        self.user_profile = Profile.objects.get(id=self.user.id)

        # 初期タグ
        post_tag = Tag()
        post_tag.name = 'テストタグ'
        post_tag.save()
        self.tag = Tag.objects.get(id=post_tag.id)

    def test_is_empty(self):
        saved_post = Post.objects.all()
        self.assertEqual(saved_post.count(), 0)

    def test_saveing_and_retrieving_post(self):
        # DBに保存されるかの確認
        user_post = Post()
        user_post.author = self.user
        user_post.profile = self.user_profile
        # user_post.photo = self.user_profile
        user_post.text = 'テスト投稿です'
        user_post.pr1 = 'おすすめ1'
        user_post.pr2 = 'おすすめ2'
        user_post.pr3 = 'おすすめ3'
        user_post.pr4 = 'おすすめ4'
        # user_post.tag = 'タグ'
        user_post.car_type = 'カローラ'
        user_post.price = 5000
        user_post.place = '福岡県福岡市博多区'
        user_post.save()

        saves_all_user_post = Post.objects.all()
        self.assertEqual(saves_all_user_post.count(), 1)


class MessageModelTest(TestCase):
    """メッセージモデル"""

    def setUp(self):
        # 初期ユーザーデータ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

        # 初期プロフィールデータ
        first_user_profile = Profile()
        first_user_profile.userpro = self.user
        first_user_profile.introduction = 'テストユーザーです。宜しくお願いします。'
        first_user_profile.address = '福岡県福岡市博多区'
        first_user_profile.save()
        self.user_profile = Profile.objects.get(id=self.user.id)

    def test_is_empty(self):
        saved_message = Message.objects.all()
        self.assertEqual(saved_message.count(), 0)

    def test_saveing_and_retrieving_message(self):
        # DBに保存されるかの確認
        user_message = Message()
        user_message.message = 'テストユーザーさん、元気ですか？'
        user_message.sender = self.user
        user_message.receiver = self.user
        user_message.profile = self.user_profile
        user_message.save()

        saves_all_user_message = Message.objects.all()
        self.assertEqual(saves_all_user_message.count(), 1)
