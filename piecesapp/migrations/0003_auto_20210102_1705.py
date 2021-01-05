# Generated by Django 3.1.4 on 2021-01-02 20:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('piecesapp', '0002_auto_20210102_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='boardpiece_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piecesapp.pieces'),
        ),
        migrations.AlterField(
            model_name='pieces',
            name='piece_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]