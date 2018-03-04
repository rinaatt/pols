from django.db import models


class QuestionSet(models.Model):
    title = models.CharField('Title', max_length=200)
    descr = models.TextField('Description')

    def __str__(self):
        return self.title


class Question(models.Model):
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    question_text = models.CharField('Text', max_length=400)
    order = models.IntegerField('Order')

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=400)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
