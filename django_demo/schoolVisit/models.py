from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Visit(models.Model):
    STATUS = [
        ('planned','Planned'),
        ('done','Done'),
    ]

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateField()
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS)