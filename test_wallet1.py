import pytest
from wallet import Wallet

@pytest.fixture
def empty_wallet():
    # Returns wallet balance to zero
    return Wallet()

@pytest.fixture
def wallet():
    #Returns wallet balance to 20
    return Wallet(20)

def test_default_intial_amount(empty_wallet):
    assert wallet.balance == 0

def test_default_intial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_deposit(wallet):
    wallet.deposit(80)
    assert wallet.balance == 100

def test_wallet_withdraw(wallet):
    wallet.withdraw(10)
    assert wallet.balance == 10





