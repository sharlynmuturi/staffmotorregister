# Generated by Django 5.0.3 on 2024-03-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffno', models.IntegerField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('organizationalunit', models.CharField(max_length=100)),
                ('subarea', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField(max_length=100)),
                ('idno', models.IntegerField(max_length=100)),
                ('krapin', models.IntegerField(max_length=100)),
            ],
        ),
    ]
