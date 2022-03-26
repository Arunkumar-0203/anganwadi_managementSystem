# Generated by Django 3.2.12 on 2022-03-10 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anganwadi_app', '0025_alter_tbl_healthtips_a_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=300, null=True)),
                ('user_contact', models.CharField(max_length=300, null=True)),
                ('user_email', models.CharField(max_length=300, null=True)),
                ('user_username', models.CharField(max_length=300, null=True)),
                ('user_password', models.CharField(max_length=300, null=True)),
                ('usser_confirm', models.CharField(max_length=300, null=True)),
                ('user_housename', models.CharField(max_length=300, null=True)),
                ('user_street', models.CharField(max_length=300, null=True)),
                ('user_pincode', models.CharField(max_length=300, null=True)),
                ('user_certificate', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('user_age', models.CharField(max_length=300, null=True)),
                ('user_status', models.CharField(max_length=300, null=True)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.location')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_pwomens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwomen_name', models.CharField(max_length=300, null=True)),
                ('pwomen_husbandname', models.CharField(max_length=300, null=True)),
                ('pwomen_contact', models.CharField(max_length=300, null=True)),
                ('pwomen_medicalproof', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('pwomen_photo', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('pwomen_email', models.CharField(max_length=300, null=True)),
                ('pwomen_isactive', models.CharField(max_length=300, null=True)),
                ('pwomen_username', models.CharField(max_length=300, null=True)),
                ('pwomen_password', models.CharField(max_length=300, null=True)),
                ('pwomen_confirmpassword', models.CharField(max_length=300, null=True)),
                ('p_street', models.CharField(max_length=300, null=True)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.location')),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
