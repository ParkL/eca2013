"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.test import TestCase
from django.utils import timezone
from nlpagent.models import Person, Course, Module, Major, ModuleMembership

class SimpleTest(TestCase):
    def test_person_title_not_obligatory(self):
        """
        The title field in person should not be obligatory
        """
        p = Person.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(Person.objects.get(pk=p.id).title, "")

    def test_base_models(self):
        person = Person.objects.create( title="Dr.",
                                        first_name="Hubert",
                                        last_name="Fancypants")

        tomorrow = timezone.now() + datetime.timedelta(days=1)

        course = Course.objects.create(  number="2342 L 6972",
                                    title="The art of manufacturing pants",
                                    credit_points=6,
                                    category=Course.INTEGRATED_COURSE,
                                    first_meeting=tomorrow,
                                    first_meeting_at="Fancypants Pants Co.")
        course.people.add(person)
        course.save()

        module = Module.objects.create(title="Pants Manufacturing in EECS")
        module.courses.add(course)

        major = Major.objects.create(name="Computer Science")

        mm = ModuleMembership(  module=module,
                                major=major,
                                degree=ModuleMembership.DIPLOMA)
        mm.save()

        # Round robin
        self.assertTrue(major.modules.all()[0].
            courses.all()[0].people.all()[0].last_name, "Fancypants")

        # this is how we access membership info
        self.assertEquals(
            module.modulemembership_set.get(major=major).degree,
            ModuleMembership.DIPLOMA)

        # alternative
        self.assertEquals(
            ModuleMembership.objects.get(major=major, module=module).degree,
            ModuleMembership.DIPLOMA)

        # revers and count
        self.assertEquals(  person.course_set.all()[0].
                            module_set.all()[0].
                            major_set.count(), 1)



