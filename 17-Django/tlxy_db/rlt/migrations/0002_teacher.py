# Generated by Django 2.0.5 on 2018-09-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rlt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=20)),
                ('schools', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rlt.School')),
            ],
        ),
    ]