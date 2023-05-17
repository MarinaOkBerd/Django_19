from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # products_list = [
        #     {'name': 'Milk Valio',
        #      'description': 'Молоко, жирность 2,5%, бренд Valio',
        #      'category': 'Milk',
        #      'price': 100.0,
        #      'date_of_creation': '2023-05-10',
        #      'last_modified_date': '2023-05-12'
        #      },
        #     {'name': 'Juice j7',
        #      'description': 'Cok, 1 литр, бренд j7',
        #      'category': 'Juice',
        #      'price': 150.0,
        #      'date_of_creation': '2023-05-11',
        #      'last_modified_date': '2023-05-14'},
        # ]
        category_list = [
            {'name': 'Water',
             'description': 'Вода, 1,5 литра'
             },
            {'name': 'Kvass',
             'description': 'Квас, 2 литра'
             },

        ]

        Category.objects.all().delete()

        category_objects = []
        for category_item in category_list:
            category_objects.append(Category(**category_item))

        Category.objects.bulk_create(category_objects)
