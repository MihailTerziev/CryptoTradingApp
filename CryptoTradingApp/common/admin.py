from django.contrib import admin
from CryptoTradingApp.common.models import *


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("date_of_purchase", "currency", "buyer", "payment_method", "quantity")


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("traded_currency_one", "traded_currency_two", "traded_quantity", "date_of_trade", "trader", "trader_wallet")


@admin.register(BalanceIncrease)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("amount", "user", "date_of_transaction", "transaction_method")
