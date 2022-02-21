from django.db import models as m
# img  = m.ImageField(upload_to="user_profile",default="")
class BaseProfile(m.Model):
    name = m.CharField(max_length=125)
    email = m.EmailField(max_length=255,unique=True)
    password = m.CharField(max_length=500)
    usePurpose = m.TextField()
    def __str__(self):
        return self.name
