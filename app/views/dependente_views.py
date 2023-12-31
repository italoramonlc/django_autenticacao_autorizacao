from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms.dependente_forms import DependenteForm
from app.models import Dependente


class DependenteCreateView(LoginRequiredMixin,CreateView):
    model = Dependente
    form_class = DependenteForm
    template_name = "dependentes/form_dependente.html"
    success_url = "lista_dependentes"


class DependenteListView(LoginRequiredMixin,ListView):
    model = Dependente
    template_name = "dependentes/lista_dependentes.html"