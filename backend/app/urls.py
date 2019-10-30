from django.urls import path
from .views import *

urlpatterns = [
    path('', AllTwit.as_view(), name="home"),
    path('my/', PostView.as_view(), name="posts"),
    path('like/', Like.as_view(), name="like"),
    # path('my/update/', UpdatePost.as_view(), name="update"),
]
