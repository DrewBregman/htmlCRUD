# Generated by Django 3.1.7 on 2021-03-25 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0012_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='uProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifAccepted', models.BooleanField(default=False, null=True)),
                ('ifAdmin', models.BooleanField(default=False, null=True)),
                ('title', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uProj', to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
