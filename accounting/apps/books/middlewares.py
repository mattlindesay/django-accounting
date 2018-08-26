from .utils import organization_manager


class AutoSelectOrganizationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user or not request.user.is_authenticated():
            return self.get_response(request)

        orga = organization_manager.get_selected_organization(request)
        if orga is not None:
            return self.get_response(request)

        user_orgas = organization_manager.get_user_organizations(request.user)
        if user_orgas.count():
            orga = user_orgas.first()
            organization_manager.set_selected_organization(request, orga)

        return self.get_response(request)
