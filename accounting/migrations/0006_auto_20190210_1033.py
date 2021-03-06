# Generated by Django 2.1.5 on 2019-02-10 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_studentpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('paid_amount', models.IntegerField()),
                ('fee_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.FeeCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='studentpayment',
            name='fee_category',
        ),
    ]
