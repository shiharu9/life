from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=20, verbose_name='Event name')
    content = models.TextField(verbose_name='Description')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    period = models.ForeignKey('Period', on_delete=models.PROTECT)

    class Meta:
        ordering = ['published']


class Period(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
