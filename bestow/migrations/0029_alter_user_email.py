# Generated by Django 4.2.7 on 2024-02-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestow', '0028_filter_email_alter_filter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]