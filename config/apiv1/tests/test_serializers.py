from django.test import TestCase
from users.models import Tag
from apiv1.serializers import TagSerializer


class TestTagSerializer(TestCase):
    """TagSerializerのテストクラス"""

    def test_input_valid(self):
        """入力データのバリデーション(OK)"""

        # シリアライザの作成
        input_data = {
            'name': 'tag_name',
        }
        serializer = TagSerializer(data=input_data)

        # バリデーションの結果を検証
        self.assertEqual(serializer.is_valid(), True)

    def test_input_valid_if_title_is_blank(self):
        """入力データのバリデーション（NG）"""

        # シリアライザの作成
        input_data = {
            'name': '',
        }
        serializer = TagSerializer(data=input_data)

        # バリデーションの結果を検証
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ['name'])
        self.assertCountEqual(
            [x.code for x in serializer.errors['name']],
            ['blank']
        )

    def test_output_data(self):
        """出力データの内容検証"""

        # シリアライザの作成
        tag = Tag.objects.create(
            name='tag_name'
        )
        serializer = TagSerializer(instance=tag)

        # シリアライザの出力内容を検証
        expected_data = {
            'id': tag.id,
            'name': tag.name,
        }
        self.assertDictEqual(serializer.data, expected_data)
