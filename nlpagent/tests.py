"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from nlpagent.models import Person

class SimpleTest(TestCase):
    def test_person_title_not_obligatory(self):
        """
        The title field in person should not be obligatory
        """
        p = Person(first_name="John", last_name="Doe")
        p.save()
        self.assertEqual(Person.objects.get(pk=p.id).title, "")