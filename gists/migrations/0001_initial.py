# Generated by Django 2.1 on 2018-08-16 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharable', models.BooleanField()),
                ('code', models.TextField()),
                ('expiration', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]