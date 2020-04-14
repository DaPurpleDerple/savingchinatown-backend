# Generated by Django 3.0.4 on 2020-04-11 23:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0035_auto_20200411_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='place',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.FloatField(default=0.0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='lng',
            field=models.FloatField(default=0.0, editable=False),
            preserve_default=False,
        ),
    ]
