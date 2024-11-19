from tkinter.messagebox import RETRY

from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if hasattr(view, 'queryset') and view.queryset is not None:
            model = view.queryset.model
        elif hasattr(view, 'get_queryset'):
            model = view.get_queryset().model
        else:
            #Especificar explicitamente el modelo desde la vista si no esta disponible
            model = getattr(view, 'queryset', None)
            if model is None:
                raise AttributeError('No se puede obtener el modelo para verificar los permisos')

        if request.method == 'GET':
            return request.user.has_perm(f'{model._meta.app_label}.view_{model._meta.model_name}')
        if request.method == 'POST':
            return request.user.has_perm(f'{model._meta.app_label}.add_{model._meta.model_name}')
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm(f'{obj._meta.app_label}.change_{obj._meta.model_name}')
        if request.method == 'DELETE':
            return request.user.has_perm(f'{obj._meta.app_label}.delete_{obj._meta.model_name}')
        return True