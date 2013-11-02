from django.contrib import admin
from nlpagent.models import Person, Course, Module, Major, ModuleMembership

admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Major)
admin.site.register(ModuleMembership)