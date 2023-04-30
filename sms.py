def send_sms(phonenumber: int, sms):
    import requests

    url = 'https://mysms.celcomafrica.com/api/services/sendsms/'

    data = {'partnerID': '435',
            'apikey': '6d999665d4abb2e3293714d06b403ff4',
            'mobile': phonenumber,
            'message': sms,
            'shortcode': 'OSL',
            'pass_type': 'plain'}

    response = requests.post(url=url, json=data)
    return response


# test = send_sms(+254714294113, "i am sick")