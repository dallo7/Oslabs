def send_sms(phonenumber: int, sms):
    import requests

    url = 'https://mysms.celcomafrica.com/api/services/sendsms/'

    data = {'partnerID': '435',
            'apikey': '1c37d5b44c805abf79800477e8af91d9',
            'mobile': phonenumber,
            'message': sms,
            'shortcode': 'OSL',
            'pass_type': 'plain'}

    response = requests.post(url=url, json=data)
    return response


# test = send_sms(+254714294113, "i am sick")
