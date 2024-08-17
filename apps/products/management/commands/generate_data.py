import os
from unittest.mock import patch

from django.conf import settings
from django.core.management import BaseCommand, call_command

from faker import Faker

from apps.products.documents import ProductDocument
from apps.products.models import Category, Product

fake = Faker()


def get_test_image():
    media_dir_path = settings.MEDIA_ROOT
    if not os.path.exists(media_dir_path):
        os.makedirs(media_dir_path)

    image_path = os.path.join(media_dir_path, 'test.jpg')
    if not os.path.exists(image_path):
        with open(image_path, 'wb') as f:
            f.write(fake.image())
    return 'test.jpg'


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        test_image = get_test_image()
        for _ in range(5):
            category = Category.objects.create(
                title=fake.text(50),
                description=fake.text(255),
                image=test_image
            )

            products = [
                Product(
                    title=fake.text(100),
                    description=fake.text(255),
                    price=10_000 * _ + 2300,
                    image=test_image,
                    category_id=category.id
                )
                for _ in range(100)
            ]
            Product.objects.bulk_create(products)

        with patch('builtins.input', return_value='Y'):
            call_command('search_index', '--rebuild')
        self.stdout.write(self.style.SUCCESS('Successfully generated data!'))
