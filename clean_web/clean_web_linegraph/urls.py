from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Clean_web_line_graph_main.as_view(), name='clean_web_line_graph'),
    url(r'^day$', views.Clean_web_line_graph.as_view(), name='clean_web_line_graph_day'),
    url(r'^week$', views.Clean_web_line_graph.as_view(), name='clean_web_line_graph_week'),
    url(r'^month$', views.Clean_web_line_graph.as_view(), name='clean_web_line_graph_month'),
    url(r'^year$', views.Clean_web_line_graph.as_view(), name='clean_web_line_graph_year'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)