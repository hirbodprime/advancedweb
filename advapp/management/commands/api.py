from django.core.management.base import BaseCommand , CommandError



class Command(BaseCommand):
    # help = 'deletes the blog with api requests'
    def add_arguments(self, parser):
        parser.add_argument('id' , type=int)
        # if command delete is used action will be stored True if not false
        parser.add_argument('--delete' , action='store_true' , help='delete blog with id')
        parser.add_argument('--get' , action='store_true' , help='get blog with id')

    def handle(self, *args , **options):
        idblog = options['id']
        dele = options['delete']
        gete = options['get']
        bloge = f'blog with id {idblog} does not exist'
        from Drf.models import blogmodel
        if dele:   
            try:
                import requests
                # req = requests.delete(f'http://127.0.0.1:8000/drf/DeleteAPI/' + str(idblog) + '/')
                # print(req.text)
                blog = blogmodel.objects.get(id=idblog)
                blog.delete()
                self.stdout.write(self.style.SUCCESS(f'delete shod {blog.title}'))
            except blogmodel.DoesNotExist:
                raise CommandError(f'{bloge} does not exist')
        elif gete:
            try:
                import requests
                # req = requests.get(f'http://127.0.0.1:8000/drf/FindAPI/' + str(idblog) + '/')
                # print(req.text)
                blog = blogmodel.objects.get(id=idblog)
                self.stdout.write(self.style.SUCCESS(f'title: {blog.title} , writer: {blog.wrtier} , body: {blog.body} , date: {blog.date}'))
            except blogmodel.DoesNotExist:
                raise CommandError(f'{bloge} does not exist')
        else:
            self.stdout.write(self.style.WARNING(f'use one of the commands --get or --delete'))