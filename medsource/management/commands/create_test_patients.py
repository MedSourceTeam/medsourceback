import random
import datetime
from random import randint

from django.core.management.base import BaseCommand, CommandError
from medsource.models.user import Hospital, Patient, Eps


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


class Command(BaseCommand):
    help = "Creates dummy records of patients for testing"

    def handle(self, *args, **options):
        total_patients = 5
        min_date = datetime.date(1930, 1, 1)
        max_date = datetime.date(2000, 1, 1)
        blood_options = ["o+", "o-", "a+", "a-", "ab+"]
        eps_query_set = Eps.objects.all()
        for patient_idx in range(1, total_patients + 1):
            data = dict(
                identification=randint(10000, 50000),
                date_of_birth=random_date(min_date, max_date),
                blood_type=random.choice(blood_options),
                eps = random.choice(eps_query_set)
            )
            Patient.objects.update_or_create(**data)
