from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import UploadFileForm
from .models import CompanyData
from .parser import XLSParser


class UploadFileView(FormView):
    template_name = 'parser/index.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('results')

    def handle_uploaded_file(self, file):
        parser = XLSParser(file)
        parser.parse_and_save()

    def form_valid(self, form):
        self.handle_uploaded_file(self.request.FILES['file'])
        return super().form_valid(form)


class CompanyDataView(ListView):
    model = CompanyData
    template_name = 'parser/results.html'
    context_object_name = 'company_data'


class CompanyDataViewByDate(TemplateView):
    template_name = 'parser/results_by_date.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        totals = (
            CompanyData.objects
            .values('date', 'company')
            .annotate(
                Qoil_total=Sum(F('fact_qoil_data1') + F('fact_qoil_data2')),
                Qliq_total=Sum(F('fact_qliq_data1') + F('fact_qliq_data2'))
            )
            .order_by('date', 'company')
        )

        context['totals'] = totals
        return context
