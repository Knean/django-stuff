# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-08 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('answer_image', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_text', models.TextField()),
                ('chapter_image', models.FileField(upload_to='uploads/')),
                ('create_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Chapter'),
        ),
    ]