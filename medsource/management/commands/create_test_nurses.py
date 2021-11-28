import random
from random import randint

from django.core.management.base import BaseCommand, CommandError
from medsource.models.user import Hospital, Nurse
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates dummy records of nurses for testing"

    def handle(self, *args, **options):
        education_levels = ["Técnico", "Tecnólogo", "Especialización", "Pregrado", "Maestría"]
        areas = ["Pasillo", "Cirguía", "Endocrinología", "Med interna", "Cardiología"]
        hospital_query_set = Hospital.objects.all()
        total_nurses = 10
        for nurse_idx in range(1, total_nurses + 1):
            user_data = dict(
                username=f"test_nurse{nurse_idx}",
                email=f"test_nurse{nurse_idx}@test.com",
                first_name=f"nurse{nurse_idx}",
            )
            user = User.objects.update_or_create(**user_data)[0]
            data = dict(
                user=user,
                identification=randint(10000, 50000),
                education=random.choice(education_levels),
                area=random.choice(areas),
                hospital=random.choice(hospital_query_set)
            )
            Nurse.objects.update_or_create(**data)
