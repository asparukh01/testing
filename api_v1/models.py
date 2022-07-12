from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    post = models.CharField(max_length=50, verbose_name='Должность')
    adopted_to_job = models.DateTimeField()
    salary = models.IntegerField()
    boss = models.ForeignKey('self', null=True, on_delete=models.PROTECT, related_name='employee')

    def __str__(self):
        return f'{self.pk}{self.post}'
