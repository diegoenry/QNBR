# Generated by Django 2.1.7 on 2019-04-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='countryID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='merchants',
            name='merchantID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='orderItemID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='productID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='userID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
