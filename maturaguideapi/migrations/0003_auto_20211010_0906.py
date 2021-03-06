# Generated by Django 3.2.8 on 2021-10-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maturaguideapi', '0002_questiontag'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(help_text='Nazwa kategori np. Słuchanie', max_length=128)),
                ('subject', models.ForeignKey(help_text='Przedmiot', on_delete=django.db.models.deletion.CASCADE, to='maturaguideapi.subject')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='header',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='explanation',
            name='content',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='questiontag',
            name='name',
            field=models.CharField(help_text='Nazwa tagu np. Jedzenie słownictwo', max_length=255),
        ),
        migrations.AlterField(
            model_name='questiontag',
            name='subject',
            field=models.ForeignKey(help_text='Przedmiot', on_delete=django.db.models.deletion.CASCADE, to='maturaguideapi.subject'),
        ),
        migrations.DeleteModel(
            name='AnswerCategory',
        ),
    ]
