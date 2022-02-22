from django.db import models as m
# img  = m.ImageField(upload_to="user_profile",default="")
class BaseProfile(m.Model):
    name = m.CharField(max_length=125)
    email = m.EmailField(max_length=255,unique=True)
    password = m.CharField(max_length=500)
    usePurpose = m.TextField()
    def __str__(self):
        return self.name

class FullProfile(m.Model):
    bpu = m.ForeignKey(BaseProfile,on_delete = m.CASCADE)
    profileImg = m.ImageField(upload_to="user_profile",default="default.jpg")
    address = m.TextField(max_length=255)
    city = m.TextField(max_length=100)
    pincode = m.IntegerField(max_length=6)
    def __str__(self):
        return self.bpu.name

