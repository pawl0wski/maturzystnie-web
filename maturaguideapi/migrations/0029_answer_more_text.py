# Generated by Django 3.2.8 on 2021-10-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maturaguideapi', '0028_auto_20211020_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='more_text',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
