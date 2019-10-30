from django.urls import path
from .views import *

urlpatterns = [
    path('', TweetsAll.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('all/', PostListView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    # path('update-twit/', UpdateTwits.as_view()),
]