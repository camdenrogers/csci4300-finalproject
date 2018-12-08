from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.IndexView.as_view(), name='eventList'),
    path('events/<int:pk>/', views.IndexView.as_view(), name='detail'),
]

