from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class Profile(TemplateMixin):

    template_name = "profile.html"

    show_profile = services.ShowProfile.show
    load_profile = repositories.load_profile

    @operation
    def get(show_profile, render, user):

        return render(show_profile(user))
