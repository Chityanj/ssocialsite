# app/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post

User = get_user_model()

class AuthenticationAPITestCase(APITestCase):
    def test_authenticate_user(self):
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post('/api/authenticate/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

    def test_authenticate_user_existing(self):
        # Create a user first
        user = User.objects.create_user(email='existing@example.com', username='existing@example.com', password='existingpassword')
        data = {'email': 'existing@example.com', 'password': 'existingpassword'}
        response = self.client.post('/api/authenticate/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

class FollowUnfollowAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1@example.com', username='user1', password='user1password')
        self.user2 = User.objects.create_user(email='user2@example.com', username='user2', password='user2password')
        self.client1 = self.client_class()
        self.client1.force_login(self.user1)

    def test_follow_user(self):
        response = self.client1.post(f'/api/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user1.following.count(), 1)

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        response = self.client1.post(f'/api/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user1.following.count(), 0)

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', username='testuser', password='testpassword')
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_post(self):
        self.authenticate()

        data = {'title': 'Test Post', 'description': 'This is a test post'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_post_missing_fields(self):
        self.authenticate()

        data = {'title': 'Test Post'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 0)

    def test_get_all_posts(self):
        # Create some test posts
        Post.objects.create(title='Post 1', description='Description 1', author=self.user)
        Post.objects.create(title='Post 2', description='Description 2', author=self.user)

        response = self.client.get('/api/all_posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_post(self):
        post = Post.objects.create(title='Test Post', description='This is a test post', author=self.user)

        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_delete_post(self):
        self.authenticate()

        post = Post.objects.create(title='Test Post', description='This is a test post', author=self.user)

        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_like_post(self):
        self.authenticate()

        post = Post.objects.create(title='Test Post', description='This is a test post', author=self.user)

        response = self.client.post(f'/api/like/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.likes.count(), 1)

    def test_unlike_post(self):
        self.authenticate()

        post = Post.objects.create(title='Test Post', description='This is a test post', author=self.user)
        self.user.profile.liked_posts.add(post)

        response = self.client.post(f'/api/unlike/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.likes.count(), 0)  