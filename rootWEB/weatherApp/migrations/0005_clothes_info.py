# Generated by Django 4.1.7 on 2023-04-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0004_remove_photo_cloth_idx_delete_cloth_tbl_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLOTHES_INFO',
            fields=[
                ('CLOTHES_IDX', models.IntegerField(primary_key=True, serialize=False)),
                ('CLOTHES_MON', models.IntegerField()),
                ('CLOTHES_PNG', models.CharField(max_length=200)),
                ('CLOTHES_LOC', models.CharField(max_length=200)),
                ('CLOTHES_SHIRT_SHORT', models.IntegerField()),
                ('CLOTHES_SHIRT_LONG', models.IntegerField()),
                ('CLOTHES_SHIRT_SWEAT', models.IntegerField()),
                ('CLOTHES_SWEATER', models.IntegerField()),
                ('CLOTHES_SHIRT', models.IntegerField()),
                ('CLOTHES_BLOUS', models.IntegerField()),
                ('CLOTHES_ONEPICE', models.IntegerField()),
                ('CLOTHES_NEET', models.IntegerField()),
                ('CLOTHES_SHIRT_POLO', models.IntegerField()),
                ('CLOTHES_KARDIGUN', models.IntegerField()),
                ('CLOTHES_JUMPER', models.IntegerField()),
                ('CLOTHES_JACKET', models.IntegerField()),
                ('CLOTHES_COAT', models.IntegerField()),
                ('CLOTHES_PADDING', models.IntegerField()),
                ('CLOTHES_JEANS', models.IntegerField()),
                ('CLOTHES_PANTS_WINTER', models.IntegerField()),
                ('CLOTHES_PANTS_SUMMER', models.IntegerField()),
                ('CLOTHES_SKERT', models.IntegerField()),
                ('CLOTHES_PANTS_CAGO', models.IntegerField()),
                ('CLOTHES_SHOOSE_GUDU', models.IntegerField()),
                ('CLOTHES_SHOOSE_RUNNING', models.IntegerField()),
                ('CLOTHES_SHOOSE_SNIKERS', models.IntegerField()),
                ('CLOTHES_SHOOSE_SANDAL', models.IntegerField()),
                ('CLOTHES_SHOOSE_WAKER', models.IntegerField()),
                ('CLOTHES_SHOOSE_BOOTS', models.IntegerField()),
                ('CLOTHES_1', models.IntegerField()),
                ('CLOTHES_2', models.IntegerField()),
                ('CLOTHES_3', models.IntegerField()),
                ('CLOTHES_4', models.IntegerField()),
            ],
        ),
    ]
