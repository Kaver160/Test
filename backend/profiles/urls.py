from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileView.as_view(), name='view_profile'),
    # path('delete/', ProfileDelete.as_view()),
]