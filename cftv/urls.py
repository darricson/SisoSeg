from django.urls import path
from cftv.views import list_orcamento, new_orcamento_cftv, update_orcamento, delete_orcamento, detail_orcamento

urlpatterns = [

    path('/orcamento_cftv', list_orcamento, name='orcamento_cftv'),
    path('/new_orc_cftv', new_orcamento_cftv, name='new_orc_cftv'),
    path('/update_orc_cftv/<int:id>', update_orcamento, name='update_orc_cftv'),
    path('/delete_orc_cftv/<int:id>', delete_orcamento, name='delete_orc_cftv'),
    path('/detail_orcamento/<int:id>', detail_orcamento, name='detail_orcamento'),
]
