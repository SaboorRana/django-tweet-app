# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('',views.tweet_list,name='tweet_list'),
    path('/create',views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/',views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/',views.tweet_delete,name='tweet_delete'),
    path('tweet/',views.index,name='index'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('registration/', views.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
