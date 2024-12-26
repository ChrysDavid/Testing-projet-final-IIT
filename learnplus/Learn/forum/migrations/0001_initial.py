# Generated by Django 2.2.12 on 2024-12-24 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('titre', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('cours', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cours_forum', to='school.Cours')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sujet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sujet',
                'verbose_name_plural': 'Sujets',
            },
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('sujet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sujet_reponse', to='forum.Sujet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reponse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reponse',
                'verbose_name_plural': 'Reponses',
            },
        ),
    ]
