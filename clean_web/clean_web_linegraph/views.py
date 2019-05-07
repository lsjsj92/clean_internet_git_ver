from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.http import JsonResponse
import requests
from clean_web_main.get_data import *
import json

class Clean_web_line_graph(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        date_type = str(request).split('/')[-1].split("'>")[0]
        date, count = [], []
        for data in datas:
            date.append(data['dateTime'])
            count.append(data['totalCount'])
        date.reverse()
        count.reverse()
        return render(request, dataBox['template_name'], {'date': date, 'count':count})

class Clean_web_line_graph_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #전체 데이터를 보내야 함. -> 통신을 4번해야함

