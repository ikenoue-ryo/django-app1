from django.contrib.auth import get_user_model
from django.utils.timezone import localtime
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, Tag, Profile

class TestTagCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/tag/'

    def test_create_success(self):
        """タグモデル"""

        params = {
            'name': 'tag_test'
        }
        response = self.client.post(self.TARGET_URL, params, format='json')
        print('タグタグ', response)

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
        

class TestProfileCreateAPIView(APITestCase):

    TARGET_URL = '/api/v1/profile/'

    def setUp(self):
        # 初期ユーザーデータ
        self.user = User.objects.create_user('test@gmail.com', 'test_user')

    def test_create_success(self):
        """プロフィールモデル"""
        print('1', self.user.id)
        print('2', self.user.username)
        data = {
            'id': self.user.id,
            'username': self.user.username,
        }

        params = {
            'introduction': 'こんにちは',
            'address': '福岡県福岡市博多区',
            'userpro.id': self.user.id,
            'userpro.username': self.user.username,
            "icon": "https://vue-django.s3.amazonaws.com/static/image/batman.png"
        }
        response = self.client.post(self.TARGET_URL, params, format='json')
        print('response', response)

        # DBの状態を検証
        self.assertEqual(Profile.objects.count(), 1)


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
