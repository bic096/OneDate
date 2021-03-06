# Generated by Django 2.2.16 on 2020-11-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_delete_destined'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(choices=[('Human', 'Human'), ('Kuja', 'Kuja'), ('Ancestral giant', 'Ancestral giant'), ('Shandian', 'Shandian'), ('Clone', 'Clone'), ('Nobles', 'Nobles'), ('Reindeer', 'Reindeer'), ('Animal', 'Animal'), ('Gyojin', 'Gyojin'), ('Giant', 'Giant'), ('Triton', 'Triton'), ('Mink', 'Mink'), ('Long arms', 'Long arms'), ('Long legs', 'Long legs'), ('Three eyes', 'Three eyes'), ('Dwarf', 'Dwarf'), ('King', 'King'), ('Hybrid', 'Hybrid'), ('Cyborg', 'Cyborg'), ('Newkama', 'Newkama'), ('Zombie', 'Zombie'), ('Unknown', 'Unknown')], default='Human', max_length=20, verbose_name='Raza'),
        ),
    ]
