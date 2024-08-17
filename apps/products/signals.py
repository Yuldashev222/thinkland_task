from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

from apps.products.documents import ProductDocument
from apps.products.models import Product, Category
from apps.products.services import (
    delete_object_files_after_delete,
    change_object_files_after_update
)


@receiver(post_delete, sender=Category)
def delete_object_files(instance, **kwargs):
    delete_object_files_after_delete(instance)


@receiver(pre_save, sender=Category)
def delete_object_files(instance, **kwargs):
    change_object_files_after_update(instance)


@receiver(post_delete, sender=Product)
def delete_object_files(instance, **kwargs):
    delete_object_files_after_delete(instance)


@receiver(pre_save, sender=Product)
def delete_object_files(instance, **kwargs):
    change_object_files_after_update(instance)

    # update index on changing object
    if instance.pk:
        obj = ProductDocument(
            meta={'id': instance.id},
            title=instance.title,
            description=instance.description,
            price=instance.price,
            image=instance.image.name,
            category_id=instance.category_id,
        )
        obj.save()
