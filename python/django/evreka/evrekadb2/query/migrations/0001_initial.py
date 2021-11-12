# Generated by Django 3.2.8 on 2021-11-12 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField(max_length=10)),
                ('longitutde', models.FloatField(max_length=10)),
                ('collection_frequency', models.IntegerField(max_length=10)),
                ('last_collection', models.DateTimeField(max_length=15)),
                ('operation', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='query.operation')),
            ],
        ),
    ]
