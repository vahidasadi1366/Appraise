# Generated by Django 2.2.1 on 2019-07-05 16:42
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0010_merge_20190517_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='packageFile',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to='Packages',
                verbose_name='Package file',
            ),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='batches',
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name='campaign_campaign_batches',
                related_query_name='campaign_campaigns',
                to='Campaign.CampaignData',
                verbose_name='Batches',
            ),
        ),
    ]
