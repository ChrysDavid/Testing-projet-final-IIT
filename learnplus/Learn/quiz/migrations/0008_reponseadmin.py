# Generated by Django 2.2.12 on 2024-12-26 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20241226_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReponseAdmin',
            fields=[
                ('reponse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Reponse')),
            ],
            bases=('quiz.reponse',),
        ),
    ]
