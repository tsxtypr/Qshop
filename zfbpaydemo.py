from alipay import  AliPay

# 公钥
alipay_public_key_string="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA9O64pwEwQQf6wut37u3YjkDsnpTc9SNXRIv1nBP6jWgdd2y5Fr3cY9+qpe2jhSdag1juYsOgjhkQZjTHD5kdrAk2ZoZWPY14YukTLi1HmvduwOOpXCc1ZRgFOnPjHH8PP5t9lDxZar1/9n7R1Z71mjzEyU02FraQg5uKRaCaRLeq01ksoOJOCe5jOlvGBILWnNCuv16EOyCqWbspr2Tg/beBFP1Tzopo/XZg7yNBCl9iMmUwFTqeoY0/7/sxCkO1TMp036tXr6uDFyqi/nWw05uHvkI1RXSV+mYfmrjQ+EPLcsmPY/dj0TcXi1IDAHIKr6yE6r/ZdPhjEZqEcDXZnQIDAQAB
-----END PUBLIC KEY-----"""


# 私钥
alipay_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA9O64pwEwQQf6wut37u3YjkDsnpTc9SNXRIv1nBP6jWgdd2y5Fr3cY9+qpe2jhSdag1juYsOgjhkQZjTHD5kdrAk2ZoZWPY14YukTLi1HmvduwOOpXCc1ZRgFOnPjHH8PP5t9lDxZar1/9n7R1Z71mjzEyU02FraQg5uKRaCaRLeq01ksoOJOCe5jOlvGBILWnNCuv16EOyCqWbspr2Tg/beBFP1Tzopo/XZg7yNBCl9iMmUwFTqeoY0/7/sxCkO1TMp036tXr6uDFyqi/nWw05uHvkI1RXSV+mYfmrjQ+EPLcsmPY/dj0TcXi1IDAHIKr6yE6r/ZdPhjEZqEcDXZnQIDAQABAoIBAQCzYy/saMttpal8HzdMz/heX6CtmLun8sVUl+k/8cX80Tdbo06AIHgM0eDK/BxaRnNdZcHapgquaB8BrD/q5aq8uFaWimcZV8bHMotws4sRLY15SoRc0P6jVw9lO0EoOsrxPDGiYvzeV4IkB8gpW+3nlABQqvMleXqoWT/RNQonrqpnqmOp4as41iL9c/7J7znzxBeBZkDGEwrCx/85muXHjkDI/sjCYfkVx1uyQ9LBaBtpoTxnDUXQRdhI+RmpCilqgQi0Rbt9b3np9KmlfNVldK8sd0LRygki3g1zNnMK+IaNSMgBLlvbIgzuvtw6sNpM/RUjUQx80tHrYDhJu/tBAoGBAPytxYsWXg55UVW6LSgb2SrwZaQ0+qilFv8wnrS338wwTt6tM8scCwDQkvdfR5D7THhvsUBrJ0O5p8l6FFXSrRmo3966YNpNNBoHp20pfscirXo1tlSc7QHdfAWzReIgRvyh+VQAaE0yDbL7H6c1Rv7MKDhW0EN+2WyYMNiejEoRAoGBAPgm4mzyUHcgQzeVclWTuOXvpAA71yOk/mUCv72CWUftJducUZHzLCY9QnfBmbUj8yBze1UJHS4WBDZf9pjmfSjghJPztX2Y2gzzH/e5HxGojlMpI7FKrt7Vw+rYf/YS2CoRDDHBxFe1XYWFC6t+YdIqbEK4M8p5pbrJYbcoe+rNAoGARVVtcjfmATS647odb/cMRSMH0OIUsbfzMnzl35Lg3weWbLW8E4yTXFrfKO/FFHxQRG/phFKiyIumBbvw3ofbpcHYBCbCMsSiek4FXAfZ2MykK3eXm2ogArYCtRG3KFBRCjtrzef6tsv4RFdyHRCadYoRszvnE8433Pt508bVmfECgYEAyAmgcS6MitspFD+WoUGpxUF+tOmILiWtJQQoSL4w9nhHEldasgqSxmiPkjYwkALg1IIDI7NrIGGDF8oX4X272x3SAeptnUeATvwWAv3p+7QitwrsyNhpSxyLCF9qF5VtR8viRqHqgsGjGCT+GUqR1Hd6OfZ/WXLilEYOTTWHXukCgYEAtbaoOez4Y4SRifDkOgVy7J61JSSaQ6lCOLcUgDrUxUY7DCjCc6hPFb7v6rpwcDUIRL1TWC84lqipjgkUbVvfyVedzAEhY3J99VwDyt4pxirGhvI0oZ6bNmYU5wbQ4d+sFlmzb06OiQ8c9pe6y/VJNgvykBySddZ/UnlL6s5l3WM=
-----END RSA PRIVATE KEY-----"""

# 实例化支付对象
alipay=AliPay(
    appid='2016101300673931',
    app_notify_url=None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
)

#实例化订单
order_string=alipay.api_alipay_trade_page_pay(
    # 交易主体
    subject='牛羊生鲜',
    out_trade_no='10000000001',
    total_amount='100',
    # 请求支付，之后及时回调的一个接口
    return_url=None,
    # 通知地址
    notify_url=None,
)


# 发送支付请求

#请求地址    支付网关+实例化订单
result="https://openapi.alipaydev.com/gateway.do?"+order_string
print(result)