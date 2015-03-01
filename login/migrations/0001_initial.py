# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=75)),
                ('request_date', models.DateField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Password reset audit',
                'verbose_name': 'Password reset audit',
            },
            bases=(models.Model,),
        ),
    ]
