# Generated by Django 2.1.3 on 2018-11-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chapter_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY_ID', models.CharField(max_length=10000)),
                ('SUB_CATEGORY_ID', models.CharField(max_length=100)),
                ('EXAM_ID', models.CharField(max_length=100)),
                ('CHAPTER_NAME', models.CharField(max_length=100)),
                ('ACTIVE_STATUS', models.CharField(max_length=40)),
                ('CREATED_DATE', models.DateTimeField()),
            ],
        ),
    ]
