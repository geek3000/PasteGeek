# Generated by Django 3.0.1 on 2019-12-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'comment',
                'ordering': ['comment'],
            },
        ),
    ]