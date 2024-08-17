import os

from django.core.files.storage import default_storage
from django.db import models


def delete_object_files_after_delete(obj: models.Model):
    """
    delete object files from server after delete obj
    :param obj:
    :return None:
    """
    for field in obj._meta.get_fields():
        if isinstance(field, (models.FileField, models.ImageField)):
            field = getattr(obj, field.name, None)
            if field and os.path.isfile(field.path):
                os.remove(field.path)


def change_object_files_after_update(obj: models.Model):
    """
    Change object files from server after update obj
    :param obj:
    :return None:
    """
    if not obj.pk:
        return
    print(222222222)
    for field in obj._meta.get_fields():
        if isinstance(field, (models.FileField, models.ImageField)):
            try:
                old_file = getattr(obj.__class__.objects.get(pk=obj.pk), field.name)
            except obj.DoesNotExist:
                continue

            new_file = getattr(obj, field.name, None)
            if (
                    old_file
                    and
                    old_file != new_file
                    and
                    default_storage.exists(old_file.path)
            ):
                default_storage.delete(old_file.path)
