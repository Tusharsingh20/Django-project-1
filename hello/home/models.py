from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    feedback=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to='upload images', height_field=None, width_field=None, max_length=None, default="")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
