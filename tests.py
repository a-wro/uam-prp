import unittest
from django.test import TestCase

from djmoney.money import Money

class ClientTest(TestCase):
    #check if client can view the book list
    def testGET(self):
        #GET request.
        response = self.client.get('/library/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    #checks if client can add a book properly
    def testPOST(self):
        response = self.client.post('/library/create/', 
                {'title': 'test', 
                'slug': 'test', 
                'price': Money(5, 'EUR'),
                'description':'test',}
                )
    #checks the serializer url
    def testIndex(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

