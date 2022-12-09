from django import forms
from CryptoTradingApp.common.models import *


class IncreaseBalanceForm(forms.Form):
    amount = forms.CharField(widget=forms.NumberInput)
    transaction_method = forms.ChoiceField(choices=PaymentMethod.choices())


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ("currency", "quantity", "payment_method")

        labels = {
            "currency": "Choose currency",
            "payment_method": "Choose payment method"
        }

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "placeholder": "Enter quantity"
                }
            )
        }


class TradeCreateForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ("traded_currency_one", "traded_currency_two", "traded_quantity")

        labels = {
            "traded_currency_one": "Convert",
            "traded_currency_two": "To",
            "traded_quantity": "Amount"
        }

        widgets = {
            "traded_quantity": forms.NumberInput(
                attrs={
                    "placeholder": "Enter amount"
                }
            )
        }
