# Generated by Django 4.2.1 on 2023-06-19 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('c_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField(max_length=100)),
                ('s_name', models.CharField(max_length=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
