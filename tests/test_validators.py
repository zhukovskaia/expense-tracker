"""Тесты проверки пользовательского ввода."""

import unittest
from datetime import datetime
from unittest.mock import patch

import validators


def run_with_input(func, answers):
    """Вызывает func, подставляя ответы пользователя по очереди."""
    with patch("builtins.input", side_effect=answers), patch("builtins.print"):
        return func()


class TestReadAmount(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(run_with_input(validators.read_amount, ["350"]), 350.0)

    def test_comma_as_separator(self):
        self.assertEqual(run_with_input(validators.read_amount, ["99,90"]), 99.9)

    def test_retries_on_invalid_input(self):
        answers = ["abc", "", "-5", "0", "inf", "nan", "100"]
        self.assertEqual(run_with_input(validators.read_amount, answers), 100.0)


class TestReadDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(run_with_input(validators.read_date, ["2026-10-16"]), "2026-10-16")

    def test_empty_means_today(self):
        today = datetime.now().strftime(validators.DATE_FORMAT)
        self.assertEqual(run_with_input(validators.read_date, [""]), today)

    def test_retries_on_invalid_date(self):
        answers = ["16.10.2026", "2026-13-01", "2026-02-30", "2026-10-16"]
        self.assertEqual(run_with_input(validators.read_date, answers), "2026-10-16")


class TestReadCategory(unittest.TestCase):
    def test_lowercase_and_strip(self):
        self.assertEqual(run_with_input(validators.read_category, ["  Еда "]), "еда")

    def test_retries_on_empty(self):
        self.assertEqual(run_with_input(validators.read_category, ["", "   ", "кино"]), "кино")


if __name__ == "__main__":
    unittest.main()
