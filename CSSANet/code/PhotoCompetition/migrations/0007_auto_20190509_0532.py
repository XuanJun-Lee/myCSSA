# Generated by Django 2.2.1 on 2019-05-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoCompetition', '0006_auto_20190509_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='categoryType',
            field=models.CharField(choices=[('Nature', '风景'), ('Culture', '人文')], default='Nature', max_length=30, null=True, verbose_name='题材类型'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='deviceType',
            field=models.CharField(choices=[('MobilePhone', '手机'), ('Camera', '相机')], default='MobilePhone', max_length=30, null=True, verbose_name='设备类型'),
        ),
    ]
