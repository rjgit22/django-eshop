# Generated by Django 3.1.6 on 2021-05-19 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210519_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
