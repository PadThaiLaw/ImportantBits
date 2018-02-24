# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canlii_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500)),
                ('neutral_citation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cited_paragraph', models.PositiveIntegerField()),
                ('citing_paragraph', models.PositiveIntegerField()),
                ('sentiment_score', models.DecimalField(decimal_places=10, max_digits=12)),
                ('citation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Citation')),
            ],
        ),
        migrations.AddField(
            model_name='citation',
            name='cited_case_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cited_case', to='api.Decision'),
        ),
        migrations.AddField(
            model_name='citation',
            name='citing_case_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='citing_case', to='api.Decision'),
        ),
    ]
