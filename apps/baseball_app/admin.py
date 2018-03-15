# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        model = Player


admin.site.register(Player, PlayerAdmin)