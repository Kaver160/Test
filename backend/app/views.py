from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from backend.app.models import Post
from backend.app.forms import PostForm, RemoveUser

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
    @login_required(login_url='http://127.0.0.1:8000/')
    def remove_user(request):
        if request.method == 'POST':
            form = RemoveUser(request.POST)
            username = request.POST.get('username')
            if form.is_valid():
                rem = User.objects.get(username=username)
                rem.delete()
                return redirect('main')
        else:
            form = RemoveUser()
        context = {'form': form}
        return render(request, 'remove_user.html', context)


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

# class UpdatePost(View):
#     def post(self, request):
#         pk = request.POST.get("pk")
#         post = Post.objects.get(id=pk)
#         return redirect('http://127.0.0.1:8000/api/v1/app/post/detail/'+ id +'/')
