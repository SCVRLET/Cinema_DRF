from datetime import date

from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    synopsis = models.TextField(max_length=1000, verbose_name='Синопсис')
    budget_in_dollars = models.PositiveIntegerField(verbose_name='Бюджет (в долларах)')
    box_office_in_dollars = models.PositiveIntegerField(verbose_name='Сборы (в долларах)',
        blank=True)
    world_premier = models.DateField(verbose_name='Мировая премьера')
    duration_in_minutes = models.PositiveIntegerField(verbose_name='Длительность (в минутах)')
    certificate = models.CharField(max_length=3, verbose_name='Возрастное ограничение')
    countries = models.CharField(max_length=150, verbose_name='Страны')
    tagline = models.CharField(max_length=70, verbose_name='Слоган',
        blank=True)
    genres = models.ManyToManyField('MovieGenre', related_name='films_with_genre', verbose_name='Жанр')
    directors = models.ManyToManyField('Person', related_name="films_as_director", verbose_name='Режиссер')
    actors = models.ManyToManyField('Person', related_name="films_as_actor", verbose_name='актеры')
    scenarists = models.ManyToManyField('Person', related_name="films_as_scenarist", verbose_name='Сценарист')
    operators = models.ManyToManyField('Person', related_name="films_as_operator", verbose_name='Оператор')
    composers = models.ManyToManyField('Person', related_name="films_as_composer", verbose_name='Композитор')


class Serial(Movie, models.Model):
    total_episodes_count = models.PositiveIntegerField(verbose_name='Всего серий')
    total_seasons_count = models.PositiveIntegerField(verbose_name='Всего сезонов')
    last_season_date = models.DateField(verbose_name='Дата выхода последнего сезона')
    average_episode_duration_in_minutes = models.PositiveIntegerField(
        verbose_name='Средняя продолжительность одной серии (в минутах)')


class MovieGenre(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    patronymic = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения')
    
    def get_age(self):
        return date.today() - self.date_of_birth

    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)