# Generated by Django 3.1.7 on 2021-05-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_Activities', '0004_student_info_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='my_choice',
            field=models.CharField(choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], default='empty', max_length=10),
            preserve_default=False,
        ),
    ]