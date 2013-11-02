from django.db import models

# Create your models here.

class Person(models.Model):
    """Represents a person"""
    class Meta:
        ordering = ["last_name"]
        verbose_name_plural = "People"

    address = models.CharField(max_length=30) # Prof. Dr. Dr. hc. mult.
    first_name = models.CharField(max_length=30) 
    last_name =  models.CharField(max_length=30) 
    # and more
    # quest, favorite color, ... http://www.youtube.com/watch?v=pWS8Mg-JWSg

    def _get_full_name(self): # TODO: i18n proper formatting
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

    def __unicode__(self):
        return self.full_name

class Course(models.Model):
    """Represents a single course"""
    # TODO Brain: should we use a table for this? 
    NO_CATEGORY = 'NO'
    INTEGRATED_COURSE = 'IV' # integrierte Veranstaltung
    LECTURE = 'VL'           # Vorlesung
    SEMINAR = 'SE'           # Seminar
    PROJECT = 'PR'           # Projekt
    COLLOQUIUM = 'CO'        # Kolloquium

    CATEGORY_CHOICES = (
        # TODO Brain: do we need this? 
        (NO_CATEGORY, 'Kein Veranstaltungstyp'), 
        (INTEGRATED_COURSE, 'Integrierte Veranstaltung'),
        (LECTURE, 'Vorlesung'),
        (SEMINAR, 'Seminar'),
        (PROJECT, 'Projekt'),
        (COLLOQUIUM, 'Kolloquium'),
    )
    
    number = models.CharField(max_length=15) # is this enough room? 
    title = models.CharField(max_length=50) 
    credit_points = models.IntegerField()
    # can't use 'type' ;) it's a keyword in python
    category = models.CharField(max_length=2, 
                                choices=CATEGORY_CHOICES, 
                                default='NO'),
    people = models.ManyToManyField(Person)
    first_meeting = models.DateTimeField()
    first_meeting_at = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s (%d CP)' % (self.title, self.credit_points)

# TODO: Missing so far: CourseComponent

class Module(models.Model):
    """Represents a module"""
    title = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course) # managed by Django for now

    def _get_cp_sum(self):
        return 42 # FIXME! 

    credit_points = property(_get_cp_sum)

    def __unicode__(self):
        return '%s' % self.title

# TODO: Is "Major" a good name in this context? 
# probably not ... but I can't come up with a
# better one at the moment
class Major(models.Model):
    """Represents an academic major"""
    class Meta:
        ordering = ['name']
    # Computer Science, Human Factors ...
    name = models.CharField(max_length=50)
    modules = models.ManyToManyField(Module, through='ModuleMembership')

    def __unicode__(self):
        return '%s' % self.name

class ModuleMembership(models.Model):
    """
    Represents the relationship between Major and Module

    There's an additional field named degree that represents 
    the intended degree in this relationship.
    """

    BACHELOR_OF_ARTS = "BA"
    BACHELOR_OF_SCIENCE = "BSC"
    MASTER_OF_ARTS = "MA"
    MASTER_OF_SCIENCE = "MSC"
    DIPLOMA = "DIP"

    DEGREE_CHOICES = (
        (BACHELOR_OF_ARTS, "BA"),
        (BACHELOR_OF_SCIENCE, "BSc"),
        (MASTER_OF_ARTS, "MA"),
        (MASTER_OF_SCIENCE, "MSc"),
        (DIPLOMA, "Diplom"),
    )

    module = models.ForeignKey(Module)
    major = models.ForeignKey(Major)
    degree = models.CharField(  max_length=3, 
                                choices=DEGREE_CHOICES,
                                default=BACHELOR_OF_SCIENCE) # TODO!


    def __unicode__(self):
        return "Module %s for %s (%s)" % (  module.title, 
                                            major.name, 
                                            DEGREE_CHOICES[self.degree])


        
    