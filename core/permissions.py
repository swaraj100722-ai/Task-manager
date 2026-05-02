from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to users with the 'Admin' role.
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        return request.user.role == 'Admin' or request.user.email.endswith('@task.com')

class IsProjectOwnerOrMember(permissions.BasePermission):
    """
    Allows access to the owner or members of a project.
    """
    def has_object_permission(self, request, view, obj):
        # obj can be a Project or a Task (if Task, check its project)
        if hasattr(obj, 'members'): # Project object
            return request.user == obj.owner or obj.members.filter(id=request.user.id).exists()
        elif hasattr(obj, 'project'): # Task object
            return request.user == obj.project.owner or obj.project.members.filter(id=request.user.id).exists()
        return False

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and (request.user.role == 'Admin' or request.user.email.endswith('@task.com'))
