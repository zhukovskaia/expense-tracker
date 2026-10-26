"""Тесты добавления и просмотра расходов."""

import unittest
from unittest.mock import patch

with patch("storage.load_expenses", return_value=[]):
    import expences


class TestExpences(unittest.TestCase):
    def setUp(self):
        expences._expenses.clear()
        self.save_patcher = patch("storage.save_expenses")
        self.save_mock = self.save_patcher.start()
        self.print_patcher = patch("builtins.print")
        self.print_mock = self.print_patcher.start()

    def tearDown(self):
        self.save_patcher.stop()
        self.print_patcher.stop()

    def test_add_expense(self):
        expences.add_expense("еда", 350.0, "2026-10-16", "обед")
        self.assertEqual(expences.get_expenses(), [
            {"date": "2026-10-16", "category": "еда", "amount": 350.0, "comment": "обед"},
        ])

    def test_add_expense_saves_to_file(self):
        expences.add_expense("еда", 100.0, "2026-10-16")
        self.save_mock.assert_called_once_with(expences.get_expenses())

    def test_comment_is_optional(self):
        expences.add_expense("кино", 500.0, "2026-10-16")
        self.assertEqual(expences.get_expenses()[0]["comment"], "")

    def test_show_empty_list(self):
        expences.show_expenses()
        self.print_mock.assert_called_once_with("Список расходов пуст.")

    def test_show_expenses(self):
        expences.add_expense("еда", 350.0, "2026-10-16", "обед")
        self.print_mock.reset_mock()
        expences.show_expenses()
        printed = " ".join(str(c.args[0]) for c in self.print_mock.call_args_list)
        self.assertIn("2026-10-16 | еда — 350.0 руб. (обед)", printed)

    def test_delete_expense(self):
        expences.add_expense("еда", 100.0, "2026-10-16")
        expences.add_expense("кино", 500.0, "2026-10-17")
        self.save_mock.reset_mock()
        expences.delete_expense(1)
        self.assertEqual([e["category"] for e in expences.get_expenses()], ["кино"])
        self.save_mock.assert_called_once()

    def test_delete_wrong_index(self):
        expences.add_expense("еда", 100.0, "2026-10-16")
        self.save_mock.reset_mock()
        for index in (0, -1, 2):
            expences.delete_expense(index)
        self.assertEqual(len(expences.get_expenses()), 1)
        self.save_mock.assert_not_called()

    def test_filter_expenses(self):
        expences.add_expense("еда", 100.0, "2026-10-16", "обед")
        expences.add_expense("кино", 500.0, "2026-10-17")
        self.print_mock.reset_mock()
        expences.filter_expenses("  ЕДА ")
        printed = " ".join(str(c.args[0]) for c in self.print_mock.call_args_list)
        self.assertIn("2026-10-16 | еда — 100.0 руб. (обед)", printed)
        self.assertNotIn("кино", printed)

    def test_filter_not_found(self):
        expences.add_expense("еда", 100.0, "2026-10-16")
        self.print_mock.reset_mock()
        expences.filter_expenses("кино")
        self.print_mock.assert_called_once_with("Расходов в категории 'кино' не найдено.")


if __name__ == "__main__":
    unittest.main()
