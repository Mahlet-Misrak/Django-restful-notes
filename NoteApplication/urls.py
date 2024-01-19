
from django.contrib import admin
from django.urls import path
from user import views as user_views
# from . import views # This is the views file
from note import views as note_views
# from .views import delete_user


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', note_views.getNotes, name='routes'),
    path('note/', note_views.getNotes, name='get_notes'),
    path('user/', user_views.getUsersList, name='get_users'),
    path('note/create/', note_views.createNote, name='createNote'),
    path('user/create/', user_views.createUser, name='create_user'),
    path('user/delete/<int:user_id>/', user_views.delete_user, name='delete_user'),
    path('note/delete/<int:note_id>/', note_views.delete_note, name='delete_note'),

   
]
