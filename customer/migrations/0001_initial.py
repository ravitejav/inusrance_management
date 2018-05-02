# Generated by Django 2.0.4 on 2018-04-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0002_auto_20180410_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('Fname', models.CharField(max_length=80)),
                ('Lname', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField(max_length=15)),
                ('age', models.IntegerField(max_length=100)),
                ('sex', models.CharField(max_length=1)),
                ('DOB', models.DateField()),
                ('cust_id', models.IntegerField(max_length=40, primary_key=True, serialize=False)),
                ('Cagent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.agent')),
            ],
        ),
        migrations.CreateModel(
            name='policy',
            fields=[
                ('policy_num', models.IntegerField(primary_key=True, serialize=False)),
                ('policy_code', models.CharField(max_length=3)),
            ],
        ),
    ]
