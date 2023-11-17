import time
import database

ALLOWED_CHARACTERS = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJK"
                      "LMNOPQRSTUVWXYZ1234567890!@#$%^&"
                      "*()_+-=[]{}|;':\",./<>?`~ \n")

class Game:
    def __init__(self):
        self.start_time = None
        self.untyped_text: str | None = None
        self.typed_text: str | None = None
        self.miss_clicks = 0
        self.allowed_characters = ALLOWED_CHARACTERS

    def start_game(self):
        self.untyped_text = database.get_random_text()
        self.typed_text = ""
        self.start_time = time.time()

    def typed_letter_correct(self, character: str) -> bool:
        assert self.untyped_text is not None
        self.typed_text += self.untyped_text[0]
        self.untyped_text = self.untyped_text[1:]
        print("checking correctness of" + character + self.typed_text[-1])
        if character == self.typed_text[-1]:
            return True
        self.miss_click()
        return False

    def end_game(self):
        self.start_time = None
        self.untyped_text = None
        self.typed_text = None
        self.miss_clicks = 0

    def get_time(self) -> float:
        assert self.start_time is not None
        return time.time() - self.start_time

    def get_wpm(self) -> float:
        assert self.typed_text is not None
        return len(self.typed_text) / 5 / self.get_time() * 60

    def game_started(self) -> bool:
        return self.start_time is not None

    def get_accuracy(self) -> float:
        assert self.typed_text is not None
        return 100 - (self.miss_clicks / len(self.typed_text) * 100)

    def get_typed_text(self) -> str:
        assert self.typed_text is not None
        return self.typed_text

    def get_untyped_text(self) -> str:
        assert self.untyped_text is not None
        return self.untyped_text

    def get_miss_clicks(self) -> int:
        return self.miss_clicks

    def miss_click(self) -> None:
        self.miss_clicks += 1

    def is_allowed_character(self, character: str):
        return character in self.allowed_characters


