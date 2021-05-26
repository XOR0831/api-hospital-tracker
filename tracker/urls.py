from django.urls import path

from . import (
    views
)

urlpatterns = [
    path("",views.ListHospitalAPIView.as_view(),name="hospital_list"),
    path("create/", views.CreateHospitalAPIView.as_view(),name="hospital_create"),
    path("update/<int:pk>/",views.UpdateHospitalAPIView.as_view(),name="update_hospital"),
    path("delete/<int:pk>/",views.DeleteHospitalAPIView.as_view(),name="delete_hospital"),

]