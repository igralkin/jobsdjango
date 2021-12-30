from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return f'{self.title}'


class Company(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=3000)
    employee_count = models.IntegerField()

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
