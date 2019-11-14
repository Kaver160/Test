from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse, request
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from backend.profiles.form import ProfileForm


from .models import Profile
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'
    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj
# class ProfileDelete(View):
#     def post(self, request):
#         pk = request.POST.get("id")
#         user = Profile.objects.get(pk='id')
#         user.delete()
#         return HttpResponse(status=201)
#     Profile.objects.filter(user=4).delete()
