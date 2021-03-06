# Generated by Django 2.2.4 on 2020-06-20 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200618_0409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['band']},
        ),
        migrations.AlterModelOptions(
            name='band',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='band',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
