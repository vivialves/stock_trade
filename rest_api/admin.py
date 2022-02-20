# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Trade


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'timestamp_create', 'timestamp_update', 'status')

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'symbol', 'shares', 'price','timestamp_create', 'timestamp_update', 'status')