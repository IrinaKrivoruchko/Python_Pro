from django.db import models

class Elixirs(models.Model):
    identifier = models.CharField('Identifier', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50, unique=True)

    class Meta:
        verbose_name = "Еліксир"
        verbose_name_plural = "Еліксири"
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    identifier = models.CharField('Identifier', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50, unique=True)

    class Meta:
        verbose_name = "Інгредієнт"
        verbose_name_plural = "Інгредієнти"

    def __str__(self):
        return self.name

class Houses(models.Model):
    identifier = models.CharField('Identifier', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50, unique=True)
    houseColours = models.CharField('HouseColours', max_length=50)
    founder = models.CharField('Founder', max_length=50)
    animal = models.CharField('Animal', max_length=50)
    element = models.CharField('Element', max_length=50)

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультети"
        ordering = ['name']

    def __str__(self):
        return self.name

class Spells(models.Model):
    identifier = models.CharField('Identifier', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = "Закляття"
        verbose_name_plural = "Закляття"

    def __str__(self):
        return self.name