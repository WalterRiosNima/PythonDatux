import IngresaDatos as ID
import funcionesBitcoin as fB


url="https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    data=fB.get_url_data(url)
    bitcoin_bpi=data["bpi"]
    bitcoin_usd=bitcoin_bpi["USD"]
    bitcoin_priceusd =bitcoin_usd["rate"]
    bitcoin_priceusd=fB.get_str_to_number(bitcoin_priceusd)
    print("El precio actual del bitcoin es: {:.4f} USD" .format(bitcoin_priceusd))
    n=ID.get_float("Ingrese el número de Bitcoins que posee: ")
    convert=fB.conv_Bitcoin_to_USD(n, bitcoin_priceusd)
    print("\nActualmente, usted posee {0:.4f} USD en Bitcoins".format(convert))


if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)