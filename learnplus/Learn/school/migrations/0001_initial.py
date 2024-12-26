# Generated by Django 2.2.12 on 2024-12-24 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='ressources/cours')),
                ('duree_en_heure', models.PositiveIntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/chapitres')),
                ('description', models.TextField(default='Description du chapitre')),
                ('date_debut', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
                ('titre', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Chapitre',
                'verbose_name_plural': 'Chapitres',
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Filiere',
                'verbose_name_plural': 'Filieres',
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='images/matiere/')),
                ('description', models.TextField(default='Description du cours')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Matiere',
                'verbose_name_plural': 'Matieres',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Niveau',
                'verbose_name_plural': 'Niveaux',
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='images/cours')),
                ('video', models.FileField(null=True, upload_to='ressources/cours')),
                ('pdf', models.FileField(null=True, upload_to='ressources/cours')),
                ('description', models.TextField(default='Description du cours')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours_chapitre', to='school.Chapitre')),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Cours',
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroClasse', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('filiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classe_filiere', to='school.Filiere')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classe_niveau', to='school.Niveau')),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.AddField(
            model_name='chapitre',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classe_chapitre', to='school.Classe'),
        ),
        migrations.AddField(
            model_name='chapitre',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiere_chapitre', to='school.Matiere'),
        ),
    ]
