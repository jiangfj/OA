from django.urls import path
from . import views
urlpatterns = [
    path('list', views.notice_list),
    path('add', views.notice_add_view),
    path('view', views.notice_view),
    path('update', views.notice_update_view),
    path('update/<str:_id>', views.notice_update_view),
    path('del', views.notice_delete_view),
]
