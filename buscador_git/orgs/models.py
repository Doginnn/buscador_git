from django.db import models


class Org(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Empresa')
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name
