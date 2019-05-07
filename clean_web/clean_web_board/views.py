from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.http import JsonResponse
import requests
from clean_web_main.get_data import *

class Clean_web_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        datas = (requests.get(dataBox['url'], params=dataBox['params'], headers=dataBox['headers'])).json()
        board_list = []
        for data in datas:
            board_list.append([data['content'], data['category']])
        board_list.reverse()
        return render(request, dataBox['template_name'], {'board_data': board_list})