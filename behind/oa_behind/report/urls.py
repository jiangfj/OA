from django.urls import path
from . import views
urlpatterns = [
path('list', views.list),
path('add', views.add),
path('view', views.content),
path('update/<str:_id>', views.update),
path('update', views.update),
path('del', views.delete),

]