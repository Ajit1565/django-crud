# Generated by Django 3.1.1 on 2020-09-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200903_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
