# Generated by Django 3.0.6 on 2020-05-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200515_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='status_1',
            new_name='status_comment',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='status_2',
            new_name='status_date',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_img',
            field=models.URLField(null=True),
        ),
    ]
