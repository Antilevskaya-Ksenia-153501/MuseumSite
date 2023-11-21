from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound
from . forms import ExhibitForm, ReviewForm
from . models import *
import requests
import datetime
from datetime import date
import matplotlib.pyplot as plt
from django.conf import settings
import os
from .api_urls import API_URLS
from django.db.models import Q


def list_exhibits(request):
    if not request.user.is_authenticated:
        exhibits = Exhibit.objects.all()
    elif  request.user.is_employee and not request.user.is_superuser:
        exhibits = Exhibit.objects.filter(employee_id=request.user.id)
    else:
        exhibits = Exhibit.objects.all()
    return render(request, 'list_exhibits.html', {'exhibits': exhibits})


def list_halls(request):
    halls = Hall.objects.all()
    return render(request, 'list_halls.html', {'halls': halls})


def list_employees(request):
    employees = authorization.models.Employee.objects.all()
    return render(request, 'list_employees.html', {'employees':employees})


def exhibit_details(request, id):
    exhibit = get_object_or_404(Exhibit, id=id)
    return render(request, 'exhibit_details.html', {'exhibit': exhibit})


def edit_exhibit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    exhibit = None
    try:
        exhibit = get_object_or_404(Exhibit, id=id)
    except:
        return HttpResponseNotFound('<h2>No such exhibit</h2>')
    form = ExhibitForm(instance=exhibit)
    if request.method == "POST":
        form = ExhibitForm(request.POST, instance=exhibit)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ExhibitForm(instance=exhibit)
    return render(request, 'edit_exhibit.html', {'form': form, 'exhibit': exhibit})


def delete_exhibit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    try:
        exhibit = get_object_or_404(Exhibit, id=id)
        exhibit.delete()
        return redirect('/')
    except:
        return HttpResponseNotFound('<h2>No such exhibit</h2>')


def create_exhibit(request):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    form = ExhibitForm()
    if request.method == "POST":
        form = ExhibitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exhibits')
        else:
            form = ExhibitForm()
    return render(request, 'create_exhibit.html', {'form': form})


def list_recent_exhibits(request):
    td=datetime.date.today()
    diff = date(td.year, td.month-6, td.day)
    recent_exhibits=Exhibit.objects.filter(receiptDate__gte=diff)
    return render(request, 'list_recent_exhibits.html', {'recent_exhibits': recent_exhibits})


def list_excursions(request):
    if request.user.is_staff and not request.user.is_superuser:
        excursions = Excursion.objects.filter(employee_id=request.user.id)
    else:
        excursions=Excursion.objects.all()
    return render(request, 'list_excursions.html', {'excursions': excursions})


def list_employeesearch(request):
    query = int('0' + request.GET.get("floor"))
    employees_id = Hall.objects.filter(floor=query).values_list('employee', flat = True)
    employees=[]
    for obj in employees_id:
        employees.append(authorization.models.Employee.objects.get(id=obj))
    return render(request, 'search_results.html', {'employees': employees})


def excursion_by_season(request):
    choosen_season = request.GET.get('seasons')
    excursions=[]
    if choosen_season == "winter":
        # Q(date__month=1) | Q(date__month=2) | Q(date__month=12)
        excursions = Excursion.objects.filter(date__month__in=[12, 1, 2])
    elif choosen_season == "spring":
        excursions = Excursion.objects.filter(date__month__in=[3, 4, 5])
    elif choosen_season == "summer":
        excursions = Excursion.objects.filter(date__month__in=[6, 7, 8])
    elif choosen_season == "autumn":
        excursions = Excursion.objects.filter(date__month__in=[9, 10, 11])
    return  render(request, 'excursion_by_season.html', {'excursions':  excursions})


def about(request):
    return render(request, 'about_us.html')


def questions(request):
    questions = FrequentlyAskedQuestion.objects.all()
    return render(request, 'faq.html', {'questions': questions})


def get_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews':reviews})


# def create_review(request):
#     if not request.user.is_authenticated or not request.user.is_customer:
#         return render(request, 'register.html', {'form': authorization.forms.CustomerCreateForm})
#     form = ReviewForm()
#     if request.method == "POST":
#         form = ReviewForm(request.POST, request.FILES)
#         form.author = request.user
#         form.review_date = datetime.date.today()
#         if form.is_valid():
#             # form.fields['author'].value = request.user
#             # form.fields['review_date'].value = datetime.date.today()
#             # form.save()
#             stars = form.cleaned_data['stars']
#             comment = form.cleaned_data['comment']
#             review = Review(author=authorization.models.Customer.objects.get(email=request.user.email), comment=comment, stars=stars, review_date=datetime.date.today())
#             review.save() 
#             return redirect('reviews')
#         else:
#             form = ReviewForm()
#     return render(request, 'create_review.html', {'form': form})


def create_review(request):
    if not request.user.is_authenticated or not request.user.is_customer:
        return render(request, 'register.html', {'form': authorization.forms.CustomerCreateForm})
    if request.method == "POST":
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=authorization.models.Customer.objects.get(email=request.user.email), comment=comment, stars=stars, review_date=datetime.date.today())
        review.save() 
        return redirect('reviews')
    else:
         return render(request, 'create_review.html')


def contacts(request):
    employees = authorization.models.Employee.objects.all()
    return render(request, 'contacts.html', {'employees': employees})


def home(request):
    article = NewsArticle.objects.order_by('-pub_date').first()
    response = requests.get(API_URLS['random_quote'])
    random_quote = None
    if (response.status_code == 200 and request.user.is_authenticated):
        data = response.json()
        random_quote = data['quote']['body']
    return render(request, 'home.html', {'article': article, 'random_quote': random_quote})
    return render(request, 'home.html', {'article': article})


def news_list(request):
    articles = NewsArticle.objects.all()
    return render(request, 'news_list.html', {'articles': articles})


def news_details(request, article_id):
    article = NewsArticle.objects.get(id=article_id)
    return render(request, 'news_details.html', {'article': article})


def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies':vacancies})


def get_policy(request):
    return render(request, 'policy.html')


def get_coupons(request):
    coupons = Coupon.objects.all()
    return render(request, 'coupons.html', {'coupons':coupons})


def show_analytics(request):
    if not request.user.is_superuser:
        raise PermissionDenied("No access")

    excursions = dict()
    winterEx = Excursion.objects.filter(date__month__in=[12, 1, 2])
    excursions["winter"] = winterEx.count()
    springEx = Excursion.objects.filter(date__month__in=[3, 4, 5])
    excursions["spring"] = springEx.count()
    summerEx = Excursion.objects.filter(date__month__in=[6, 7, 8])
    excursions["summer"] = summerEx.count()
    autumnEx = Excursion.objects.filter(date__month__in=[9, 10, 11])
    excursions["autumn"] = autumnEx.count()

    seasons = list(excursions.keys())
    excursion_count = list(excursions.values())

    plt.bar(seasons, excursion_count)
    plt.xlabel('Season')
    plt.ylabel('Number of excursions')
    # plt.plot(x, y)
    if request.method == "GET":
        plt.savefig(os.path.join(settings.MEDIA_ROOT, 'excursions_per_seasons.png'), format='png')
        plt.close()
    return render(request, 'analytics.html')

def military(request):
    return render(request, 'military.html')