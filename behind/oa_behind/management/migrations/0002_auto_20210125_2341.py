# Generated by Django 3.1.5 on 2021-01-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='user',
        ),
        migrations.RemoveField(
            model_name='management',
            name='username',
        ),
        migrations.AlterField(
            model_name='management',
            name='img',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='management',
            name='power',
            field=models.CharField(default='0', max_length=2, null=True, verbose_name='权限'),
        ),
    ]
