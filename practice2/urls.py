from django.urls import path,include

urlpatterns = [
    path('users',include('App1.urls'))
]

