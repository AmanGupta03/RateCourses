# Generated by Django 2.1.4 on 2019-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('domain', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('star', models.IntegerField(default=0)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]