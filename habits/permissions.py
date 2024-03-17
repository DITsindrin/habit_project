from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Валидация для владельца привычки """
    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True


class IsStaff(BasePermission):
    """ Валидация для пользователя с правами is_staff """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
