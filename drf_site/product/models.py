from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20)
    product = models.ManyToManyField('Product', through='UserProduct')
    groups = models.ManyToManyField('Group', through='UserGroup')


class Teachers(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    price = models.CharField(max_length=5)
    count_lessons = models.PositiveIntegerField(default=56)
    min_students = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()
    count_groups = models.PositiveIntegerField()


class Group(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField(CustomUser)
    min_students = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class UserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)


class UserProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    video_link = models.URLField()





