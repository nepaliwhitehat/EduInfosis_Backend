# Generated by Django 2.1.5 on 2019-01-23 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Class')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarksEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('full_marks', models.IntegerField()),
                ('full_marks_th', models.IntegerField()),
                ('full_marks_pr', models.IntegerField()),
                ('pass_marks', models.IntegerField()),
                ('pass_marks_th', models.IntegerField()),
                ('pass_marks_pr', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Section')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='marksentry',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Subject'),
        ),
        migrations.AddField(
            model_name='examschedule',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.ExamTerm'),
        ),
        migrations.AddField(
            model_name='examschedule',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Subject'),
        ),
    ]
