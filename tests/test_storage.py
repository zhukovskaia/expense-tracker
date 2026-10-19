"""Тесты сохранения и загрузки расходов."""

import os
import tempfile
import unittest
from unittest.mock import patch

import storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.file_name = os.path.join(self.tmp_dir.name, "expenses.json")
        self.patcher = patch.object(storage, "FILE_NAME", self.file_name)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.tmp_dir.cleanup()

    def test_load_without_file(self):
        self.assertEqual(storage.load_expenses(), [])

    def test_save_and_load(self):
        expenses = [
            {"date": "2026-10-16", "category": "еда", "amount": 350.0, "comment": "обед"},
            {"date": "2026-10-17", "category": "транспорт", "amount": 60.0, "comment": ""},
        ]
        storage.save_expenses(expenses)
        self.assertEqual(storage.load_expenses(), expenses)

    def test_cyrillic_saved_as_is(self):
        storage.save_expenses([{"category": "еда"}])
        with open(self.file_name, encoding="utf-8") as f:
            self.assertIn("еда", f.read())


if __name__ == "__main__":
    unittest.main()
