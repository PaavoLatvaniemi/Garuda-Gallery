from django.test import TestCase
from django.urls import resolve
from django.urls import reverse
from .views import home
# Create your tests here.

def test_MainPage_view_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)

def test_MainPage_url_resolves_home_view(self):
    view = resolve('/')
    self.assertEquals(view.func, home)