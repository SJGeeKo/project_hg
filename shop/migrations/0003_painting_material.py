# Generated by Django 2.1.1 on 2018-10-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_painter_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='material',
            field=models.CharField(default='Oil', max_length=250),
        ),
    ]
