import random
from random import randint

from django.core.management.base import BaseCommand, CommandError
from medsource.models.user import Hospital, Doctor
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates dummy records of doctors for testing"

    def handle(self, *args, **options):
        education_levels = ["Pregrado", "Master", "Especialización", "Doctorado", "GodMode"]
        specializations = ["Cardiología", "Neurología", "Endocrinología", "Med interna", "Hematología"]
        hospital_query_set = Hospital.objects.all()
        total_doctors = 5
        for doctor_idx in range(1, total_doctors + 1):
            user_data = dict(
                username=f"test_doctor{doctor_idx}",
                email=f"test_doctor{doctor_idx}@test.com",
                first_name=f"doctor{doctor_idx}",
            )
            user = User.objects.update_or_create(**user_data)[0]
            data = dict(
                user=user,
                identification=randint(10000, 50000),
                education=random.choice(education_levels),
                specialization=random.choice(specializations),
                hospital=random.choice(hospital_query_set)
            )
            Doctor.objects.update_or_create(**data)
