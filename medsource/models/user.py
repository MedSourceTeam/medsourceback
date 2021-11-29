from django.db import models
from django.contrib.auth.models import User
import uuid

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
    full_name = models.CharField(
        'Nombre Completo', max_length=200, null=False, blank=False)
    date_of_birth = models.DateField(
        'Fecha de Nacimiento', null=False, blank=False)
    phone = models.BigIntegerField('Teléfono', null=True, blank=True)
    marital_status = models.CharField(
        'Estado Civil', max_length=200, null=True, blank=True)
    blood_type = models.CharField(
        'Grupo Sanguineo', max_length=200, null=False, blank=False)
    eps = models.ForeignKey('Eps', on_delete=models.PROTECT,
                            related_name='patient', null=False, blank=False)

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


# ---------------------------------- ANTECEDENTES ---------------------------------------


class Record (models.Model):
    name = models.CharField(
        'Nombre del antecedente', max_length=200, null=False, blank=False)
    kind = models.CharField(
        'Tipo', max_length=200, null=False, blank=False)
    sort = models.CharField(
        'Clase', max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'


# ---------------------------------- ANTECEDENTES - PACIENTES ---------------------------------------


class Patient_Record (models.Model):
    patient = models.ForeignKey(
        'Patient', on_delete=models.PROTECT, related_name='presencia', null=False, blank=False)
    record = models.ForeignKey(
        'Record', on_delete=models.PROTECT, related_name='presencia', null=False, blank=False)

    def __str__(self):
        return str(self.patient), str(self.record)

    class Meta:
        verbose_name = 'Presencia de antecedente'
        verbose_name_plural = 'Presencia de antecedentes'


# ---------------------------------- Procedimientos ---------------------------------------


class Procedure (models.Model):
    name = models.CharField(
        'Nombre del procedimiento', max_length=200, null=False, blank=False)
    uvr = models.IntegerField(
        'UVR', null=False, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'


# ---------------------------------- Desarrollo Procedimientos ---------------------------------------


class Development (models.Model):
    date = models.DateField(
        'Fecha', null=False, blank=False)
    room = models.CharField(
        'Sala', null=False, max_length=200, blank=False)
    comment = models.CharField(
        'Comentario', max_length=200, null=True, blank=True)
    patient = models.ForeignKey(
        'Patient', on_delete=models.PROTECT, related_name='desarrollo', null=False, blank=False)
    doctor = models.ForeignKey(
        'Doctor', on_delete=models.PROTECT, related_name='desarrollo', null=False, blank=False)
    nurse = models.ForeignKey(
        'Nurse', on_delete=models.PROTECT, related_name='desarrollo', null=False, blank=False)
    hospital = models.ForeignKey(
        'Hospital', on_delete=models.PROTECT, related_name='desarrollo', null=False, blank=False)
    procedure = models.ForeignKey(
        'Procedure', on_delete=models.PROTECT, related_name='desarrollo', null=False, blank=False)

    def __str__(self):
        return str(self.patient), str(self.doctor), str(self.nurse)

    class Meta:
        verbose_name = 'Desarrollo'
        verbose_name_plural = 'Desarrollos'


# ---------------------------------- Consultas ---------------------------------------


class Consultation (models.Model):
    pulse = models.IntegerField(
        'Pulso', null=True, blank=True)
    height = models.IntegerField(
        'Altura', null=True, blank=True)
    weight = models.IntegerField(
        'Peso', null=True, blank=True)
    pa = models.IntegerField(
        'Pa', null=True, blank=True)
    pr = models.IntegerField(
        'Pr', null=True, blank=True)
    t = models.IntegerField(
        'T', null=True, blank=True)
    medication = models.CharField(
        'Medicamento', max_length=200, null=True, blank=True)
    symptom = models.CharField(
        'Sintoma', max_length=200, null=True, blank=True)
    diagnosis = models.CharField(
        'Diagnostico', max_length=200, null=True, blank=True)
    patient = models.ForeignKey(
        'Patient', on_delete=models.PROTECT, related_name='consulta', null=False, blank=False)
    doctor = models.ForeignKey(
        'Doctor', on_delete=models.PROTECT, related_name='consulta', null=False, blank=False)
    hospital = models.ForeignKey(
        'Hospital', on_delete=models.PROTECT, related_name='consulta', null=False, blank=False)

    def __str__(self):
        return str(self.patient), str(self.doctor)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


# ---------------------------------- Tokens ---------------------------------------

class Token(models.Model):
    token = models.UUIDField('Token', auto_created=True,
                             unique=True, primary_key=True, default=uuid.uuid4,)
    code = models.IntegerField('Codigo', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='token', null=False, blank=False)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
