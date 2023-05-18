# Generated by Django 4.2.1 on 2023-05-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('about', models.TextField(max_length=256, unique=True)),
                ('content', models.TextField(max_length=1024, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='posts/')),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
    ]
