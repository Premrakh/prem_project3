# Generated by Django 4.1.7 on 2023-03-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('pic', models.FileField(default='empty.png', upload_to='member_pic')),
            ],
        ),
    ]
