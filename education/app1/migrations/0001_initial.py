# Generated by Django 5.0.2 on 2024-02-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id      ', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name    ', models.CharField(max_length=20)),
                ('phone   ', models.IntegerField()),
                ('email   ', models.CharField(max_length=40)),
                ('stu_name', models.CharField(max_length=20)),
                ('msg     ', models.CharField(max_length=20)),
            ],
        ),
    ]
