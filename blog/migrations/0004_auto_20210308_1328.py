# Generated by Django 3.1.5 on 2021-03-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210307_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=200),
        ),
    ]
