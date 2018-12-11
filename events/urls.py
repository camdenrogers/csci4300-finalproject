from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = "events"
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/map/', views.map, name='map'),
    path('populatedb/', views.getData, name='getdata'),
    path('events/', views.IndexView.as_view(), name='eventList'),
    path('events/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('events/partiallist/<int:num>/', views.PartialList, name='partialview'),
    path('events/groups/<int:num>/', views.Groups, name='groups'),
    path('events/groups/<int:num>/create/', views.NewGroup, name='newGroup'),
    path('events/groups/<int:eventnum>/<int:groupnum>/', views.JoinGroup, name='joinGroup'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]

