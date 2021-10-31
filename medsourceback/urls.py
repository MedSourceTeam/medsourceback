from django.contrib import admin
from django.urls import path
from medsource.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from medsource.views.nurseRegistView import NurseRegistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('medico/registro', DoctorRegistView.as_view()),
    path('enfermero/registro', NurseRegistView.as_view()),
]
