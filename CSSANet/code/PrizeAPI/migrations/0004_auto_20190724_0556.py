# Generated by Django 2.2.3 on 2019-07-24 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrizeAPI', '0003_auto_20190716_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='prize_userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.UserProfile'),
        ),
    ]
