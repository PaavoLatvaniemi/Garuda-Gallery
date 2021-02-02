from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.http import Http404

from upload.models import Photo, PhotoGroup
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def detail(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)

    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")

    if photo.user != request.user:
        raise Http404("Photo does not exist")
        
    return render(request, 'explorer/detail.html', {'photo': photo})



class photo_list(LoginRequiredMixin ,TemplateView):
    template_name = "explorer/explorer.html"
    def get(self, request):
        all_photos = Photo.objects.filter(user=request.user)
        all_groups = PhotoGroup.objects.filter(user=request.user)
        return render(request, self.template_name, {'photos' : all_photos, 'groups' : all_groups, 'current_group_name': 'All'})
    
    def post(self, request):
        
        all_groups = PhotoGroup.objects.filter(user=request.user)

        if(request.POST.get("all")):
            all_photos = Photo.objects.filter(user=request.user)
            context = {'photos' : all_photos, 'groups' : all_groups, 'current_group_name': 'All'}
            return render(request, self.template_name, context)

        for group in all_groups:
            if request.POST.get(str(group.id)):
                current_group = group
                break

        all_photos = Photo.objects.filter(user=request.user, photo_group=current_group.id)
        context = {'photos' : all_photos, 'groups' : all_groups, 'current_group_name': current_group.name}
        return render(request, self.template_name, context)


@login_required
def delete(request, photo_id=None):
    instance = get_object_or_404(Photo, id=photo_id)
    instance.delete()
    instance.photo.delete(save=False)
    instance.thumbnail.delete(save=False)
    instance.photo_MidRes.delete(save=False)

    return redirect('/explorer')
