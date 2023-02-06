from django.db import models

class Model_coin(models.Model):

    CHOICES = (('BRL','BRL'),
                ('USD','USD'), 
                ('EUR','EUR'), 
                ('BTC','BTC'), 
                ('ETH','ETH'),
    )

    coin_send = models.FloatField(max_length=20)
    coin_return = models.FloatField(max_length=20)
    type_send = models.FloatField(choices=CHOICES)
    type_return = models.FloatField(choices=CHOICES)
    
    def __str__(self):
        return f"Coin ID: {self.pk}"
