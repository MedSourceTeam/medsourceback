import random
from random import randint

from django.core.management.base import BaseCommand, CommandError
from medsource.models.user import Hospital, Eps
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates dummy records of eps for testing"

    def handle(self, *args, **options):
        total_eps = 10
        for eps_idx in range(1, total_eps + 1):
            name = f"test_eps_{eps_idx}"
            Eps.objects.update_or_create(name=name)
