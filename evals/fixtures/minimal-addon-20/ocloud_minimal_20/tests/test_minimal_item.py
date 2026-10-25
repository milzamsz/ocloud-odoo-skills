from psycopg2 import IntegrityError

from odoo.exceptions import AccessError, ValidationError
from odoo.tests import TransactionCase
from odoo.tests.common import new_test_user


class TestMinimalItem(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = new_test_user(cls.env, login="ocloud_minimal_user", groups="base.group_user")
        cls.Item = cls.env["ocloud.minimal.item"].with_user(cls.user)

    def test_internal_user_can_create_item(self):
        item = self.Item.create({"name": "Fixture item", "quantity": 2})

        self.assertEqual(item.quantity, 2)

    def test_quantity_constraint_is_enforced(self):
        # Proves the models.Constraint object was created on the table.
        with self.assertRaises((IntegrityError, ValidationError)), self.cr.savepoint():
            self.Item.create({"name": "Invalid item", "quantity": -1})

    def test_internal_user_cannot_delete_item(self):
        item = self.Item.create({"name": "Retained item"})

        with self.assertRaises(AccessError):
            item.unlink()
