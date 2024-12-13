import unittest

class TestBankAccount(unittest.TestCase):
    def test_create_account_with_valid_balance(self):
        """Тест создания счёта с нормальным начальным балансом."""
        account = BankAccount("55555", 300.0)
        self.assertEqual(account.getBalance(), 300.0)

    def test_create_account_with_invalid_balance(self):
        """Тест создания счёта с неправильным начальным балансом."""
        with self.assertRaises(ValueError):
            BankAccount("55555", -300.0)

    def test_deposit_valid_amount(self):
        """Тест успешного пополнения счёта."""
        account = BankAccount("55555", 300.0)
        account.deposit(50.0)
        self.assertEqual(account.getBalance(), 350.0)

    def test_deposit_invalid_amount(self):
        """Тест пополнения счёта с неправильной суммой."""
        account = BankAccount("55555", 100.0)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid_amount(self):
        """Тест успешного снятия средств."""
        account = BankAccount("55555", 200.0)
        account.withdraw(50.0)
        self.assertEqual(account.getBalance(), 150.0)

    def test_withdraw_insufficient_funds(self):
        """Тест снятия средств, превышающих баланс."""
        account = BankAccount("55555", 100.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(200.0)
        self.assertEqual(str(context.exception), "Нет денег")

    def test_withdraw_invalid_amount(self):
        """Тест снятия некорректной суммы."""
        account = BankAccount("55555", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)

    def test_balance_after_operations(self):
        """Тест проверки баланса после операций."""
        account = BankAccount("55555", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.getBalance(), 120.0)

    def test_create_account_with_default_balance(self):
        """Тест создания счёта с балансом по умолчанию."""
        account = BankAccount("55555")
        self.assertEqual(account.getBalance(), 0.0)

if name == "__main__":
    unittest.main()
