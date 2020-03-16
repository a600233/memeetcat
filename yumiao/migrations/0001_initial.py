# Generated by Django 2.1.5 on 2020-03-16 20:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.CharField(max_length=20)),
                ('adminname', models.CharField(max_length=20)),
                ('adminpassword', models.CharField(max_length=20)),
                ('adminemail', models.CharField(max_length=20)),
                ('admintelephone', models.IntegerField()),
                ('adminauthority', models.IntegerField()),
            ],
            options={
                'db_table': 'admin',
                'ordering': ['id'],
            },
            managers=[
                ('administratorObj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=20)),
                ('appname', models.CharField(max_length=20)),
                ('appreason', models.CharField(max_length=100)),
                ('applocation', models.CharField(max_length=100)),
                ('appgender', models.BooleanField(default=True)),
                ('appage', models.IntegerField()),
                ('appincome', models.IntegerField()),
            ],
            options={
                'db_table': 'application',
                'ordering': ['id'],
            },
            managers=[
                ('appObj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catid', models.CharField(max_length=20)),
                ('catname', models.CharField(max_length=20)),
                ('catlocation', models.CharField(max_length=100)),
                ('catintroduction', models.CharField(max_length=100)),
                ('catbreed', models.CharField(max_length=100)),
                ('catage', models.IntegerField()),
                ('catpicture', models.ImageField(null=True, upload_to='img')),
            ],
            options={
                'db_table': 'cat',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('userpassword', models.CharField(max_length=20)),
                ('usertelephone', models.IntegerField()),
                ('useremail', models.CharField(max_length=20)),
                ('usergender', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['id'],
            },
            managers=[
                ('userObj', django.db.models.manager.Manager()),
            ],
        ),
    ]
