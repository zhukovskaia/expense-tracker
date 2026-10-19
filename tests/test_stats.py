"""Тесты подсчёта суммы и статистики по категориям."""

import unittest

import stats


class TestTotalAmount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(stats.total_amount([]), 0)

    def test_sum_of_amounts(self):
        expenses = [{"amount": 100}, {"amount": 50.5}, {"amount": 0.5}]
        self.assertAlmostEqual(stats.total_amount(expenses), 151.0)

    def test_amount_as_string(self):
        self.assertAlmostEqual(stats.total_amount([{"amount": "200"}]), 200.0)

    def test_skips_invalid_amounts(self):
        expenses = [{"amount": 100}, {"amount": "abc"}, {"amount": None}, {}]
        self.assertAlmostEqual(stats.total_amount(expenses), 100.0)


class TestStatsByCategory(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(stats.stats_by_category([]), {})

    def test_groups_by_category(self):
        expenses = [
            {"category": "еда", "amount": 100},
            {"category": "транспорт", "amount": 60},
            {"category": "еда", "amount": 50},
        ]
        self.assertEqual(stats.stats_by_category(expenses), {"еда": 150.0, "транспорт": 60.0})

    def test_ignores_case_and_spaces(self):
        expenses = [
            {"category": "Еда", "amount": 100},
            {"category": "  ЕДА ", "amount": 50},
        ]
        self.assertEqual(stats.stats_by_category(expenses), {"еда": 150.0})

    def test_sorted_by_amount_desc(self):
        expenses = [
            {"category": "кино", "amount": 10},
            {"category": "еда", "amount": 300},
            {"category": "транспорт", "amount": 60},
        ]
        self.assertEqual(list(stats.stats_by_category(expenses)), ["еда", "транспорт", "кино"])

    def test_empty_category(self):
        result = stats.stats_by_category([{"category": "", "amount": 10}])
        self.assertEqual(result, {"без категории": 10.0})

    def test_skips_invalid_amounts(self):
        expenses = [
            {"category": "еда", "amount": 100},
            {"category": "еда", "amount": "abc"},
        ]
        self.assertEqual(stats.stats_by_category(expenses), {"еда": 100.0})


if __name__ == "__main__":
    unittest.main()
