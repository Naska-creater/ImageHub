from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class UserManager(BaseUserManager):
    def _create_user(self, email, phone, password=None, **extra_fields):
        with transaction.atomic():
            user = self.model(email=email, phone=phone, **extra_fields)
            if password:
                user.set_password(password)
            user.username = "user"
            user.save(using=self._db)
        return user

    def create_user(self,email, phone, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone, **extra_fields)

    def create_superuser(self,email, phone,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('nick_name', True)
        return self._create_user(email, phone,password, **extra_fields)