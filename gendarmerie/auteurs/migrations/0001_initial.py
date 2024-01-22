# Generated by Django 4.2.9 on 2024-01-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateField(null=True)),
                ('Address', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]