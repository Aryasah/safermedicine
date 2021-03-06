# Generated by Django 3.1.7 on 2021-04-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=122, null=True)),
                ('lname', models.CharField(blank=True, max_length=122, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=122, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('desc', models.TextField(blank=True, default='none', null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=122, null=True)),
                ('month', models.IntegerField(blank=True, max_length=4, null=True)),
                ('year', models.IntegerField(blank=True, max_length=4, null=True)),
                ('cardNumber', models.IntegerField(blank=True, default='none', null=True)),
                ('cvv', models.IntegerField(blank=True, max_length=4, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
