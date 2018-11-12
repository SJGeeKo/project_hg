# Generated by Django 2.1.1 on 2018-11-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_paintingimg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painter',
            name='image',
            field=models.ImageField(default="{% static 'img/profile_default.jpg' %}", upload_to='user_profile'),
        ),
        migrations.AlterField(
            model_name='paintingimg',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='paintingImgs'),
        ),
    ]