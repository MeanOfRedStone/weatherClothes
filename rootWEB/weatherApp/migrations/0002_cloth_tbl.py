# Generated by Django 4.1.7 on 2023-04-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cloth_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadMonth', models.IntegerField(default=0)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
