from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import HandleToken, register, overall_score

app_name = 'api_first'

urlpatterns = [
    path('login/', HandleToken.as_view()), # get token
    path('register/', register),
    path('get_score/', overall_score)
]
