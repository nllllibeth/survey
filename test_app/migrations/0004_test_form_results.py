# Generated by Django 4.2.2 on 2023-06-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_rename_result_test_form_correct_test_form_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_form',
            name='results',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]