# Generated by Django 5.1 on 2024-09-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0012_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]