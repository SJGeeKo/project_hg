# Generated by Django 2.1.1 on 2018-12-19 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_paintereng'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaintingEng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('material', models.CharField(default='Oil', max_length=250)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(default=100000)),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Painting')),
            ],
        ),
        migrations.RemoveField(
            model_name='paintereng',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='paintereng',
            name='slug',
        ),
    ]
