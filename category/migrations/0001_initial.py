# Generated by Django 2.1.3 on 2018-11-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ca_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY_NAME', models.CharField(max_length=250)),
                ('ACTIVE_STATUS', models.CharField(max_length=10)),
                ('PRIORITY_STATUS', models.IntegerField()),
                ('CREATED_DATE', models.DateField()),
                ('cimage', models.CharField(max_length=1000)),
            ],
        ),
    ]
