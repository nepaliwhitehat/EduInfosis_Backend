# Generated by Django 2.1.5 on 2019-02-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_auto_20190211_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpayment',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'Fully PAID'), (2, 'PARTIALLY PAID')], default=1),
            preserve_default=False,
        ),
    ]