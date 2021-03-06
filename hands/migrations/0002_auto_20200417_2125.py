# Generated by Django 2.0.2 on 2020-04-17 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hands_info',
            name='hand_detail',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='hands_info',
            name='hand_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='hands_info',
            name='hand_skill',
            field=models.CharField(choices=[('Tutoring', 'Tutoring'), ('Gardening', 'Gardening'), ('Cleaning', 'Cleaning'), ('Delivery', 'Delivery'), ('Tele-calling', 'Tele-calling'), ('Others', 'Others')], default='Others', max_length=16),
        ),
    ]
