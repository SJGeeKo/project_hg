# Generated by Django 2.1.1 on 2018-11-27 15:32

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20181128_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painter',
            name='image',
            field=models.ImageField(default='user_profile/profile_default_Y-6i6KZW.jpg', upload_to=shop.models.profile_path),
        ),
    ]
