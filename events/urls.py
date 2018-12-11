from django.urls import path

from . import views

app_name = "events"
urlpatterns = [
    path('', views.index, name='index'),
    path('events/map/', views.map, name='map'),
    path('populatedb/', views.getData, name='getdata'),
    path('events/', views.IndexView.as_view(), name='eventList'),
    path('events/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('events/partiallist/<int:num>', views.PartialList, name='partialview'),
]

