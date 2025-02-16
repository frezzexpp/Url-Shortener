# Generated by Django 5.1.5 on 2025-02-10 17:55

import projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_shortenedurl_short_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_link',
            field=models.CharField(default=projects.models.generate_short_link, max_length=100, unique=True),
        ),
    ]
