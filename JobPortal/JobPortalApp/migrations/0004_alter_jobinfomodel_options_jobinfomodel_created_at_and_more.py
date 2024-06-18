# Generated by Django 5.0.6 on 2024-06-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortalApp', '0003_seekermodel_github_seekermodel_linkedin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobinfomodel',
            options={'ordering': ['Created_at'], 'verbose_name': 'Job Info'},
        ),
        migrations.AddField(
            model_name='jobinfomodel',
            name='Created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='jobinfomodel',
            name='Updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
