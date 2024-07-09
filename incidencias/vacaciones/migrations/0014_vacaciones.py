# Generated by Django 4.2.13 on 2024-07-03 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacaciones', '0013_delete_vacaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('dias_totales', models.IntegerField(blank=True, null=True)),
                ('disfrutada', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vacacione',
                'verbose_name_plural': 'Vacaciones',
                'ordering': (['fecha_inicio'], ['usuario']),
            },
        ),
    ]