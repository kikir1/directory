# Generated by Django 3.0.7 on 2020-08-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20200823_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='version',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='directory',
            unique_together={('id', 'version')},
        ),
    ]
