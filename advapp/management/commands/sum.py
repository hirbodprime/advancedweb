from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num' , type=int)
        parser.add_argument('num2' , type=int)
        parser.add_argument('--add' , action='store_true')
        parser.add_argument('--minus' , action='store_true')
        
    def handle(self, *args, **options):
        num = options['num']
        num2 = options['num2']
        add = options['add']
        minus = options['minus']
        res = num + num2
        res2 = num - num2
        if add:
            self.stdout.write(self.style.SUCCESS(f'{num} + {num2} : {res}'))
        elif minus:
            self.stdout.write(self.style.WARNING(f'{num} - {num2} : {res2}'))
        else:
            self.stdout.write(self.style.WARNING(f'please use one of the commands --add --minus'))
        