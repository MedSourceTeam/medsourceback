from django.db import models
from django.contrib.auth.models import User


# ---------------------------------- EPS ---------------------------------------

class Eps(models.Model):
    name = models.CharField(
        'Nombre de la Eps', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Eps'
        verbose_name_plural = 'Eps'

# ---------------------------------- HOSPITAL ---------------------------------------


class Hospital(models.Model):
    name = models.CharField('Nombre del Hospital',
                            max_length=100, null=False, blank=False)
    address = models.CharField(
        'Dirección', max_length=100, null=False, blank=False)
    city = models.CharField('Ciudad', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitales'

# ---------------------------------- PACIENTES ---------------------------------------


class Patient (models.Model):
    # user = models.OneToOneField(
    #    User, on_delete=models.CASCADE, related_name="Usuario")
    identification = models.IntegerField(
        'Cedula', null=False, blank=False, unique=True)
    date_of_birth = models.DateTimeField(
        'Fecha de Nacimiento', null=False, blank=False)
    phone = models.BigIntegerField('Teléfono', null=True, blank=True)
    marital_status = models.CharField(
        'Estado Civil', max_length=200, null=True, blank=True)
    blood_type = models.CharField(
        'Grupo Sanguineo', max_length=200, null=False, blank=False)
    eps = models.ForeignKey('Eps', on_delete=models.PROTECT,
                            related_name='petient', null=False, blank=False)

    def __str__(self):
        return str(self.identification)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

# ---------------------------------- ENFERMEROS ---------------------------------------


class Nurse (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="nurse")
    identification = models.IntegerField(
        'Cedula', null=False, blank=False, unique=True)
    education = models.CharField(
        'Formación', max_length=200, null=False, blank=False)
    area = models.CharField('Area', max_length=200, null=False, blank=False)
    hospital = models.ForeignKey(
        'Hospital', on_delete=models.PROTECT, related_name='nurse', null=False, blank=False)

    def __str__(self):
        return str(self.identification)

    class Meta:
        verbose_name = 'Enfermero'
        verbose_name_plural = 'Enfermeros'

# ---------------------------------- Doctores ---------------------------------------


class Doctor (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor")
    identification = models.IntegerField(
        'Cedula', null=False, blank=False, unique=True)
    education = models.CharField(
        'Formación', max_length=200, null=False, blank=False)
    specialization = models.CharField(
        'Especialización', max_length=200, null=True, blank=True)
    hospital = models.ForeignKey(
        'Hospital', on_delete=models.PROTECT, related_name='doctor', null=False, blank=False)

    def __str__(self):
        return str(self.identification)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'
