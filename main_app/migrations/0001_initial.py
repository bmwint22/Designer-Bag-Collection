from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('texture', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=50)),
            ],
        ),
    ]
