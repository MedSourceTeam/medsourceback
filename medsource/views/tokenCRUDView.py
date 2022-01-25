from rest_framework import generics, views, status
from rest_framework.response import Response
from medsource.serializers import TokenSerializer
from medsource.models import Token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags


class TokenCRUDView(views.APIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data['email'])
        token = Token(user=user)
        try:
            token.save()
        except:
            Token.objects.filter(user=user).delete()
            token.save()
        subject = "Recuperacion de contraseña"
        message = """Para Recuperar su contraseña dirijase al siquiente enlace: <br> 
        <a href="https://medsourcetm.herokuapp.com/recuperarcontrasena/""" + str(token.token) + """">Recuperar Contraseña</a>"""
        send_mail(subject, strip_tags(message),
                  settings.EMAIL_HOST_USER, [user.email], html_message=message)
        return Response({"exitoso": True}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        token = Token.objects.filter(token=kwargs['arg']).exists()
        if token:
            return Response({"exitoso": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exitoso": False}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        token = Token.objects.filter(token=kwargs['arg']).exists()
        if token:
            token = Token.objects.get(token=kwargs['arg'])
            user = User.objects.get(pk=token.user.id)
            user.set_password(request.data["password"])
            token.delete()
            user.save()
            return Response({"exitoso": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exitoso": False}, status=status.HTTP_200_OK)
