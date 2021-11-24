import random
from random import randint

from django.core.management.base import BaseCommand, CommandError
from medsource.models.user import Hospital


class Command(BaseCommand):
    help = "Creates dummy records of Hospitals for testing"

    def handle(self, *args, **options):
        total_hospitals = 10
        cities = ["Bogotá", "Medellín", "Bucaramanga"]
        for hospital_idx in range(1, total_hospitals + 1):
            data = dict(
                name=f"Hospital{hospital_idx}",
                address=f"Calle {randint(1, 15)} Av {randint(3, 100)}",
                city=random.choice(cities)
            )
            Hospital.objects.update_or_create(**data)
