import unittest
from decimal import Decimal
from app import checkout_total,delete_account

class CheckoutTests(unittest.TestCase):
    def test_no_discount(self):self.assertEqual(checkout_total(200),Decimal("200.00"))
    def test_percentage_discount(self):self.assertEqual(checkout_total(200,10),Decimal("180.00"))
    def test_small_subtotal(self):self.assertEqual(checkout_total(50,20),Decimal("40.00"))
    def test_full_discount(self):self.assertEqual(checkout_total(75,100),Decimal("0.00"))
    def test_decimal_rounding(self):self.assertEqual(checkout_total("19.99",15),Decimal("16.99"))
    def test_negative_subtotal(self):
        with self.assertRaises(ValueError):checkout_total(-1)
    def test_negative_discount(self):
        with self.assertRaises(ValueError):checkout_total(10,-1)
    def test_excess_discount(self):
        with self.assertRaises(ValueError):checkout_total(10,101)

class AuthorizationTests(unittest.TestCase):
    def setUp(self):self.accounts={"demo-1":{"name":"Synthetic account"}}
    def test_non_admin_cannot_delete(self):
        with self.assertRaises(PermissionError):delete_account({"role":"viewer"},"demo-1",self.accounts)
        self.assertIn("demo-1",self.accounts)
    def test_missing_role_cannot_delete(self):
        with self.assertRaises(PermissionError):delete_account({},"demo-1",self.accounts)
        self.assertIn("demo-1",self.accounts)
    def test_admin_can_delete(self):
        result=delete_account({"role":"admin"},"demo-1",self.accounts)
        self.assertEqual(result["deleted"],"demo-1");self.assertNotIn("demo-1",self.accounts)
    def test_missing_target_is_explicit(self):
        with self.assertRaises(KeyError):delete_account({"role":"admin"},"missing",self.accounts)

if __name__=="__main__":unittest.main()
