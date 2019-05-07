from django.shortcuts import render, redirect

from django.views import View
from django.views import generic

class Clean_web_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'clean_web_main/index.html'
        return render(request, template_name)