from django.urls import path
from . import views


app_name="home"

urlpatterns = [
    path("",views.index, name="home"),
    path("particular/<int:ques_id>", views.ParticularQues, name="particularQues"),
    path("vote/<int:ques_id>", views.vote, name="vote"),
    path("result/<int:ques_id>",views.result, name="result"),
    path("contact", views.contact, name="Contact"),
]
