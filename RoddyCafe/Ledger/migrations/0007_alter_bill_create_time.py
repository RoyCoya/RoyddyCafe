# Generated by Django 4.0.6 on 2023-03-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0006_alter_preference_default_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='create_time',
            field=models.DateTimeField(default=None, verbose_name='记录时间'),
            preserve_default=False,
        ),
    ]
