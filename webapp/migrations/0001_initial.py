# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('Age', models.IntegerField(default=19)),
                ('memo', models.TextField(default='xxaa')),
                ('createDate', models.DateTimeField(default='2017-08-05 12:12')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ZabbixGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ZabbixUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='zabbixgroup',
            name='relation',
            field=models.ManyToManyField(to='webapp.ZabbixUser'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='TypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.UserType'),
        ),
    ]
