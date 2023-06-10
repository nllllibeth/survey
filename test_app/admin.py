from django.contrib import admin
from .models import Test, Test_form, Question

# Register your models here.
admin.site.register(Test)
admin.site.register(Test_form)
admin.site.register(Question)