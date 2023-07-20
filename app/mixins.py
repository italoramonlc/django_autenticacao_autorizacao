from django.contrib.auth.mixins import UserPassesTestMixin


class GerentePermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.cargo == 1
