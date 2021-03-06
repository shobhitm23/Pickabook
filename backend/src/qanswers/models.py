from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)

    question = models.TextField(max_length=300, blank=False)

    creation_date = models.DateField(default=datetime.date.today)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


    def __str__(self):
        return self.question    



class Answer(models.Model):
    profile = models.ForeignKey('users.Profile',  on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)


    answer = models.TextField(max_length=500, blank=False)

    creation_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.answer    
