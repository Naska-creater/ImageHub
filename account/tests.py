from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from account.models import User


class UserRegistrationAPITestCase(APITestCase):

    def setUp(self):
        self.url = reverse('user/registration/')

    def test_user_registration(self):
        data = {
            'first_name': 'testuser',
            'second_name': 'testusertest',
            'email': 'testuser@mail.ru',
            'phone': '12345',
            'password': '12345',
            'nick_name': 'testuser'
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().nick_name, 'testuser')

class UserChangeAPIViewTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('user/change/')

    def test_get_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_patch_user(self):
        data = {
            'first_name': 'UpdatedName',
            'second_name': 'UpdatedSurname'
        }
        response = self.client.patch(self.url, data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.first_name, 'UpdatedName')
        self.assertEqual(self.user.second_name, 'UpdatedSurname')

    def test_delete_user(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(get_user_model().objects.filter(id=self.user.id).exists())

class AdminChangeGenericAPIViewTests(APITestCase):

    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='12345',
            first_name='Admin',
            second_name='Admin'
        )
        self.client.force_authenticate(user=self.admin_user)

        self.user = User.objects.create_user(
            email='test@example.com',
            password='12345',
            first_name='Test',
            second_name='User',
            phone='1234567890'
        )

    def test_get_users(self):
        response = self.client.get(reverse('admin/view/'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.email, [u['email'] for u in response.data])

    def test_patch_user(self):
        url = reverse('admin/change/', kwargs={'pk': self.user.pk})
        data = {'first_name': 'UpdatedName'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')

    def test_delete_user(self):
        url = reverse('admin/change/', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())