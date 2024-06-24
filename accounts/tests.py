from django.test import TestCase

# Create your tests here.

class AuthTestCase(TestCase):
    def test_login(self):
        response = self.client.post('/accounts/login/', {'username': 'test
                                                         