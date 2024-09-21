import unittest

import dnd
from dice import make_test_dice


class TestLogic(unittest.TestCase):
    def test_problem1(self):
        params = [
            (2, make_test_dice(4, 6, 1), 10),
            (3, make_test_dice(4, 6, 1), 1),
            (3, make_test_dice(1, 2, 3), 1),
        ]

        for level, dice, expected in params:
            with self.subTest(level=level, dice=dice, expected=expected):
                self.assertEqual(dnd.magic_missile(level, dice), expected)

    def test_problem2(self):
        params = [
            ([21, 46], 12),
            ([2, 5], 15),
            ([9, 5], 15),
            ([1589, 338], 1),
        ]

        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(dnd.heavy_tome(*inp), expected)

    def test_problem3(self):
        params = [
            ([2, 21, 46, make_test_dice(4, 6, 1)], 10),
            ([0, 100, 5], 15),
            ([0, 6, 10], 1),
            ([0, 82, 115], 9),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(dnd.take_turn(*inp), expected)

    def test_problem4_num_factors(self):
        params = [
            (2, 2),
            (5, 2),
            (50, 6),
            (62, 4),
            (423593, 4),
        ]

        for n, expected in params:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(dnd.num_factors(n), expected)

    def test_problem4_i_love_math(self):
        params = [
            (1, 1),
            (4, 3),
            (5, 5),
            (49, 47),
            (62, 61),
            (423584, 423584),
        ]
        for opponent_hp, expected in params:
            with self.subTest(opponent_hp=opponent_hp, expected=expected):
                self.assertEqual(dnd.i_love_math(opponent_hp), expected)

    def test_problem4_math_update(self):
        params = [
            ([2, 21, 46, make_test_dice(4, 6, 1)], 36),
            ([2, 21, 46, make_test_dice(6)], 31),
            ([0, 21, 46], 31),
            ([0, 100, 5], -10),
            ([0, 82, 115], 103),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(dnd.math_update(*inp), expected)

    def test_problem5_simple_strategies(self):
        from dnd import always_cast_5, catch_up, fight, math_update, simple_update

        dice_1 = make_test_dice(1)
        dice_4 = make_test_dice(4)
        dice_6 = make_test_dice(6)
        dice_7 = make_test_dice(7)
        params = [
            ([always_cast_5, always_cast_5, simple_update], {"dice": dice_4}, (20, 0)),
            ([always_cast_5, always_cast_5, simple_update], {"dice": dice_7}, (30, -5)),
            ([always_cast_5, always_cast_5, math_update], {"dice": dice_1}, (1, 0)),
            ([always_cast_5, catch_up, simple_update], {"dice": dice_6}, (-8, 10)),
            ([catch_up, catch_up, math_update], {"dice": dice_6}, (28, -5)),
            # custom hps
            (
                [always_cast_5, always_cast_5, simple_update],
                {"dice": dice_1, "hp0": 12, "hp1": 13},
                (0, 1),
            ),
        ]
        for args, kwargs, expected in params:
            with self.subTest(args=args, kwargs=kwargs, expected=expected):
                self.assertEqual(fight(*args, **kwargs), expected)

    def test_problem6_always_cast(self):
        strategy = dnd.always_cast(8)
        params = [
            ((7, 7), 8),
            ((50, 50), 8),
            ((131, 131), 8),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(strategy(*inp), expected)

    def test_problem7_is_always_cast(self):
        params = [
            (dnd.always_cast_5, True),
            (dnd.always_cast(9), True),
            (dnd.catch_up, False),
        ]
        for strategy, expected in params:
            with self.subTest(strategy=strategy, expected=expected):
                self.assertEqual(dnd.is_always_cast(strategy), expected)

    def test_problem8_make_averaged(self):
        averaged_missile = dnd.make_averaged(dnd.magic_missile, samples_count=8)
        params = [
            ([1, make_test_dice(1)], 1),
            ([2, make_test_dice(4, 1)], 1),
            ([3, make_test_dice(2, 2, 6)], 10),
            ([4, make_test_dice(6, 1, 5, 4)], 1),
            ([5, make_test_dice(3, 5, 6, 4, 1)], 1),
            ([3, make_test_dice(3, 2, 4)], 9),
            ([5, make_test_dice(6, 5, 5, 4, 2)], 22),
            ([6, make_test_dice(2, 3, 4, 6, 5, 1)], 1),
            ([4, make_test_dice(6, 4, 5, 2)], 17),
            ([7, make_test_dice(3, 6, 2, 4, 1, 5, 6)], 1),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertAlmostEqual(averaged_missile(*inp), expected)

    def test_problem9_max_scoring_spell_level(self):
        params_1000 = [
            ([1, 1, 1, 1], 1),
            ([6, 6, 6], 10),
            ([2, 2, 2, 2, 2, 1], 3),
            ([4, 4, 1, 4], 2),
            ([3, 3, 3], 10),
            ([5, 5, 1], 2),
            ([1] * 200 + [6] * 200, 10),
            ([2, 3, 4, 5, 6], 10),
            ([6, 5, 4, 3, 2, 1], 3),
        ]
        for dice_vals, expected in params_1000:
            with self.subTest(
                dice_vals=dice_vals, times_called=1000, expected=expected
            ):
                dice = make_test_dice(*dice_vals)
                self.assertEqual(dnd.max_scoring_spell_level(dice, 1000), expected)

        params_1 = (
            ([1, 1, 1], 1),
            ([6], 10),
            ([5, 5, 4, 3, 2, 1], 4),
            ([2, 2, 2, 1], 2),
            ([2, 3, 6, 6], 10),
        )
        for dice_vals, expected in params_1:
            with self.subTest(dice_vals=dice_vals, times_called=1, expected=expected):
                dice = make_test_dice(*dice_vals)
                self.assertEqual(dnd.max_scoring_spell_level(dice, 1), expected)

    def test_problem10_tome_strategy(self):
        params = [
            ((25, 65, 10, 5), 5),
            ((8, 30, 15, 4), 4),
            ((50, 20, 9, 7), 0),
            ((12, 40, 20, 6), 6),
            ((14, 47, 12, 9), 0),
            ((33, 12, 18, 6), 6),
            ((100, 20, 10, 7), 7),
            ((21, 99, 8, 5), 0),
            ((5, 2, 7, 3), 3),
            ((45, 60, 11, 4), 0),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(dnd.tome_strategy(*inp), expected)

    def test_problem11_math_strategy(self):
        params = [
            ((30, 50, 20, 5), 5),
            ((25, 40, 18, 7), 7),
            ((15, 45, 14, 9), 0),
            ((10, 25, 10, 4), 0),
            ((5, 3, 12, 6), 6),
            ((22, 18, 19, 8), 8),
            ((50, 70, 16, 6), 0),
            ((40, 20, 15, 9), 9),
            ((100, 90, 11, 10), 10),
            ((8, 2, 13, 5), 5),
        ]
        for inp, expected in params:
            with self.subTest(inp=inp, expected=expected):
                self.assertEqual(dnd.math_strategy(*inp), expected)
