from django.db.models import CharField, IntegerField, DateField

from datetime import date


class HumanMixin():
    first_name = CharField(verbose_name='Имя', max_length=30)
    last_name = CharField(verbose_name='Фамилия', max_length=150)
    patronymic = CharField(verbose_name='Отчество', max_length=150, blank=True)
    date_of_birth = DateField()
    place_of_birth = CharField(max_length=100)
    

    def get_age(self):
        return date.today() - self.date_of_birth