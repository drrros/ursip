from django.urls import path

from .views import UploadFileView, CompanyDataView, CompanyDataViewByDate

urlpatterns = [
    path('', UploadFileView.as_view(), name='index'),
    path('results/', CompanyDataView.as_view(), name='results'),
    path('totals/', CompanyDataViewByDate.as_view(), name='totals'),
]
