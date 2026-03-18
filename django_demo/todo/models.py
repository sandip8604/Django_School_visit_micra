from django.db import models

class user(models.Model):
    usr_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=100,default="")
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username