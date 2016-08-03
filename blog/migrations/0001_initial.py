# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 16:18
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_num', blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[blog.validators.MinLengthValidator(3)], verbose_name='제목')),
                ('content', models.TextField(help_text='Mark Down 문법을 써주세요')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('lnglat', models.CharField(help_text='경도, 위도 포맷으로 입력', max_length=50, validators=[blog.validators.lnglat_validator])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_field', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
