# Generated by Django 4.2.7 on 2023-11-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
