from django.urls import path, include
from . import views
urlpatterns = [
    # path('sms',views.sms_view),
    path('email',views.sendEmail),
    path('sms',views.sendSms),
    path('<str:username>',views.UsersView.as_view()),

    path('<str:username>/passwordChange',views.passwordChange),
    path('<str:username>/passwordGet',views.passwordGet),
    # path('<str:username>/changeInfo',views.changeInfo),
    # path('<str:username>/avatar',views.user_avatar),
]


