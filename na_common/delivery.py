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


def get_delivery_zone(country_code):
    for zone in DELIVERY_ZONES:
        if country_code in zone['codes']:
            return zone
    return DELIVERY_ZONES[-1]  # Otherwise return RoW - Rest of the World


class statuses:
    DELIVERY_EXTRA = 'extra'
    DELIVERY_EXTRA_PAID = 'extra_paid'
    DELIVERY_MISSING_ADDRESS = 'missing_address'
    DELIVERY_PAID = 'paid'
    DELIVERY_NOT_PAID = 'no_delivery_fee'
    DELIVERY_POSTAGE_EUROPE = 'postage_uk_europe'
    DELIVERY_POSTAGE_ROW = 'postage_uk_row'
    DELIVERY_REFUND = 'refund'
    DELIVERY_REFUND_PAID = 'refund_paid'

    DELIVERY_STATUSES = [
        DELIVERY_EXTRA,
        DELIVERY_EXTRA_PAID,
        DELIVERY_MISSING_ADDRESS,
        DELIVERY_PAID,
        DELIVERY_POSTAGE_EUROPE,
        DELIVERY_POSTAGE_ROW,
        DELIVERY_REFUND,
    ]
