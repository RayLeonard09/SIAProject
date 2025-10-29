from django.apps import AppConfig


class CctcaccountingsystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CCTCAccountingSystem'

    def ready(self):
        # Automatically create an admin account if it doesn't exist
        from django.contrib.auth.models import User
        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="admin123"
                )
                print("✅ Default admin account created:")
                print("   Username: admin")
                print("   Password: admin123")
        except Exception as e:
            # Avoid breaking startup if database isn't ready yet (like during migrations)
            print(f"⚠️ Skipped admin creation: {e}")
