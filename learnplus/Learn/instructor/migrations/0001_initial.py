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
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='images/Instructor')),
                ('bio', models.TextField(default='Votre bio')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor_classe', to='school.Classe')),
                ('matieres', models.ManyToManyField(blank=True, related_name='instructors', to='school.Matiere')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
            },
        ),
        migrations.CreateModel(
            name='AffectationMatiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affectations', to='instructor.Instructor')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affectations', to='school.Matiere')),
            ],
            options={
                'verbose_name': 'Affectation de Matière',
                'verbose_name_plural': 'Affectations de Matières',
                'unique_together': {('instructor', 'matiere')},
            },
        ),
    ]
