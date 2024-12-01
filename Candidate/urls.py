from django.urls import path
from Candidate import views

urlpatterns = [
    path('',views.index, name="index"),
    path('profileIds',views.profileIds, name="profileIds"),
    path('individualIds/<int:user_id>/',views.individualIds, name="individualIds"),
]