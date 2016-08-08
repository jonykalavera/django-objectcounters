# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the counter', max_length=128, verbose_name='counter name', db_index=True)),
                ('value', models.BigIntegerField(default=0, help_text='Current value of the counter', verbose_name='counter value')),
                ('object_id', models.PositiveIntegerField(db_index=True, null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name': 'Counter',
            },
        ),
        migrations.AlterUniqueTogether(
            name='counter',
            unique_together=set([('name', 'content_type', 'object_id')]),
        ),
    ]
