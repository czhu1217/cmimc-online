# Generated by Django 3.1.1 on 2020-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200913_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(default='Math Round', max_length=100),
            preserve_default=False,
        ),
    ]
