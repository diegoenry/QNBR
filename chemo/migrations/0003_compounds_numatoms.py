# Generated by Django 2.2.3 on 2019-07-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemo', '0002_compounds_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='compounds',
            name='numAtoms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]