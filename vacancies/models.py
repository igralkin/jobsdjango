from django.contrib.auth.models import User
from django.db import models

from jobsdjango.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    #picture = models.URLField(default='https://place-hold.it/100x60')
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return f'{self.title}'


class Company(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    #logo = models.URLField(default='https://place-hold.it/100x60')
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=3000)
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    skills = models.CharField(max_length=1200)
    description = models.CharField(max_length=3000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')

    def __str__(self):
        return f'{self.title}'


class Application(models.Model):
    # отклики

    written_username = models.CharField(max_length=300)  # Имя
    written_phone = models.CharField(max_length=300)  # Телефон
    written_cover_letter = models.TextField()  # Сопроводительное письмо

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='applications')

    def __str__(self):
        return f'{self.written_username} {self.written_phone}'

