# -*- coding: utf-8 -*-

"""
Set of compatibility tests for PA02.
"""

__author__ = 'Petter K. Hetland, Bishnu Poudel'
__email__ = ', bishnu.poudel@nmbu.no'

from . import chutes_simulation as cs
import pytest


class TestBoard:
    """

    """

    def test_position_adjustment(self):
        """Test position adjustment method by calling the value
        returned by ladder (8, 10)
        """
        b = cs.Board()
        assert b.position_adjustment(8) == 2

    def test_goal_reached(self):
        """Test goal_reached method by creating default instance of Board
        """
        b = cs.Board()
        assert b.goal_reached(91) is True

    def test_constructor_named_args(self):
        """Test ladders and chutes are initialized."""
        b = cs.Board(ladders=[(1, 4), (5, 16)], chutes=[(9, 2), (12, 3)],
                     goal=90)
        assert b.ladders == [(1, 4), (5, 16)] and \
               b.chutes == [(9, 2), (12, 3)]


class TestPlayer:
    """

    """

    def test_move(self):
        b = cs.Board()
        p = cs.Player(b)
        assert p.position == 0
        p.move()
        assert p.position != 0
        assert p.position == p.position +b.position_adjustment(p.position) or \
               p.position == p.position - b.position_adjustment(p.position)
