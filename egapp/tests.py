from django.test import TestCase

#Some sources for ideas:
# https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/
# Create your tests here.
import unittest
from selenium import webdriver

class TestEgApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_basic_urls(self):
        self.driver.get("http://localhost:8000/egapp/")
        self.driver.get("http://localhost:8000/egapp/1")
        self.driver.get("http://localhost:8000/egapp/1/")
        self.driver.get("http://localhost:8000/egapp/1/orange")
        self.driver.get("http://localhost:8000/egapp/1/purple")
        self.driver.get("http://localhost:8000/egapp/arbitrary/2*X")
        self.driver.get("http://localhost:8000/egapp/1/barf")

if __name__ == '__main__':
    unittest.main()