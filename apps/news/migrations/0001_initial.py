# Generated by Django 5.1.7 on 2025-03-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
