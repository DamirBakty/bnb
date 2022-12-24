from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import overall_score

app_name = 'api_first'

urlpatterns = [
    path('get_score/', overall_score)
]
