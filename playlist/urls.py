from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ChartView, SearchResultsView, EgorCridView

urlpatterns = [
    path('Egor_Crid/', EgorCridView.as_view(), name='EgorCrid'),
    url('search/', SearchResultsView.as_view(), name='search_results'),
    path('nastroi/', views.nastroi, name='nastroi'),
    path('chart/', ChartView.as_view(), name='chart'),
    path('new/', views.new, name='new'),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)