from django.contrib import admin
from django.urls import path
from medsource.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('medico/registro', DoctorRegistView.as_view()),
    path('enfermero/registro', NurseRegistView.as_view()),
    path('antecedente/ingreso', RecordRegistView.as_view()),
    path('vinculacion_antecedente/ingreso',
         Patient_RecordRegistView.as_view()),
    path('paciente/ingreso', PatientRegistView.as_view()),
    path('procedimiento/ingreso', ProcedureRegistView.as_view()),
    path('desarrollo/ingreso', DevelopmentRegistView.as_view()),
    path('consulta/ingreso', ConsultationRegistView.as_view()),
    path('hospital', HospitalListView.as_view()),
    path('eps', EpsListView.as_view()),
    path('antecedentes', RecordListView.as_view()),
    path('reestablecer_contrasena/<str:arg>', TokenCRUDView.as_view()),
    path('procedimientos/', ProcedureListView.as_view()),
    path("paciente/<int:identification>", PatientRUDView.as_view()),
    path("doctor/<int:identification>", DoctorRUDView.as_view()),
    path("enfermero/<int:identification>", NurseRUDView.as_view()),
]
