# Generated by Django 3.2 on 2021-04-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210412_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, max_length=122, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.CharField(blank=True, max_length=122, null=True)),
                ('picture', models.ImageField(upload_to='user')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='medname',
            field=models.TextField(blank=True, default='none', null=True),
        ),
    ]
