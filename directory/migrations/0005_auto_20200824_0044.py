# Generated by Django 3.1 on 2020-08-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20200824_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
