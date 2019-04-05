import json
from django.test import TestCase


class BaseTest(TestCase):
    """
    Trivial assertions for code transparency
    """
    
    def assertReponseWithModelInDB(self, response, queryset, instance):
        response = json.loads(response.content)
        for resp, query in zip(response, queryset):
            self.assertEqual(resp, instance(query).data)
    
    def assertIfObjectExist(self, queryset):
        self.assertTrue(queryset)
    
    def assertIfObjectNotExist(self, queryset):
        self.assertFalse(queryset)
