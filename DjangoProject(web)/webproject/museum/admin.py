from django.contrib import admin
from . models import *


class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'floor', 'area')


admin.site.register(Hall, HallAdmin)


class TypeOfArtAdmin(admin.ModelAdmin):
    list_display = ('type',)


admin.site.register(TypeOfArt, TypeOfArtAdmin)


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('title', 'receiptDate',  'hall')
    list_filter = ('receiptDate',)


admin.site.register(Exhibit, ExhibitAdmin)


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'employee')

admin.site.register(Excursion, ExcursionAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'date')

admin.site.register(FrequentlyAskedQuestion, FAQAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'review_date')

admin.site.register(Review, ReviewAdmin)


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(NewsArticle, NewsArticleAdmin)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Vacancy, VacancyAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Coupon, CouponAdmin)



