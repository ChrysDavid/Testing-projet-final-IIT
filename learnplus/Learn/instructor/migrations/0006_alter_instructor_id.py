# Generated by Django 3.2.25 on 2024-12-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_instructor_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
