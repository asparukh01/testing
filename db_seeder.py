import os
import random

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from django_seed import Seed
from api_v1.models import Employee

seeder = Seed.seeder()



post = ['Старший директор', 'Директор', 'Помощник директора', 'Менеджер', 'Менеджер среднего звена']
fake = Faker('ru_RU')

seeder.add_entity(Employee, 50000, {
    'name': lambda x: fake.name(),
    'post': lambda x: random.choice(post),
    'salary': lambda x: random.randint(5000, 1000000000),
})
seeder.execute()
