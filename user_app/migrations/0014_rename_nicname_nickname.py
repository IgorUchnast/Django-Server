from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('user_app', '0013_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nicname',
            new_name='nickname',
        ),
    ]
