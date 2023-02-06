from django.shortcuts import render
from django.http import HttpResponse
from .forms import Form_Coin
import requests

def coin_exchange(request):
    # Requisição por api dos cambios de moeda;

    api_rest_BRL = requests.get("http://economia.awesomeapi.com.br/last/BRL-USD,BRL-EUR")
    api_rest_USD = requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR")
    api_rest_EUR = requests.get("http://economia.awesomeapi.com.br/last/EUR-BRL,EUR-USD")
    api_rest_BTC = requests.get("http://economia.awesomeapi.com.br/last/BTC-BRL,BTC-USD,BTC-EUR")
    api_rest_ETH = requests.get("http://economia.awesomeapi.com.br/last/ETH-BRL,ETH-USD,ETH-EUR")
    
    # Precisamos obter valores do formato json

    api_rest_json_BRL = api_rest_BRL.json()
    api_rest_json_USD = api_rest_USD.json()
    api_rest_json_EUR = api_rest_EUR.json()
    api_rest_json_BTC = api_rest_BTC.json()
    api_rest_json_ETH = api_rest_ETH.json()

    # OBTENDO PREÇO PARA BRL ->USD,EUR     
    price_BRL_USD = api_rest_json_BRL["BRLUSD"]["bid"]
    price_BRL_EUR = api_rest_json_BRL["BRLEUR"]["bid"]
    
    # os dados chegam com formato str é preciso passar eles para float
    f_price_BRL_USD = float(price_BRL_USD)
    f_price_BRL_EUR = float(price_BRL_EUR)

    # OBTENDO PREÇO PARA USD ->BRL,EUR     
    price_USD_BRL = api_rest_json_USD["USDBRL"]["bid"]
    price_USD_EUR = api_rest_json_USD["USDEUR"]["bid"]

    # os dados chegam com formato str é preciso passar eles para float
    f_price_USD_BRL = float(price_USD_BRL)
    f_price_USD_EUR = float(price_USD_EUR)

    # OBTENDO PREÇO PARA EUR ->BRL,USD     
    price_EUR_BRL = api_rest_json_EUR["EURBRL"]["bid"]
    price_EUR_USD = api_rest_json_EUR["EURUSD"]["bid"]
    
    # os dados chegam com formato str é preciso passar eles para float
    f_price_EUR_BRL = float(price_EUR_BRL)
    f_price_EUR_USD = float(price_EUR_USD)

    # OBTENDO PREÇO PARA BTC ->BRL,USD,EUR     
    price_BTC_BRL = api_rest_json_BTC["BTCBRL"]["bid"]
    price_BTC_USD = api_rest_json_BTC["BTCUSD"]["bid"]
    price_BTC_EUR = api_rest_json_BTC["BTCEUR"]["bid"]

    # os dados chegam com formato str é preciso passar eles para float
    f_price_BTC_BRL = float(price_BTC_BRL)
    f_price_BTC_USD = float(price_BTC_USD)
    f_price_BTC_EUR = float(price_BTC_EUR)

    # OBTENDO PREÇO PARA ETH ->BRL,USD,EUR     
    price_ETH_BRL = api_rest_json_ETH["ETHBRL"]["bid"]
    price_ETH_USD = api_rest_json_ETH["ETHUSD"]["bid"]
    price_ETH_EUR = api_rest_json_ETH["ETHEUR"]["bid"]

    # os dados chegam com formato str é preciso passar eles para float
    f_price_ETH_BRL = float(price_ETH_BRL)
    f_price_ETH_USD = float(price_ETH_USD)
    f_price_ETH_EUR = float(price_ETH_EUR)

    
    if request.method == "GET":

        form = Form_Coin()
        
        context = {
            'form':form
        }

        return render(request, 'moeda/index.html', context=context)

    else:

        form = Form_Coin(request.POST)
        c_send_str = form.data['coin_send']
        c_send = float(c_send_str)

        type_send = form.data['type_send']

        type_return = form.data['type_return']
        
        form = Form_Coin()
        context = {
            'form':form
        }

        # Condição de funcionamento para o cambio de moeda
        ############  BRL  ############ 
        if type_send == 'BRL' and type_return == 'USD':
            
            cambio = round(c_send * f_price_BRL_USD,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"US$: {cambio}")

        if type_send == 'BRL' and type_return == 'EUR':
            cambio = round(c_send*f_price_BRL_EUR,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"€: {cambio}")
        
        if type_send == 'BRL' and type_return == 'BTC':
            valor_brl_btc = 1/f_price_BTC_BRL
            cambio = round(c_send*valor_brl_btc,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"BTC: {cambio}")

        if type_send == 'BRL' and type_return == 'ETH':
            valor_brl_eth = 1/f_price_ETH_BRL
            cambio = round(c_send*valor_brl_eth,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"ETH: {cambio}")

        ############  USD  ############ 
        
        if type_send == 'USD' and type_return == 'BRL':
            cambio = round(c_send*f_price_USD_BRL,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"R$: {cambio}")
        
        if type_send == 'USD' and type_return == 'EUR':
            cambio = round(c_send*f_price_USD_EUR,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"€: {cambio}")

        if type_send == 'USD' and type_return == 'BTC':
            valor_usd_btc = 1/f_price_BTC_USD
            cambio = round(c_send*valor_usd_btc,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"BTC: {cambio}")

        if type_send == 'USD' and type_return == 'ETH':
            valor_usd_eth = 1/f_price_ETH_USD
            cambio = round(c_send*valor_usd_eth,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"BTC: {cambio}")

        ############  EUR  ############ 

        if type_send == 'EUR' and type_return == 'BRL':
            cambio = round(c_send*f_price_EUR_BRL,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"R$: {cambio}")

        if type_send == 'EUR' and type_return == 'USD':
            cambio = round(c_send*f_price_EUR_USD,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"US$: {cambio}")

        if type_send == 'EUR' and type_return == 'BTC':
            valor_eur_btc = 1/f_price_BTC_EUR
            cambio = round(c_send*valor_eur_btc,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"BTC: {cambio}")

        if type_send == 'EUR' and type_return == 'ETH':
            valor_eur_eth = 1/f_price_ETH_EUR
            cambio = round(c_send*valor_eur_eth,6)
           
            context = {
            'form':form
            }
            return HttpResponse(f"ETH: {cambio}")

        ############  BTC  ############ 

        if type_send == 'BTC' and type_return == 'BRL':
            cambio = round(c_send*f_price_BTC_BRL,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"R$: {cambio}")
        
        if type_send == 'BTC' and type_return == 'USD':
            cambio = round(c_send*f_price_BTC_USD,2)
           
            context = {
            'form':form
            }
            return HttpResponse(F"US${cambio}")

        if type_send == 'BTC' and type_return == 'EUR':
            cambio = round(c_send*f_price_BTC_EUR,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"€: {cambio}")

        ############  ETH  ############ 
        
        if type_send == 'ETH' and type_return == 'BRL':
            cambio = round(c_send*f_price_ETH_BRL,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"R$: {cambio}")
        
        if type_send == 'ETH' and type_return == 'USD':
            cambio = round(c_send*f_price_ETH_USD,2)
           
            context = {
            'form':form
            }
            return HttpResponse(F"US$ : {cambio}")

        if type_send == 'ETH' and type_return == 'EUR':
            cambio = round(c_send*f_price_ETH_EUR,2)
           
            context = {
            'form':form
            }
            return HttpResponse(f"€: {cambio}")

        

        return render(request, 'moeda/index.html', context=context)
   