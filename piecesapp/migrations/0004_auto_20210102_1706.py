# Generated by Django 3.1.4 on 2021-01-02 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('piecesapp', '0003_auto_20210102_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieces',
            name='piece_id',
            field=models.AutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]