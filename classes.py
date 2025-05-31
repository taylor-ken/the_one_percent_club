from dataclasses import dataclass, field
from typing import List

@dataclass
class Contestant:
    """Class for keeping track of contestants. 
    They start the game with £1,000.
    A pass is earned upon reaching the fifth question (50%).
    Answer holds the contestants answer to the current question."""
    name: str
    money: int = 1000
    has_pass: bool = False
    is_eliminated: bool = False
    answer: str = ''

@dataclass
class Question:
    difficulty: int
    question: str
    is_multiple_choice: bool
    option_A: str
    option_B: str
    option_C: str
    option_D: str
    answer: str
    explanation: str    

@dataclass
class Game:
    name: str = 'The 1% Club'
    host: str = 'Lee Mack'
    prize_pot: int = 0
    playing_count: int = 0
    current_round: int = 0
    questions: list = field(default_factory=list)
    contestants: list = field(default_factory=list)
