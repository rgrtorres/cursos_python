# Generated by Django 3.1.7 on 2021-03-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField()),
                ('data_criada', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
    ]