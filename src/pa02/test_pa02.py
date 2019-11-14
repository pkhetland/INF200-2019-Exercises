# -*- coding: utf-8 -*-

"""
Set of compatibility tests for PA02.
"""

__author__ = ''
__email__ = 'h'


from . import chutes_simulation as cs
import pytest


class TestBoard:
    """

    """
    def test_position_adjustment(self):
        """Test position adjustment method by calling the default value
        returned by ladder (8, 10)
        """
        b = cs.Board()
        assert b.position_adjustment(8) == 10

    def test_goal_reached(self):
        """Test goal_reached method by creating default instance of Board
        """
        b = cs.Board()
        assert b.goal_reached(91) is True


class TestPlayer:
    """

    """
    def test_move(self):
        b = cs.Board()
        p = cs.Player(b)
        assert p.position == 0
        p.move()
        assert p.position != 0
