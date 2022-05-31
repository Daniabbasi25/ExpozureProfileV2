# Generated by Django 4.0.4 on 2022-05-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_links_icon_links_link_links_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='link_name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='links',
            name='name',
            field=models.CharField(choices=[('Youtube', 'Youtube'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Other_Links', 'Other_Links')], default='Other_Links', max_length=300),
        ),
        migrations.AlterField(
            model_name='profil',
            name='color',
            field=models.CharField(blank=True, default='#ff416c', max_length=300, null=True),
        ),
    ]
