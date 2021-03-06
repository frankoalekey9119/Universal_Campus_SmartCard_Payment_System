# Generated by Django 3.1.6 on 2021-02-16 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stationDetail',
            fields=[
                ('station', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('stationName', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('stationPersonelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='transactionDetail',
            fields=[
                ('transaction', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('UserID', models.CharField(max_length=50)),
                ('balance', models.IntegerField()),
                ('transactionAmount', models.IntegerField()),
                ('InOut', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='IntergrationPoint.stationdetail')),
            ],
        ),
        migrations.CreateModel(
            name='topUp',
            fields=[
                ('recharge', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cardId', models.CharField(max_length=50, null=True)),
                ('balance', models.IntegerField(null=True)),
                ('topUpAmount', models.IntegerField()),
                ('cardStatus', models.CharField(max_length=10, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='IntergrationPoint.stationdetail')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='recharge',
            fields=[
                ('recharge', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cardId', models.CharField(max_length=50)),
                ('balance', models.IntegerField()),
                ('transactionAmount', models.IntegerField()),
                ('cardStatus', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='IntergrationPoint.stationdetail')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
