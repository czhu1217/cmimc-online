# Generated by Django 3.1.7 on 2021-02-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0095_problem_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='google_form_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
