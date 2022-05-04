import requests
from django.core.management.base import BaseCommand
from recipes.models import Recipe

def get_data():
    return 1

def seed_data():
    return 1

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_data()
        print("seeding completed")

