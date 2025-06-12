from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_view),
    path('single', single_view)
]
