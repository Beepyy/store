# Generated by Django 3.2.7 on 2021-12-06 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bg', to='app.bought'),
        ),
    ]
