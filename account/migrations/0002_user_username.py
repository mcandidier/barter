# Generated by Django 3.1.1 on 2020-09-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
