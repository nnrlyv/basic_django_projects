from django.contrib import admin
from .models import Question , Choice


list_display = ( 'question_text', 'views_count',  'published_date')
#зарегали в админку модели
admin.site.register(Question)
admin.site.register(Choice)
