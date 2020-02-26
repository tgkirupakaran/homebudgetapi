# Generated by Django 3.0.3 on 2020-02-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=2000)),
                ('type', models.CharField(choices=[('Payable', 'Payable'), ('Receivable', 'Receivable'), ('Paid', 'Paid'), ('Recieved', 'Recieved')], default='Paid', max_length=100)),
            ],
        ),
    ]