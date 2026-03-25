from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# ✅ Profile Model for extended user information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



class UserPredictModel(models.Model):
    image = models.ImageField(upload_to='images/')
    label = models.CharField(max_length=20, default='data')

    def __str__(self):
        return str(self.image)


# ✅ Patient information model
class Patient_info(models.Model):
    Bp = models.FloatField()     # Blood Pressure
    Sg = models.FloatField()     # Specific Gravity (should ideally be Float)
    Al = models.FloatField()     # Albumin
    Su = models.FloatField()     # Sugar
    Rbc = models.FloatField()    # Red Blood Cells
    Bu = models.FloatField()     # Blood Urea
    Sc = models.FloatField()     # Serum Creatinine
    Sod = models.FloatField()    # Sodium
    Pot = models.FloatField()    # Potassium
    Hemo = models.FloatField()     # Hemoglobin
    Wbcc = models.FloatField()   # White Blood Cell Count
    Rbcc = models.FloatField()   # Red Blood Cell Count
    Htn = models.FloatField()    # Hypertension
    disease_class = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Prediction: {self.disease_class}"
