# Generated by Django 3.1.1 on 2020-10-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0013_auto_20201018_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='professeur',
            field=models.CharField(max_length=200),
        ),
    ]