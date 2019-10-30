from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):# является ли мето этого запроса безопасным
    def has_object_permission(self, request, view, obj):# является ли мето этого запроса безопасным
        if request.method in permissions.SAFE_METHODS:# если безопасный вернёт тру
            return True
        return obj.user == request.user# если нет(post delete) сравнит объект юзера с запросом юзера