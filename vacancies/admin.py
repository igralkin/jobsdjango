from django.contrib import admin
from .models import Specialty, Company, Vacancy, Application

admin.site.register(Specialty)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Application)
