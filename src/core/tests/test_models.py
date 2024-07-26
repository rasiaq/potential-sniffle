from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalize(self):
        email = 'test@ExAmple.com'
        email_match = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email_match)
        self.assertTrue(user.check_password(password))

    def test_create_user_missing_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password="test123"
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
