from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("parkings/", views.ParkingList.as_view()),
    path("parkings/<int:pk>/", views.ParkingDetail.as_view()),

    path("spaces/", views.ParkingSpaceList.as_view()),
    path("spaces/<int:pk>/", views.ParkingSpaceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
