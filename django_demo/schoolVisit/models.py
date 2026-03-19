from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)   # ✅ hashes the password
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):         # ✅ NOT models.Model
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    username   = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField()
    role       = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active  = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD  = 'username'       # ✅ field used for login
    REQUIRED_FIELDS = ['email']
    

    
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


