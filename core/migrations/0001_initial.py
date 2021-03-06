# Generated by Django 2.2.2 on 2019-06-08 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IdMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the student', max_length=50, verbose_name='Student Name')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std', models.CharField(help_text='Define Standard/Class', max_length=50, verbose_name='Result Standard')),
                ('year', models.PositiveSmallIntegerField(default=2019, help_text='What was passing year', verbose_name='Passing Year')),
                ('sci', models.FloatField(default=0.0, help_text='Define Science Marks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Science Marks')),
                ('math', models.FloatField(default=0.0, help_text='Define Maths Marks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Maths Marks')),
                ('language', models.FloatField(default=0.0, help_text='Define Language Marks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Language Marks')),
                ('social', models.FloatField(default=0.0, help_text='Define Social Marks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Social Marks')),
                ('total', models.FloatField(default=0.0, help_text='Define Total Marks', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Total Marks Of Student')),
                ('grade', models.CharField(help_text='Define Grade such as A, A+, etc', max_length=5, verbose_name='Grade As Per Result')),
                ('pass_fail', models.BooleanField(default=True, help_text='Tick if the student is pass', verbose_name='Pass Or Fail')),
                ('students', models.ForeignKey(help_text='Select a Student', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.IdMapping')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_ip', models.GenericIPAddressField(verbose_name='IP Address')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
