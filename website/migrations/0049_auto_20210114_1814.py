# Generated by Django 3.1.5 on 2021-01-14 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0048_auto_20210112_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='grader_data',
        ),
        migrations.RemoveField(
            model_name='score',
            name='task_scores',
        ),
        migrations.AddField(
            model_name='task',
            name='best_raw_points',
            field=models.FloatField(default=0.0),
        ),
    ]
