from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('exhibits/', views.list_exhibits, name='exhibits'),
    path('<int:id>', views.exhibit_details, name='exhibit_details'),
    path('edit_exhibit/<int:id>/', views.edit_exhibit, name='edit_exhibit'),
    path('delete_exhibit/<int:id>/', views.delete_exhibit, name='delete_exhibit'),
    path('create_exhibit/', views.create_exhibit, name='create_exhibit'),
    path('halls/', views.list_halls, name='halls'),
    path('employees/', views.list_employees, name='employees'),
    path('excursions/', views.list_excursions, name='excursions'),
    path('recent/', views.list_recent_exhibits, name='recent_exhibits'),
    path('search/', views.list_employeesearch, name='search_results'),
    path('sort_by_season/', views.excursion_by_season, name='sort_by_seasons'),
    path('about_us/',views.about, name='about_us'),
    path('contacts/',views.contacts, name='contacts'),
    path('faq/',views.questions, name='questions'),
    path('reviews/',views.get_reviews, name='reviews'),
    path('add_review/', views.create_review, name='create_review'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:article_id>', views.news_details, name='news_details'),
    path('vacancy/', views.get_vacancies, name='vacancies'),
    path('policy/', views.get_policy, name='policy'),
    path('coupons/', views.get_coupons, name='coupons'),
    path('analytics/', views.show_analytics, name='analytics'),

]