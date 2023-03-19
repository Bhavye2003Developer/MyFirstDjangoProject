from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    ques = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class Answer(models.Model):
    question = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question} -> {self.ans}'
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    issue = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} -> {self.email}"