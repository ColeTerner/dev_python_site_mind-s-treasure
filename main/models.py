from django.db import models

# Create your models here.
    #Class of table with its fields like properties of the class
class Task(models.Model):
    title = models.CharField('Название',max_length=50)          #
    task = models.TextField('Описание',)

    #Function, which uses while table is called(returns title)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Задачи'
        verbose_name_plural= 'Задачи'

