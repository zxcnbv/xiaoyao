# Generated by Django 2.0.5 on 2019-10-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='状态'),
        ),
    ]
