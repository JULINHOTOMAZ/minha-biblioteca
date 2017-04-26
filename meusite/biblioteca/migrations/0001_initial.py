# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=30)),
                ('editora', models.CharField(max_length=30)),
                ('paginas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prateleira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeGenero', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='prateleira',
            field=models.ForeignKey(to='biblioteca.Prateleira'),
        ),
    ]
