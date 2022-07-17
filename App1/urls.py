from django.urls import path
from App1.views import SignUpView

urlpatterns=[
    path('/signup',SignUpView.as_view()),
]

