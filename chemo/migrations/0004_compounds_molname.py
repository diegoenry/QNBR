# Generated by Django 2.2.3 on 2019-07-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemo', '0003_compounds_numatoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='compounds',
            name='molName',
            field=models.CharField(default='unkown', max_length=120),
            preserve_default=False,
        ),
    ]
