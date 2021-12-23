# Generated by Django 3.2.9 on 2021-12-23 18:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0004_auto_20211223_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='slug',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True),
        ),
    ]