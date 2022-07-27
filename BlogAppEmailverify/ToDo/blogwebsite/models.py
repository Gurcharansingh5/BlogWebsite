from django.db import models
from django.contrib.auth.models import  User ,AbstractUser

# Create your models here.
from django.db import models
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_verified =models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Blogs(models.Model):
    blodid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogid')
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1200, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    post_views = models.IntegerField(default=0, null=True, blank=True)


class comment(models.Model):
    blogname = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    commentatorname = models.ForeignKey(User, on_delete=models.CASCADE)
    commentonblog = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, null=True)
