# Generated by Django 2.1.3 on 2018-11-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairways', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media/gallery/')),
            ],
        ),
    ]
