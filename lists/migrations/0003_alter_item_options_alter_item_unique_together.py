# Generated by Django 4.1 on 2022-08-28 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list_item_text_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
