# Generated by Django 2.1.2 on 2018-11-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(choices=[('Lor', 'Lor'), ('Mede', 'Mede'), ('Onkoloq', 'Onkoloq'), ('Kardioloq', 'Kardioloq')], max_length=12)),
                ('Stage', models.IntegerField(null=True)),
                ('Level', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(default='', editable=False, max_length=130, unique=True)),
                ('age', models.IntegerField(null=True)),
                ('clinic', models.ManyToManyField(to='clinic.Clinic')),
            ],
        ),
    ]
