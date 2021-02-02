from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from upload.models import Photo, PhotoGroup
from upload.forms import GroupForm
from django.http import Http404
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'UserApp/signup.html', {'form': form})

def profile(request):
    all_photos = Photo.objects.filter(user=request.user).order_by('-uploaded')
    all_groups = PhotoGroup.objects.filter(user=request.user)
    
    context = {
        'photos' : all_photos,
        'groups' : all_groups,
    }
    return render(request, 'UserApp/profile.html', context)

class AddGroupView(LoginRequiredMixin ,TemplateView):
    template_name = "upload/add_group.html"

    def get(self, request):
        form = GroupForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = GroupForm(request.POST or None)
        if(form.is_valid):
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

        context = {'form': form}
        return redirect('/profile')

class GroupEditView(LoginRequiredMixin ,TemplateView):
    template_name = "upload/add_group.html"

    def get(self, request, group_id=None):
        instance = get_object_or_404(PhotoGroup, id=group_id)

        if instance.user != request.user:
            raise Http404("Group does not exist")

        form = GroupForm(instance=instance)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, group_id=None):
        instance = get_object_or_404(PhotoGroup, id=group_id)
        form = GroupForm(request.POST or None)
        if(form.is_valid):
            instance.name = form.data['name']
            instance.save()

        context = {'form': form}
        return redirect('/profile')

@login_required
def group_delete(request, group_id=None):
    instance = get_object_or_404(PhotoGroup, id=group_id)
    instance.delete()

    return redirect('/profile')
