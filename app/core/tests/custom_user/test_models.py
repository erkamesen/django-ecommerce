import pytest
from custom_user.models import CustomUser


@pytest.mark.django_db
class TestCustomUserModel:

    def test_str_method(self, custom_user_factory):
        custom_user = custom_user_factory()
        representation = custom_user.__str__()
        assert representation.startswith("test_") and \
            representation.endswith("@mail.com")

    def test_has_module_perms(self, custom_user_factory):
        custom_user = custom_user_factory()
        assert custom_user.has_module_perms("test")

    def test_has_perm(self, custom_user_factory):
        custom_user = custom_user_factory()
        assert custom_user.has_perm("test")

    def test_create_superuser_succesfull(self):
        superuser = CustomUser.objects.create_superuser(
            email="test@mail.com",
            password="test3142"
        )
        assert superuser.is_superuser
        assert superuser.is_staff

    def test_create_user_without_mail(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(
                email="",
                password="test3142"
            )
