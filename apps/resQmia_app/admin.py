# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

class DogAdmin(admin.ModelAdmin):
    class Meta:
        model = Dog

class VaccineDogAdmin(admin.ModelAdmin):
    class Meta:
        model = VaccineDog

class PreventionDogAdmin(admin.ModelAdmin):
    class Meta:
        model = VaccineDog

class TestDogAdmin(admin.ModelAdmin):
    class Meta:
        model = TestDog


class CatAdmin(admin.ModelAdmin):
    class Meta:
        model = Cat

class VaccineCatAdmin(admin.ModelAdmin):
    class Meta:
        model = VaccineCat

class PreventionCatAdmin(admin.ModelAdmin):
    class Meta:
        model = VaccineCat

class TestCatAdmin(admin.ModelAdmin):
    class Meta:
        model = TestCat


admin.site.register(User, UserAdmin)

admin.site.register(Dog, DogAdmin)
admin.site.register(VaccineDog, VaccineDogAdmin)
admin.site.register(PreventionDog, PreventionDogAdmin)
admin.site.register(TestDog, TestDogAdmin)

admin.site.register(Cat, CatAdmin)
admin.site.register(VaccineCat, VaccineCatAdmin)
admin.site.register(PreventionCat, PreventionCatAdmin)
admin.site.register(TestCat, TestCatAdmin)

