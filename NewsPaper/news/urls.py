from django.urls import path
from news.views import *


urlpatterns = [
    path('', PostList.as_view(template_name='posts.html')),
    path('<int:pk>', detail, name='detail'),
]



    # path('', default, name='default'),
    # path('<int:pk>', detail, name='detail')


    # path('postcreate/', PostCreate.as_view())