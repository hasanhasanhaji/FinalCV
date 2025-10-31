from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True) ## add this field when teaching  اضافه کردن فیلد نویسنده
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
