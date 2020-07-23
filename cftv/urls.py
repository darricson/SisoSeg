from django.urls import path
from cftv.views import OrcamentocftvList

urlpatterns = [

    path('orcamento', OrcamentocftvList.as_view(), name='orcamento_list'),
]
