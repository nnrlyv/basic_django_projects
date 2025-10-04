from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    published_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default="")
    views_count = models.IntegerField(default=0)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# str метод нужен чтобы обьект читали как строку
    def __str__(self):
        return self.choice_text

