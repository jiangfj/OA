from django.conf.urls import url

from . import views


urlpatterns = [
    url('list',views.department),
    url('^add_department$',views.add_department),
    url('^add_position$',views.add_position),
    # url('^del_position$',views.del_department),

]

