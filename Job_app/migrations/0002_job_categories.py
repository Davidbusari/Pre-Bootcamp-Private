# Generated by Django 2.2.4 on 2021-03-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Categories',
            field=models.TextField(default='all Categories'),
            preserve_default=False,
        ),
    ]
