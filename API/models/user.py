from django.db import models

    
class User(models.Model):

    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(auto_now=False,auto_now_add=False)
    password = models.CharField(max_length=30)

    def __str__(self):
        return '{} - {}: {}'.format(self.pk, self.first_name, self.email)

    