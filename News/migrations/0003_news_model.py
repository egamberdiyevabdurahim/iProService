# Generated by Django 5.0.2 on 2024-02-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='model',
            field=models.CharField(choices=[('Samsung', 'Samsung'), ('MI', 'MI'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('Vivo', 'Vivo'), ('htc', 'htc')], max_length=100, null=True),
        ),
    ]
