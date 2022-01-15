from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('change_password',views.change_password,name='change_password'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('add_event',views.add_event,name='add_event'),
    path('view_all_events',views.view_all_events,name='view_all_events'),

    path('add_complaint',views.add_complaint,name='add_complaint'),
    path('view_all_complaints',views.view_all_complaints,name='view_all_complaints'),

    path('add_feedback',views.add_feedback,name='add_feedback'),
    path('view_all_feedback',views.view_all_feedback,name='view_all_feedback'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)