# Generated by Django 2.1.5 on 2019-02-16 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190216_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='num_rev',
            new_name='number_of_reviews',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publ_date',
            new_name='publication_date',
        ),
    ]