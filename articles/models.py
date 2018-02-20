from django.db import models

# Create your models here.

class Articles(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_updated(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S') != self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
#
# Vote: 1,2,.. stars
class Vote(models.Model):
    text = models.CharField(    max_length=200)
    date = models.DateTimeField('date published')

#
class Choice(models.Model):
    question    = models.ForeignKey(    Vote, on_delete=models.CASCADE)
    text        = models.CharField(     max_length=200)
    votes       = models.IntegerField(  default=0)