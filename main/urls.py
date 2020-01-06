from django.urls import path
from .views import Index
from django.views.generic import RedirectView


# App Namespace
app_name = 'main'

urlpatterns = [
    path('<str:lang>/<str:section>', Index.as_view(), name='index'),
    #path('<str:lang>/<str:section>', RedirectView.as_view(), name='index'),
]
