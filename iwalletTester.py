__author__ = 'joseph kodjo-kuma Djomeda'

from Integrator import Integrator
import uuid
import webbrowser

wsdl = "https://i-walletlive.com/paylive/paymentservice.asmx?wsdl"

apiVersion = "1.4"
merchantEmail = "your@merchant.email"
merchantKey = "yourmerchantkey"
serviceType = "C2B"
integrationMode =1
namespace = "http://www.i-walletlive.com/payLIVE"
redirectUrl = "https://i-walletlive.com/payLIVE/detailsnew.aspx?pay_token="



order_id= uuid.uuid1()
comment1=" "
comment2=""


chromecast_unit_price = 150
chromecast_quantity = 2
chromecast_subtotal = chromecast_unit_price*chromecast_quantity

organza_unit_price = 50
organza_quantity = 2
organza_subtotal = organza_unit_price* organza_quantity


client = Integrator(namespace, wsdl, apiVersion, merchantEmail, merchantKey, serviceType, integrationMode)

chromecast = client.buildOrderItem("001", "chromecast", chromecast_unit_price, chromecast_quantity, chromecast_subtotal)
organza = client.buildOrderItem("002", "organza", organza_unit_price, organza_quantity,organza_subtotal)

order_items = client.buildAPIObject('ArrayOfOrderItem')

order_items.OrderItem.append(chromecast)
order_items.OrderItem.append(organza)

# print order_items
#
sub_total=chromecast_subtotal+ organza_subtotal
shipping_cost=30
tax_amount=0
total= sub_total + shipping_cost+ tax_amount

result = client.mobilePaymentOrder(order_id,sub_total,shipping_cost,tax_amount,total,comment1,comment2,order_items)
# print result
paymentToken = result.token
# print paymentToken
redirectUrl = redirectUrl+paymentToken
print redirectUrl
webbrowser.open(redirectUrl)

