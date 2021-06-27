from django.urls import path

from expenses_tracker.profiles.views import profile_home, edit_profile, delete_profile

urlpatterns = [
    path('', profile_home, name='profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile')
]