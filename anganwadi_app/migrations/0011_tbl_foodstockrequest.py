# Generated by Django 3.2.12 on 2022-03-09 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anganwadi_app', '0010_tbl_foodstock_tbl_totalfoodstock'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_foodstockrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fsrequest_date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(max_length=100, null=True)),
                ('f_status', models.CharField(max_length=100, null=True)),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dofficer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.districtofficer')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anganwadi_app.tbl_userfood')),
            ],
        ),
    ]
