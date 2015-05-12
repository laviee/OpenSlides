from django.utils.translation import ugettext_lazy

from openslides.utils.main_menu import MainMenuEntry


class AssignmentMainMenuEntry(MainMenuEntry):
    """
    Main menu entry for the assignment app.
    """
    verbose_name = ugettext_lazy('Elections')
    required_permission = 'assignments.can_see'
    default_weight = 40
    pattern_name = '/assignments'  # TODO: use generic solution, see issue #1469
    icon_css_class = 'icon-assignment'
