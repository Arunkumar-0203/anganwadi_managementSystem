# Generated by Django 3.2.12 on 2022-03-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anganwadi_app', '0005_anganawadi'),
    ]

    operations = [
        migrations.AddField(
            model_name='anganawadi',
            name='a_confirmpsw',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
