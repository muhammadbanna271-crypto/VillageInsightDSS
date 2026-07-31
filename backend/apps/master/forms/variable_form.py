from common.forms import BootstrapModelForm

from apps.master.models import Variable


class VariableForm(BootstrapModelForm):

    class Meta:

        model = Variable

        fields = (
            "code",
            "name",
            "description",
            "weight",
            "is_active",
        )