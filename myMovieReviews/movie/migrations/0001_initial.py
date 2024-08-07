# Generated by Django 5.0.6 on 2024-07-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('openingDate', models.DateTimeField(blank=True, null=True)),
                ('genre', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=20)),
                ('runningtime', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('director', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=20)),
            ],
        ),
    ]
