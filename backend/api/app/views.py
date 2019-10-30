from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from backend.app.models import Post
from backend.api.app.serializers import PostListSerialiser, PostDetailSerializer, PostSerializer
from rest_framework import generics
from backend.api.app.permissions import IsOwnerOrReadOnly

class PostCreateView(generics.CreateAPIView):#для создания объекта по полям в бд
    serializer_class= PostDetailSerializer
class PostListView(generics.ListAPIView):# увидеть весь список
    serializer_class=PostListSerialiser
    queryset = Post.objects.all()#какие записи вынуть с базы данных queryset
    # permission_classes = (IsAdminUser, )# только смотри админ
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PostDetailSerializer
    queryset=Post.objects.all()
    # authentication_classes= (TokenAuthentication,)#через веб интерфейс не авторизуемся только через токен(через кук не льзя)
    permission_classes= (IsOwnerOrReadOnly,)# позволяет менять только тот кто создал
class TweetsAll(APIView):
    """Вывод всех твитов"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tweets = Post.objects.all()
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)

#
# class UserTweet(APIView):
#     """Твиты пользователя"""
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         tweets = Post.objects.filter(user=request.user)
#         ser = PostSerializer(tweets, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         ser = AddTweetSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save(user=request.user)
#             return Response(status=200)
#         else:
#             return Response(status=400)
#
#
# class Like(APIView):
#     """Ставим лайк"""
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request):
#         pk = request.data.get("pk")
#         post = Post.objects.get(id=pk)
#         if request.user in post.user_like.all():
#             post.user_like.remove(User.objects.get(id=request.user.id))
#             post.like -= 1
#         else:
#             post.user_like.add(User.objects.get(id=request.user.id))
#             post.like += 1
#         post.save()
#         return Response(status=201)
#
# class UpdateTwits(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request):
#         prof = Post.objects.post(user = request.user)
#         ser = EditTwit(prof, data=request.data)
#         if ser.is_valid():
#             ser.save()
#

