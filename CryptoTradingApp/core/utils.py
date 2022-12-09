from CryptoTradingApp.crypto.models import *


def get_crypto_by_slug(crypto_slug):
    return CryptoCurrency.objects.get(slug=crypto_slug)


def get_all_crypto():
    all_crypto_list = []

    for crypto in CryptoCurrency.objects.all():
        all_crypto_list.append((f"crypto_{crypto.name}", crypto.name))

    return all_crypto_list


def get_user_crypto(user_pk):
    user_crypto_list = []
    wallet = CryptoWallet.objects.filter(pk=user_pk).get()

    for crypto in wallet.crypto_inventory.all():
        user_crypto_list.append((f"crypto_{crypto.name}", crypto.name))

    return user_crypto_list
