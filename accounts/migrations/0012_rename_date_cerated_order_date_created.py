# Generated by Django 4.2.4 on 2023-08-31 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_date_created_order_date_cerated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_cerated',
            new_name='date_created',
        ),
    ]
