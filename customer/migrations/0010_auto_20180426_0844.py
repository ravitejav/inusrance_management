# Generated by Django 2.0.4 on 2018-04-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_nominee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy_holder',
            name='amt_pay',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policy_holder',
            name='term',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]