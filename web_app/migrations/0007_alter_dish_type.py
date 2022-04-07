# Generated by Django 3.2 on 2022-04-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_review_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='type',
            field=models.CharField(choices=[('Main', 'Main'), ('Side', 'Side'), ('Starter', 'Starter'), ('Dessert', 'Dessert'), ('Other', 'Other')], default='Main', max_length=100),
        ),
    ]
