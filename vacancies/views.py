from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from .models import Specialty, Company, Vacancy


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    # Перезаписывается в tour_view и departure_view
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    # Главная страница сайта
    specialities = Specialty.objects.all()
    companies = Company.objects.all()
    context = {
        'specialities': specialities,
        'companies': companies,
    }
    print(specialities)
    return render(request, 'vacancies/index.html', context=context)


def vacancies_view(request):
    # Главная страница вакансий
    vacancies = Vacancy.objects.all()
    context = {
        'vacancies': vacancies
    }
    return render(request, 'vacancies/vacancies.html', context=context)


def vacancy_category_view(request, specialty_code):
    # Страница категории вакансий
    specialty_data = Specialty.objects.get(code=specialty_code)
    print(specialty_data)
    vacancies = Vacancy.objects.filter(specialty_id=specialty_data.id)

    context = {
        'vacancies': vacancies
    }
    return render(request, 'vacancies/vacancies.html', context=context)


def company_view(request, company_id):
    # Страница конкретной компании
    # from .mock_data import companies
    try:
        # company_data = companies[str(company_id)]
        company_data = Company.objects.get(id=company_id)
        print(company_data)
        vacancies = Vacancy.objects.filter(company_id=company_data.id)
        print(vacancies)
        context = {
            'company': company_data,
            'company_vacancies': vacancies
        }
    except KeyError:
        raise Http404(f"Компания с id {company_id} не найдена")
    except MultipleObjectsReturned:
        raise Http404(f"Дубликаты компаний в базе данных, конкретно: с id {company_id}")

    return render(request, 'vacancies/company.html', context=context)


def vacancy_view(request, vacancy_id):
    # Страница конкретной вакансии
    # from .mock_data import jobs

    try:
        # job_data = jobs[str(vacancy_id)]
        vacancy_data = Vacancy.objects.get(id=vacancy_id)
        print(vacancy_data)
        context = {
            'vacancy': vacancy_data
        }

    except KeyError:
        raise Http404(f"Компания с id {vacancy_id} не найдена")

    return render(request, 'vacancies/vacancy.html', context=context)
