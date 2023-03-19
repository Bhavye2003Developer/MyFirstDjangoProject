from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Answer, Contact

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Contact)