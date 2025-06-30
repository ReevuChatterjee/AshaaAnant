from django.db import models

class RescueDB(models.Model):
    contactName=models.CharField(max_length=150)
    contactNumber=models.CharField(max_length=11)
    location=models.TextField()
    type=models.CharField()
    photo=models.ImageField(upload_to='Rescue_Photo/', default='default.png', blank=True)
    issueFaced=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contactName} - {self.type} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# Create your models here.
