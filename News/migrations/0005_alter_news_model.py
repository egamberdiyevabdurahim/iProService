# Generated by Django 5.0.2 on 2024-02-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='model',
            field=models.CharField(blank=True, choices=[('Samsung', 'Samsung'), ('MI', 'MI'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('Vivo', 'Vivo'), ('htc', 'htc')], max_length=100, null=True),
        ),
    ]
