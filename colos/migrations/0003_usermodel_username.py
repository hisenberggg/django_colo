# Generated by Django 3.1.6 on 2021-02-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colos', '0002_auto_20210218_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='userName',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
