# Generated by Django 4.1.7 on 2023-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
