from io import BytesIO
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.timezone import localtime
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, Tag, Profile, Comment


class TestUserCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/user/'

    def test_create_success(self):
        """ユーザーモデル"""

        params = {
            'username': 'テストユーザー'
        }
        response = self.client.post(self.TARGET_URL, params, format='json')
        # print('user response', response.data)

        # DBの状態を検証
        self.assertEqual(User.objects.count(), 1)
        # レスポンスのステータス検証
        self.assertEqual(response.status_code, 201)
        user = User.objects.get()
        expected_json_dict = {
            'id': user.id,
            'username': user.username,
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    
    def test_create_bad_request(self):
        """ユーザーモデル"""

        # APIリクエストを実行
        params = {
            'username': ''
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # DBの状態を検証
        self.assertEqual(User.objects.count(), 0)
        # レスポンスのステータス検証
        self.assertEqual(response.status_code, 400)


class TestUserUpdateAPIView(APITestCase):

    TARGET_URL_WITH_PK = '/api/v1/user/{}/'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='secret',
        )

    def test_update_success(self):

        # Cookie認証ログイン
        # self.client.login(username='user', password='secret')

        # JWTログイン
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # APIリクエストを実行
        user = User.objects.create(
            username='テストユーザー'
        )
        params = {
            'id': user.id,
            'username': user.username,
        }
        response = self.client.put(
            self.TARGET_URL_WITH_PK.format(user.id), params, format='json',
        )
        
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(id=user.id)
        expected_json_dict = {
            'id': user.id,
            'username': user.username,
        }
        self.assertJSONEqual(response.content, expected_json_dict)


class TestTagCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/tag/'

    def test_create_success(self):
        """タグモデル"""

        params = {
            'name': 'tag_test'
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # DBの状態を検証
        self.assertEqual(Tag.objects.count(), 1)
        # レスポンスのステータス検証
        self.assertEqual(response.status_code, 201)
        tag = Tag.objects.get()
        expected_json_dict = {
            'id': tag.id,
            'name': tag.name,
        }
        # print('response.content', response.content)
        self.assertJSONEqual(response.content, expected_json_dict)

    
    def test_create_bad_request(self):
        """タグモデル"""

        # APIリクエストを実行
        params = {
            'name': '',
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # DBの状態を検証
        self.assertEqual(Tag.objects.count(), 0)
        # レスポンスのステータス検証
        self.assertEqual(response.status_code, 400)
        

class TestTagUpdateAPIView(APITestCase):

    TARGET_URL_WITH_PK = '/api/v1/tag/{}/'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='secret',
        )

    def test_update_success(self):

        # Cookie認証ログイン
        # self.client.login(username='user', password='secret')

        # JWTログイン
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # APIリクエストを実行
        tag = Tag.objects.create(
            name='tag_name'
        )
        params = {
            'id': tag.id,
            'name': tag.name,
        }
        response = self.client.put(
            self.TARGET_URL_WITH_PK.format(tag.id), params, format='json',
        )
        
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 200)
        tag = Tag.objects.get()
        expected_json_dict = {
            'id': tag.id,
            'name': tag.name,
        }
        self.assertJSONEqual(response.content, expected_json_dict)


class TestProfileCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/profile/'

    def setUp(self):
        # 初期ユーザーデータ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

    def test_create_success(self):
        """プロフィールモデル"""
        with BytesIO() as b:
            img = Image.new('L', (1, 1), 0)
            img.save(b, 'png')

            params = {
                'introduction': 'こんにちは',
                'address': '福岡県福岡市博多区',
                'userpro.id': self.user.id,
                'userpro.username': self.user.username,
                "icon": SimpleUploadedFile('dummy.png', b.getvalue()),
            }
            response = self.client.post(self.TARGET_URL, params)
            # print('response.data', response.data)

            # DBの状態を検証
            self.assertEqual(Profile.objects.count(), 1)

    def test_create_bad_request(self):
        """プロフィールモデル"""

        # APIリクエストを実行
        params = {
            'introduction': '',
            'address': '',
            'userpro.id': '',
            'userpro.username': '',
            'icon': '',
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # DBの状態を検証
        self.assertEqual(Profile.objects.count(), 0)
        # レスポンスのステータス検証
        self.assertEqual(response.status_code, 400)


class TestProfileUpdateAPIView(APITestCase):

    TARGET_URL_WITH_PK = '/api/v1/profile/{}/'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='secret',
        )

    def test_update_success(self):

        # Cookie認証ログイン
        # self.client.login(username='user', password='secret')

        # JWTログイン
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # APIリクエストを実行
        profile = Profile.objects.create(
            introduction='こんにちは',
            address='福岡県福岡市博多区',
            userpro=self.user,
        )
        params = {
            'id': profile.id,
            'introduction': profile.introduction,
            'address': profile.address,
            'userpro': profile.userpro.username,
        }
        # response = self.client.put(
        #     self.TARGET_URL_WITH_PK.format(profile.id), params, format='json',
        # )
        # print('オブジェクト', self.TARGET_URL_WITH_PK.format(profile.id))
        # print('params', params)


class TestCommentCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/comment/'

    def test_create_success(self):
        """コメントモデル"""
        
        user = User.objects.create(
            username='テストユーザー'
        )
        profile = Profile.objects.create(
            introduction='こんにちは',
            address='福岡県福岡市博多区',
            userpro=user,
        )

        params = {
            'username': user.username,
            'point':  5,
            'comment': 'ありがとうございました。',
            'profile': profile
        }
        response = self.client.post(self.TARGET_URL, params, format='json')
        # print('オブジェクト', response)
        print('params', params)

        # DBの状態を検証
        self.assertEqual(Comment.objects.count(), 1)