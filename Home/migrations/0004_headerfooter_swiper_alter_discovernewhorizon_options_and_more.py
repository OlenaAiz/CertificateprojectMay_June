# Generated by Django 5.0.6 on 2024-06-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_ourservices_icon_alter_hottours_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='headerfooter')),
            ],
            options={
                'verbose_name': 'headerfooter',
                'verbose_name_plural': 'headerandfooter',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_swiper', models.ImageField(blank=True, null=True, upload_to='swiper')),
                ('advertise1', models.CharField(max_length=100, unique=True)),
                ('text12', models.CharField(max_length=100, unique=True)),
                ('text21', models.CharField(max_length=100, unique=True)),
                ('button', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ('text12',),
            },
        ),
        migrations.AlterModelOptions(
            name='discovernewhorizon',
            options={'ordering': ('text_name',), 'verbose_name': 'Discover New Horizon',
                     'verbose_name_plural': 'Discover New Horizons'},
        ),
        migrations.RenameField(
            model_name='discovernewhorizon',
            old_name='description',
            new_name='text_description',
        ),
        migrations.RenameField(
            model_name='discovernewhorizon',
            old_name='name',
            new_name='text_name',
        ),
        migrations.AddField(
            model_name='booktournow',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='booktournow'),
        ),
        migrations.AddField(
            model_name='createyourtourstyle',
            name='buttonname',
            field=models.CharField(default='exit', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createyourtourstyle',
            name='style_photo',
            field=models.ImageField(default='exit1', upload_to='createyourtourstyle/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discovernewhorizon',
            name='name_of_class',
            field=models.CharField(default='exit1', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hottours',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='hottours/'),
        ),
        migrations.AlterField(
            model_name='ourstaff',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ourstaff/%Y/%m/%d/'),
        ),
    ]
