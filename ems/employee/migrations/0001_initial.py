# Generated by Django 2.0.6 on 2019-07-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=10)),
                ('salary', models.CharField(max_length=20)),
                ('headpic', models.ImageField(upload_to='pics')),
            ],
            options={
                'db_table': 'emplist',
            },
        ),
    ]
