
from EmployeeApp import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path(r'^department$',views.departmentApi),
    path(r'^department/([0-9]+)$',views.departmentApi),

    path(r'^employee$',views.employeeApi),
    path(r'^employee/([0-9]+)$',views.employeeApi),

    path(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)