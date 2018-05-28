#!/usr/bin/env python
import requests

class Conversion:
    def __init__(self, a="ARK", b="KAPU"):
        self.a = self.testing(a)
        self.b = self.testing(b)

    def conversion_rate(self):
        url = "https://min-api.cryptocompare.com/data/pricemulti"
        fsyms = self.a+','+self.b
        tsyms = "USD"
        
        #set request params
        params = {"fsyms": fsyms,
                  "tsyms": tsyms}
        
        r = requests.get(url, params=params)
        
        #hard code for persona and ark test site
        if self.a == 'PERSONA' and self.b == 'ARK':
            p_val = 0.20
            a_val = 2.40
            self.conversion_rate = round((a_val / p_val),8)
        else:
            self.conversion_rate = round((r.json()[self.b][tsyms] / r.json()[self.a][tsyms]),8)
        
        return self.conversion_rate 
    
    def testing(self, a):
        # Convert for coins that don't have exchanges for testing
        test = {'dkapu': 'kapu', 
                   'dark': 'ark',
                   'persona-t': 'kapu',
                   'lwf-t': 'xrp',
                   'shift-t': 'shift'}
        
        if a in test.keys():
            return test[a].upper()
        else:
            return a.upper()
