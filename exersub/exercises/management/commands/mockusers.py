from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from exercises.models import CUser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Make mock users for testing purposes'

    def handle(self, *args, **options):
        print('Existing CUsers:')
        cusers = CUser.objects.all()
        print(cusers)
        first_names = ['Arne', 'Berit', 'Camilla', 'David']
        last_names = ['Olsen', 'Fredriksen', 'Jensen']
        for last in last_names:
            for first in first_names:
                username = (first + last).lower()
                # User.objects.get(username=username).delete()
                pwd = 'beepbeep'
                email = first + '@' + last + '.com'
                print('Creating ' + username)
                try:
                    new_cuser = CUser.make(username=username, password=pwd, email=email,
                                    first_name=first, last_name=last)
                    # new_cuser.save()
                except IntegrityError as e:
                    print(e)

