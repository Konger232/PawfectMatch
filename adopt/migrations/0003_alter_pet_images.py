# Generated by Django 5.0.1 on 2024-04-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_remove_user_is_foster_family_remove_user_is_shelter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='images',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
