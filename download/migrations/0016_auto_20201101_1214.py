# Generated by Django 3.1.1 on 2020-11-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0015_auto_20201021_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='matiére',
            name='matiére',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]