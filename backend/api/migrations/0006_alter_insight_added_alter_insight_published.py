# Generated by Django 5.0.3 on 2024-03-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_insight_added_alter_insight_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='added',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='published',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
