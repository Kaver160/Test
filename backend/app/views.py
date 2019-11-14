from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from backend.app.models import Post
from backend.app.forms import PostForm, RemoveUser
from backend.profiles.models import Profile
from django.shortcuts import get_object_or_404


class AllTwit(ListView):
    # model = Post
    queryset = posts = Post.objects.filter(twit__isnull=True,)
    context_object_name = 'posts'
    template_name = 'app/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        return context
class PostView(View):
    """"Сообщения пользователя"""
    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(twit__isnull=True, user = request.user)
        else:
            posts = Post.objects.filter(twit__isnull=True,)
        form = PostForm()
        # paginator = Paginator(posts, 5)
        # page = request.GET.get("page")
        # page_obj = paginator.get_page(page)
        return render(request, "app/index2.html", {"posts": posts, "form": form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)
            form = form.save(commit=False)
            if pk is not None:
                form.twit = Post.objects.get(id=pk)
            form.user = request.user
            form.save()
            return redirect("posts")
        else:
            return HttpResponse("error")
class Like(LoginRequiredMixin, View):
    """Ставим лайк"""
    def post(self, request):
        pk = request.POST.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)
#
# class Delete(View):
#     def get(self, request):
#             pk = request.POST.get("id")
#             user = Profile.objects.get(pk='16')
#             user.delete()
        # try:
        #     u = User.objects.get(username=user)
        #     u.delete()
        #     messages.success(request, "The user is deleted")
        #
        # except User.DoesNotExist:
        #     messages.error(request, "User doesnot exist")
        #     return render(request, 'front.html')
        #
        # except Exception as e:
        #     return render(request, 'front.html', {'err': e.message})
        #
        # return render(request, 'front.html')





