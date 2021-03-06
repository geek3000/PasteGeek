# Generated by Django 3.0.1 on 2019-12-30 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('paste_text', models.TextField()),
                ('p_language', models.CharField(default='plaintext', max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date')),
                ('user', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'paste',
                'ordering': ['date'],
            },
        ),
    ]
