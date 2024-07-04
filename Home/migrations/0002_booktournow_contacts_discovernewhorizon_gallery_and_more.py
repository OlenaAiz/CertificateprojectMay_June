# Generated by Django 5.0.6 on 2024-05-27 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTourNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('buttonname', models.CharField(max_length=100, unique=True)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Book A Tour Now',
                'verbose_name_plural': 'Book A Tour Now',
                'ordering': ('description1',),
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.TextField(max_length=20)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('address',),
            },
        ),
        migrations.CreateModel(
            name='DiscoverNewHorizon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='discoverNewHorizon/%Y/%m/%d/')),
                ('buttonname', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Discover New Horizon',
                'verbose_name_plural': 'Discover New Horizons',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Our Service',
                'verbose_name_plural': 'Our Services',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OurStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('phone_number', models.TextField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='ourStaff/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Our Staff',
                'verbose_name_plural': 'Our Staff',
                'ordering': ('position',),
            },
        ),
        migrations.AlterModelOptions(
            name='createyourtourstyle',
            options={'ordering': ('sort',), 'verbose_name': 'Tour Style', 'verbose_name_plural': 'Tour Styles'},
        ),
        migrations.CreateModel(
            name='HotTours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=4, max_digits=8)),
                ('reviewstar', models.PositiveSmallIntegerField()),
                ('reviews', models.PositiveSmallIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='hotTours/%Y/%m/%d/')),
                ('is_visible', models.BooleanField(default=True)),
                ('tourstyle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours',
                                                to='Home.createyourtourstyle')),
            ],
            options={
                'verbose_name': 'Hot Tour',
                'verbose_name_plural': 'Hot Tours',
                'ordering': ('date',),
            },
        ),
    ]