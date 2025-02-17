# Generated by Django 4.0.6 on 2023-03-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ledger', '0002_alter_bill_options_bill_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='name',
        ),
        migrations.AddField(
            model_name='bill',
            name='remark',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='收支记录id'),
        ),
    ]
