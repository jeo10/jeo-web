from django.core.exceptions import PermissionDenied


class GroupRequiredMixin(object):
    group_required = []

    def dispatch(self, request, *args, **kwargs):
        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
            print(user_groups)
        if len(set(user_groups).intersection(self.group_required)) < len(self.group_required):
            print('no entra')
            print(len(set(user_groups).intersection(self.group_required)))
            raise PermissionDenied

        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
