from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('compose_mail',views.compose_mail,name='compose_mail'),
    path('view_send_messages',views.view_send_messages,name='view_send_messages'),

    path('view_particular_mail1/<int:id>',views.view_particular_mail1,name='view_particular_mail1'),

    path('move_trash/<int:id>',views.move_trash,name='move_trash'),

    path('view_trash',views.view_trash,name='view_trash'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)