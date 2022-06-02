from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# 127.0.0.1/polls/ 인 경우, path'', 아무것도 없기 때문에 views.index라는 view 내부로 연결해줌.