from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from PIL import Image
=======
>>>>>>> parent of 2741b71 (resoved conflicts)

# Create your models here.
class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
<<<<<<< HEAD
    
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return str(self.user)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



        
 
=======
    
>>>>>>> parent of 2741b71 (resoved conflicts)
