# Generated by Django 5.0.2 on 2024-02-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetlog',
            name='employee',
        ),
        migrations.AddField(
            model_name='assetlog',
            name='employee',
            field=models.ManyToManyField(related_name='employee_log', to='corporate_assets.employee'),
        ),
    ]
