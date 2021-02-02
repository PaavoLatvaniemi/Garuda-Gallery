from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UploadForm
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin


class UploadView(LoginRequiredMixin ,TemplateView):
    template_name = "upload/index.html"

    def get(self, request):
        form = UploadForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None)
        if(form.is_valid):
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

        context = {'form': form}
        return redirect('/explorer')
