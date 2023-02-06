from django.urls import path
from moeda import views as v

app_name = 'moeda'

urlpatterns = [
    path('', v.coin_exchange, name='coin_exchange')
]