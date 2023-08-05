# app/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        response = self.client.post('/api/register/', {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_user(self):
        # Assuming a user with 'test@example.com' already exists
        response = self.client.post('/api/register/', {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authenticate_user(self):
        response = self.client.post('/api/token/', {
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)

    def test_authenticate_invalid_user(self):
        response = self.client.post('/api/token/', {
            'email': 'nonexistent@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post(self):
        # Assuming you have a valid JWT token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/posts/', {
            'title': 'Test Post',
            'description': 'This is a test post description'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_missing_title(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/posts/', {
            'description': 'This is a test post description'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Add more test cases following a similar pattern
    def test_follow_user(self):
        # Assuming you have a valid JWT token and user IDs
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/follow/2/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_follow_nonexistent_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/follow/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unfollow_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/unfollow/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unfollow_nonexistent_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/unfollow/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)
        self.assertIn('followers', response.data)
        self.assertIn('followings', response.data)

    def test_create_and_delete_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer valid_jwt_token')
        response = self.client.post('/api/posts/', {
            'title': 'Test Post',
            'description': 'This is a test post description'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post_id = response.data['id']

        response = self.client.delete(f'/api/posts/{post_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
