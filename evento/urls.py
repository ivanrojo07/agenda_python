from django.urls import path, include
from .views import ListEvento, eventUser,eventForDays

urlpatterns=[
    path('', ListEvento.as_view()),
    path('<int:pk>/', ListEvento.as_view()),
    path('user/', eventUser),
    path('user/today/',eventForDays),
]