from django.db import models
from django.urls import reverse

import authorization.models


class Hall(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=5)
    employee = models.ManyToManyField(authorization.models.Employee, related_name='halls')
    def __str__(self):
        return f" hall: {self.title}, {self.number}"


class TypeOfArt(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Exhibit(models.Model):
    title = models.CharField(max_length=100)
    typeOfArt = models.ManyToManyField(TypeOfArt, related_name='exhibits')
    receiptDate = models.DateField()
    employee = models.ForeignKey(authorization.models.Employee, on_delete=models.DO_NOTHING)
    hall = models.ForeignKey(Hall, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='exhibit/', null=True, blank=False, default='exhibit/default.jpg',
                              max_length=100)

    def get_absolute_url(self):
        return reverse('exhibit_details', args=[str(self.id)])

    def __str__(self):
        return f"exhibit: {self.title}"


class Excursion(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    numOfPpl = models.PositiveIntegerField()
    employee = models.ForeignKey(authorization.models.Employee, on_delete=models.DO_NOTHING)
    code = models.PositiveIntegerField()

    def __str__(self):
        return f"excursion: {self.title}"


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=False)
    date = models.DateField()


class Review(models.Model):
    author = models.ForeignKey(authorization.models.Customer, on_delete=models.DO_NOTHING)
    review_date = models.DateField()
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(blank=True)


class NewsArticle(models.Model):
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=False, default='news/default.png',
                              max_length=100)
    pub_date = models.DateField()


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.title


class Coupon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.PositiveIntegerField()
    valid_from = models.DateField()
    valid_to = models.DateField()

    def __str__(self):
        return self.title


