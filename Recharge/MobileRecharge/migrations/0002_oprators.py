# Generated by Django 4.1.4 on 2022-12-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobileRecharge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oprators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oprator_name', models.CharField(blank=True, default='', max_length=100)),
                ('oprator_code', models.CharField(blank=True, default='', max_length=100)),
                ('oprator_type', models.CharField(blank=True, default='', max_length=100)),
                ('oprator_status', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
