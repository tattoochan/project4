# Generated by Django 2.0.2 on 2020-04-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hands', '0004_hands_info_portrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hands_info',
            name='portrait',
            field=models.ImageField(default='default_pic.png', null=True, upload_to='images/'),
        ),
    ]