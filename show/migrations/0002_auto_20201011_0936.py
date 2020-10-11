# Generated by Django 3.1.2 on 2020-10-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='show',
            name='next_ep',
            field=models.DateField(null=True),
        ),
    ]
