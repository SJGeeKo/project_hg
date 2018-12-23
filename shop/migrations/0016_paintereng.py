# Generated by Django 2.1.1 on 2018-12-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20181128_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='PainterEng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('birth', models.DateField()),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(blank=True)),
                ('painter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Painter')),
            ],
        ),
    ]