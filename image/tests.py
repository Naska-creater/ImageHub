from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from account.models import User
from image.models import Category, Image

class CategoryAdminAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            first_name='testadmin',
            second_name='testadmintest',
            email='testadmin@mail.ru',
            password='12345',
            phone='12345')

        self.client.force_authenticate(user=self.admin_user)
        self.category_data = {'name': 'Test Category_1'}
        self.category = Category.objects.create(**self.category_data)

    def test_view_categories(self):
        url = reverse('category/create/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.category.name, [cat['name'] for cat in response.data])

    def test_create_category(self):
        url = reverse('category/create/')
        new_category_data = {'name': 'Test Category_2'}
        response = self.client.post(url, new_category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_update_category(self):
        url = reverse('category/change/', kwargs={'pk': self.category.pk})
        updated_data = {'name': 'Updated Category'}
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category_1')

    def test_delete_category(self):
        url = reverse('category/change/', kwargs={'pk': self.category.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

class CategoryUserAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            first_name='admin',
            second_name='admin',
            email='admi@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.category_data = {'name': 'Test Category'}
        self.category = Category.objects.create(**self.category_data)

        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )

    def test_view_categories(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('categories/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.category.name, [cat['name'] for cat in response.data])

class ImagesViewAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            first_name='admin',
            second_name='admin',
            email='admi@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.image_data = {'name': 'Test Image', 'file': 'D:\HomeWork_IT\ImageHub\image\image\птица.jpeg'}
        self.image = Image.objects.create(**self.image_data)

        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )

    def test_view_all_images(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('images/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.image.name, [img['name'] for img in response.data])

class ImageUserAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            first_name='admin',
            second_name='admin',
            email='admi@mail.ru',
            password='12345',
            phone='12345'
        )
        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_image(self):
        url = reverse('create/')
        image_data = {
            'file': 'D:\HomeWork_IT\ImageHub\image\image\птица.jpeg',
            'description': 'Test Image'
        }
        response = self.client.post(url, image_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get().user, self.user)

    def test_delete_own_image(self):
        image = Image.objects.create(user=self.user, image='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg')
        url = reverse('change/', kwargs={'pk': image.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Image.objects.count(), 0)

    def test_delete_other_image(self):
        other_user_image = Image.objects.create(user=self.admin_user, image='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg')
        url = reverse('change/', kwargs={'pk': other_user_image.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Image.objects.count(), 1)

    def test_update_own_image(self):

        image = Image.objects.create(user=self.user, image='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg')
        url = reverse('change/', kwargs={'pk': image.pk})
        updated_data = {
            'description': 'Updated Image Description'
        }
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        image.refresh_from_db()
        self.assertEqual(image.description, 'Updated Image Description')

    def test_update_other_image(self):

        other_user_image = Image.objects.create(user=self.admin_user, image='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg')
        url = reverse('change/', kwargs={'pk': other_user_image.pk})
        updated_data = {
            'description': 'Updated Image Description'
        }
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        other_user_image.refresh_from_db()
        self.assertNotEqual(other_user_image.description, 'Updated Image Description')


class MyImageGenericAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.user)

        self.image1 = Image.objects.create(name='Image 1', file='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg', user=self.user)

    def test_get_user_images(self):
        url = reverse('my/')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        image_names = [img['name'] for img in response.data]
        self.assertIn(self.image1.name, image_names)

class ImageAdminAPITestCase(APITestCase):
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            first_name='testuser',
            second_name='testusertest',
            email='testuser@mail.ru',
            password='12345',
            phone='12345'
        )
        self.client.force_authenticate(user=self.user)
        self.image = Image.objects.create(user=self.user, image='D:\HomeWork_IT\ImageHub\image\image\птица.jpeg')

        self.admin_user = get_user_model().objects.create_superuser(
            first_name='admin',
            second_name='admin',
            email='admi@mail.ru',
            password='12345',
            phone='12345'
        )

    def test_update_image(self):

        url = reverse('change/', kwargs={'pk': self.image.pk})
        updated_data = {
            'description': 'Updated Image Description'
        }
        self.client.force_authenticate(user=self.admin_user)

        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.image.refresh_from_db()
        self.assertEqual(self.image.description, 'Updated Image Description by Admin')

    def test_delete_image(self):
        url = reverse('change/', kwargs={'pk': self.image.pk})

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Image.objects.count(), 0)
