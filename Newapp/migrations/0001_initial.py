# Generated by Django 2.2 on 2020-10-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=65)),
            ],
        ),
    ]
