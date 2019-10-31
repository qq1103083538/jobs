# Generated by Django 2.0.12 on 2019-10-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191030_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalcertificationorqualification',
            name='extra',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='额外的资料'),
        ),
        migrations.AlterField(
            model_name='thesisworks',
            name='extra',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='额外的资料'),
        ),
        migrations.AlterField(
            model_name='thesisworks',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='论文著作'),
        ),
        migrations.AlterField(
            model_name='thesisworks',
            name='obtain_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='获取时间'),
        ),
    ]
