# Generated by Django 3.0.3 on 2020-02-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_bloodbag_total_ml'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbank',
            name='email',
            field=models.EmailField(default='ab@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodbank',
            name='password',
            field=models.CharField(default='123asd', max_length=400),
            preserve_default=False,
        ),
    ]
