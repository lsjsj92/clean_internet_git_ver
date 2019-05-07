from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.http import JsonResponse
import requests
from clean_web_main.get_data import *


class Clean_web_piechart(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        dataBox = get_data("piechart")
        for data in datas:
            yes += int(data['yes'])
            no += int(data['no'])

        pie_data.append(['yes', yes])
        pie_data.append(['no', no])
        return render(request, dataBox['template_name'], {'pie_data': pie_data})
