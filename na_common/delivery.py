DELIVERY_ZONES = [
    {
        'name': 'UK', 'codes': 'GB', 'price': 2.00
    }, {
        # https://www.royalmail.com/international-zones#europe
        'name': 'Europe',
        'codes': 'AL,AD,AM,AT,AZ,BY,BE,BA,BG,HR,CY,CZ,DK,EE,FO,FI,FR,GE,DE,GI,GR,GL,HU,IS,IE,IT,'
                    'KZ,KG,LV,LI,LT,LU,MK,MT,MD,MC,ME,NL,NO,PL,PT,RO,RU,SM,RS,SK,ES,SE,CH,TJ,TR,TM,'
                    'UA,UZ,VA',
        'price': 4.50
    }, {
        'name': 'RoW',
        'codes': '',
        'price': 6.00
    }
]


DELIVERY_MISSING_ADDRESS = 'missing_address'
DELIVERY_REFUND = 'refund'
DELIVERY_EXTRA = 'extra'
DELIVERY_POSTAGE_EUROPE = 'postage_uk_europe'
DELIVERY_POSTAGE_ROW = 'postage_uk_row'


DELIVERY_STATUSES = [
    DELIVERY_MISSING_ADDRESS,
    DELIVERY_REFUND,
    DELIVERY_EXTRA,
    DELIVERY_POSTAGE_EUROPE,
    DELIVERY_POSTAGE_ROW
]
