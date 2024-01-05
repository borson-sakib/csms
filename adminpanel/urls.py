from django.urls import path

from . import views
from .views import register
from .views import init_tickt
from .views import upload_csv
from .views import verify_entry
from .views import query_form
from .views import get_queries
from .views import raise_ticket


urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('register/', register, name='register'),
    path('init_tickt/', init_tickt, name='init_tickt'),
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('verify_entry/', verify_entry, name='verify_entry'),
    path('query_form/', query_form, name='query_form'),
    path('get_queries/', get_queries, name='get_queries'),
    path('raiseTicket/', raise_ticket, name='raiseTicket'),

]