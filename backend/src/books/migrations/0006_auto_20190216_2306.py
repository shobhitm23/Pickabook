# Generated by Django 2.1.5 on 2019-02-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190216_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='author_name',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FA', 'Fantasy'), ('RO', 'Romance'), ('TR', 'Thriller'), ('MY', 'Mystery'), ('BI', 'Biography'), ('FI', 'Fiction'), ('NF', 'Non Fiction'), ('SF', 'Science Fiction')], default='FA', max_length=2),
        ),
    ]
