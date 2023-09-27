# Generated by Django 4.1.3 on 2022-12-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shirt_size', models.CharField(choices=[('V', 'Vegetarian'), ('NV', 'Non-veg'), ('VV', 'Vegan')], max_length=5)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
