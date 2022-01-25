import base64
from rest_framework import generics, status
from medsource.models import Doctor, Nurse, Development
from rest_framework_simplejwt.backends import TokenBackend
from medsourceback import settings
from medsource.serializers import DownloadSerializer
from django.db.models import Q
from openpyxl import load_workbook
from rest_framework.response import Response


class WorkView(generics.GenericAPIView):

    serializer_class = DownloadSerializer

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        queryset = Development.objects.all()

        try:
            person = Doctor.objects.get(user=valid_data["user_id"])

        except:
            person = Nurse.objects.get(user=valid_data["user_id"])

        queryset = queryset.filter(Q(doctor__identification=person.identification) | Q(
            nurse__identification=person.identification))

        book = load_workbook(filename="medsource/resources/Formato.xlsx")
        sheet = book.active

        sheet["D4"] = str(person.hospital)
        sheet["D5"] = str(person.user.first_name) + \
            " " + str(person.user.last_name)
        sheet["D8"] = str(person.user.email)
        sheet["J5"] = str(person.identification)

        pos = 16

        for row in queryset:
            sheet["A" + str(pos)] = str(pos-15)
            sheet["B" + str(pos)] = str(row.date)
            sheet["C" + str(pos)] = str(row.patient.full_name)
            sheet["D" + str(pos)] = str(row.patient.identification)
            sheet["E" + str(pos)] = str(row.procedure.name)
            sheet["F" + str(pos)] = int(row.procedure.uvr)
            pos += 1

        with open("medsource/resources/tempfile.xlsx", "wb+") as tmp:
            book.save(tmp.name)
            return Response({
                "file": base64.b64encode(tmp.read()),
                "mimeType": 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            }, status.HTTP_200_OK)
