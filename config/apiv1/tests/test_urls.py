from django.urls import resolve
from django.test import TestCase

from apiv1.views import UserViewSet, PostViewSet, TagViewSet, ProfileViewSet, CommentViewSet


class UrlResolveTests(TestCase):

    def test_url_resolve_user_view(self):
        """UserViewSetが呼び出されるかの検証"""
        found = resolve('/api/v1/user/')
        self.assertEqual(found.func.__name__, UserViewSet.__name__)

    def test_url_resolve_post_view(self):
        """PostViewSetが呼び出されるかの検証"""
        found = resolve('/api/v1/posts/')
        self.assertEqual(found.func.__name__, PostViewSet.__name__)

    def test_url_resolve_tag_view(self):
        """TagViewSetが呼び出されるかの検証"""
        found = resolve('/api/v1/tag/')
        self.assertEqual(found.func.__name__, TagViewSet.__name__)

    def test_url_resolve_profile_view(self):
        """ProfileViewSetが呼び出されるかの検証"""
        found = resolve('/api/v1/profile/')
        self.assertEqual(found.func.__name__, ProfileViewSet.__name__)

    def test_url_resolve_comment_view(self):
        """CommentViewSetが呼び出されるかの検証"""
        found = resolve('/api/v1/comment/')
        self.assertEqual(found.func.__name__, CommentViewSet.__name__)