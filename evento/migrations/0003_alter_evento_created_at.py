# Generated by Django 3.2.5 on 2021-07-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_alter_evento_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='created_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
