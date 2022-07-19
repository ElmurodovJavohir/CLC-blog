from django.contrib import admin

# Register your models here.

from django.apps import apps# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass