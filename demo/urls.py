from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('upload/', views.insert),
    path('get-json/', views.excel_file),
    
]





