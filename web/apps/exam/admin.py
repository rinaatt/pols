from django.contrib import admin
from . import models


@admin.register(models.QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
