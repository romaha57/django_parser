from django.db import models


class Vacancy(models.Model):
    link = models.URLField(verbose_name='ссылка на вакансию')
    logo = models.CharField(max_length=255, verbose_name='ссылка на логотип', null=True)
    title = models.TextField(verbose_name='заголовок')
    requirements = models.TextField(verbose_name='краткое описание', null=True)
    meta_data = models.CharField(max_length=255, verbose_name='доп. информация')
    date = models.DateTimeField(verbose_name='дата публикации')
    company_name = models.CharField(max_length=100, verbose_name='название компании')
    salary = models.CharField(max_length=100, verbose_name='зарплата')
    city_name = models.CharField(max_length=100, verbose_name='город', default='россия')
    language = models.CharField(max_length=100, verbose_name='язык програмирования', default='python')

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        ordering = ('-date',)
        unique_together = ('link', 'city_name', 'language')

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name='город')
    id_for_habr = models.CharField(max_length=20, verbose_name='id города на habr')
    id_for_hh = models.CharField(max_length=20, verbose_name='id города на hh')

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=40, verbose_name='язык программирования')

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'

    def __str__(self):
        return self.name

