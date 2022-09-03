# Generated by Django 4.1 on 2022-09-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asesoramientofiscal', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
                ('mail', models.EmailField(max_length=50, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Monotributista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
                ('mail', models.EmailField(max_length=50, unique=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableInscripto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sociedad', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
                ('mail', models.EmailField(max_length=50, unique=True, verbose_name='email')),
            ],
        ),
    ]