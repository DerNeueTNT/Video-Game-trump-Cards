import random
from typing import Any
try:
    import os
    import sys
    supports_sys = True
except Exception:
    supports_sys = False
import string

def supports_ansi() -> bool:
    if not supports_sys:
        return False

    if not sys.stdout.isatty():
        return False

    if os.environ.get("NO_COLOR") is not None:
        return False

    if os.name != "nt":
        return True

    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32

        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()

        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)) == 0:
            return False

        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        if mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING:
            return True

        return kernel32.SetConsoleMode(
            handle,
            mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        ) != 0

    except Exception:
        return False
    else:
        return False

class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self) -> Any:
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def search_and_remove(self, item: Any) -> Any:
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self) -> str:
        return f"[{', '.join(self.items)}]"


class Character():
    def __init__(self, name: str = "", origin: str = "", power: int = 0, durability: int = 0, mobility: int = 0, stealth: int = 0, intelligence: int = 0, versatility: int = 0):
        self.name: str = name
        self.origin: str = origin
        self.power: int = power
        self.durability: int = durability
        self.mobility: int = mobility
        self.stealth: int = stealth
        self.intelligence: int = intelligence
        self.versatility: int = versatility
    def printer(self):
        print("name: " + self.name)
        print("origin: " + self.origin)
        if self.power in range(1, 11):
            print("power: " + str(self.power))
        else: 
            print("power: " + str(self.power) + "*")
        if self.durability in range(1, 11):
            print("durability: " + str(self.durability))
        else:
            print("durability: " + str(self.durability) + "*")
        if self.mobility in range(1, 11):
            print("mobility: " + str(self.mobility))
        else:
            print("mobility: " + str(self.mobility) + "*")
        if self.stealth in range(1, 11):
            print("stealth: " + str(self.stealth))
        else:
            print("stealth: " + str(self.stealth) + "*")
        if self.intelligence in range(1, 11):
            print("intelligence: " + str(self.intelligence))
        else:
            print("intelligence: " + str(self.intelligence) + "*")
        if self.versatility in range(1, 11):
            print("versatility: " + str(self.versatility))
        else:
            print("versatility: " + str(self.versatility) + "*")
    def compare(self, other, comp_str: str = ""):
        did_win: int = 0
        match comp_str:
            case "power" | "pow":
                if self.power > other.power:
                    did_win = 1
                elif self.power == other.power:
                    did_win = 2
                return did_win, other.power, "power", other.name
            case "durability" | "dur":
                if self.durability > other.durability:
                    did_win = 1
                elif self.durability == other.durability:
                    did_win = 2
                return did_win, other.durability, "durability", other.name
            case "mobility" | "mob":
                if self.mobility > other.mobility:
                    did_win = 1
                elif self.mobility == other.mobility:
                    did_win = 2
                return did_win, other.mobility, "mobility", other.name
            case "stealth" | "ste":
                if self.stealth > other.stealth:
                    did_win = 1
                elif self.stealth == other.stealth:
                    did_win = 2
                return did_win, other.stealth, "stealth", other.name
            case "intelligence" | "int":
                if self.intelligence > other.intelligence:
                    did_win = 1
                elif self.intelligence == other.intelligence:
                    did_win = 2
                return did_win, other.intelligence, "intelligence", other.name
            case "versatility" | "ver":
                if self.versatility > other.versatility:
                    did_win = 1
                elif self.versatility == other.versatility:
                    did_win = 2
                return did_win, other.versatility, "versatility", other.name
            case _:
                return None, None, None, None

def main():
    ANSI: bool = supports_ansi()
    print("ANSI:", ANSI)
    draw_pile = Queue()
    op_draw_pile = Queue()
    char_dict: dict[str, Character] = {
        "defect": Character("The Defect", "slay the spire", 6, 5, 4, 2, 4, 6),
        "silent": Character("The Silent", "slay the spire", 5, 3, 5, 6, 4, 5),
        "necrobinder": Character("The Necrobinder", "slay the spire 2", 6, 4, 4, 3, 3, 4),
        "regent": Character("The Regent", "slay the spire 2", 7, 5, 2, 2, 3, 3),
        "ironclad": Character("The Ironclad", "slay the spire", 6, 6, 3, 2, 3, 3),
        "agent 47": Character("Agent 47", "Hitman: codename 47", 5, 5, 5, 10, 6, 7),
        "frisk": Character("Frisk", "Undertale", 10, 5, 3, 2, 3, 4),
        "shovel knight": Character("Shovel Knight", "Shovel Knight", 5, 5, 5, 2, 3, 6),
        "v1": Character("V1", "ULTRAKILL", 8, 4, 9, 2, 5, 7),
        "scout": Character("Scout", "Team Fortress 2", 4, 3, 6, 3, 2, 4),
        "soldier": Character("Soldier", "Team Fortress 2", 6, 4, 5, 2, 1, 4),
        "pyro": Character("Pyro", "Team Fortress 2", 5, 4, 4, 2, 0, 5),
        "demoman": Character("Demoman", "Team Fortress 2", 5, 4, 6, 2, 4, 5),
        "heavy": Character("Heavy", "Team Fortress 2", 6, 6, 2, 1, 5, 3),
        "engineer": Character("Engineer", "Team Fortress 2", 5, 3, 4, 2, 8, 6),
        "medic": Character("Medic", "Team Fortress 2", 4, 4, 4, 2, 7, 5),
        "sniper": Character("Sniper", "Team Fortress 2", 5, 3, 3, 5, 4, 3),
        "spy": Character("Spy", "Team Fortress 2", 4, 3, 4, 9, 5, 5),
        "driver": Character("The Driver", "Pacific Drive", 2, 5, 7, 3, 3, 8),
        "driller": Character("Driller", "Deep Rock Galactic", 6, 5, 5, 2, 3, 6),
        "engineer2": Character("Engineer", "Deep Rock Galactic", 6, 5, 6, 2, 4, 6),
        "gunner": Character("Gunner", "Deep Rock Galactic", 6, 6, 4, 2, 3, 5),
        "scout2": Character("Scout", "Deep Rock Galactic", 5, 5, 7, 2, 3, 6),
        "gordon freeman": Character("Gordon Freeman", "Half-Life", 6, 6, 5, 2, 6, 6),
        "chell": Character("Chell", "Portal", 2, 5, 8, 3, 5, 3),
        "sans": Character("Sans", "Undertale", 5, 0, 10, 3, 6, 5),
        "glados": Character("GLaDOS", "Portal", 7, 7, 1, 1, 9, 9),
        "wheatley": Character("Wheatley", "Portal 2", 3, 4, 2, 2, 1, 3),
        "lancer": Character("Lancer", "Deltarune", 3, 4, 4, 3, 2, 3),
        "baba": Character("Baba", "Baba Is You", 1, 1, 2, 2, 5, 8),
        "green shovel knight": Character("Green Shovel Knight", "Shovel Knight", 5, 5, 5, 2, 3, 6),
        "annoying dog": Character("Annoying Dog", "Undertale", 1, 1, 5, 3, 1, 11),
        "stanley": Character("Stanley", "The Stanley Parable", 2, 10, 3, 3, 2, 1),
        "flowey": Character("Flowey", "Undertale", 3, 2, 2, 4, 5, 3),
    }
    try:
        seed = input("Game code: ")

        if seed == "":
            seed = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=24))

            if ANSI:
                print(f"\033[F\033[KAuto-generated code: {seed}")
            else:
                print(f"Auto-generated code: {seed}")
        
        while True:
            player_opt = str(input("Are you player 1 or 2? "))
            if player_opt.lower() in ["1", "p1", "one", "player 1", "player one"]:
                player = 1
                break
            elif player_opt.lower() in ["2", "p2", "two", "player 2", "player two"]:
                player = 2
                break
            print("INVALID INPUT")

        cards = list(char_dict.values())

        rng = random.Random(seed)
        rng.shuffle(cards)

        player_1_cards = cards[::2]
        player_2_cards = cards[1::2]

        if player == 1:
            my_cards = player_1_cards
            op_cards = player_2_cards
        else:
            my_cards = player_2_cards
            op_cards = player_1_cards

        for card in my_cards:
            draw_pile.push(card)
        for card in op_cards:
            op_draw_pile.push(card)

        turn: int = 1
        while True:
            if draw_pile.size() > 0:
                p_top = draw_pile.peek()
            else:
                if ANSI:
                    print("\033[0;91mYOU LOSE!\033[0m")
                else:
                    print("YOU LOSE!")
                break

            if op_draw_pile.size() > 0:
                e_top = op_draw_pile.peek()
            else:
                if ANSI:
                    print("\033[0;92mYOU WIN!\033[0m")
                else:
                    print("YOU WIN!")
                break
                
            # the tool I was using at the time was refusing to let me use multi-line strings without complaining
            print(f"You have: {draw_pile.size()} cards | Opponent has: {op_draw_pile.size()} cards")
            if ANSI:
                if (player == 1 and turn == 1) or (player == 2 and turn == 2):
                    print(f"\033[0;39;46mYour opponent is holding {e_top.name} from {e_top.origin}\033[0m")
                else:
                    print("\033[0;39;41mopponent's turn\033[0m")
            else:
                if (player == 1 and turn == 1) or (player == 2 and turn == 2):
                    print(f"Your opponent is holding {e_top.name} from {e_top.origin}")
                else:
                    print("opponent's turn")
            print("")
            p_top.printer()
            print("")

            did_quit: bool = False
            while True:
                user_input: str = input("Input: ").strip().lower()
                if user_input in ["quit", "stop", "q", "end"]:
                    did_quit = True
                    break
                did_win, other_stat, what_stat, what_char = p_top.compare(e_top, user_input)
                if did_win == 1:
                    if ANSI:
                        print(f"\033[0;32mYou won\033[0m against {what_char}'s {other_stat} {what_stat}")
                    else:
                        print(f"You won against {what_char}'s {other_stat} {what_stat}")
                    draw_pile.push(op_draw_pile.pop())
                    draw_pile.push(draw_pile.pop())
                    break
                elif did_win == 0:
                    if ANSI:
                        print(f"\033[0;31mYou lost\033[0m to {what_char}'s {other_stat} {what_stat}")
                    else:
                        print(f"You lost to {what_char}'s {other_stat} {what_stat}")
                    op_draw_pile.push(draw_pile.pop())
                    op_draw_pile.push(op_draw_pile.pop())
                    break
                elif did_win == 2:
                    if ANSI:
                        print(f"\033[0;36mYou tied\033[0m with {what_char}")
                    else:
                        print(f"You tied with {what_char}")
                    draw_pile.push(draw_pile.pop())
                    op_draw_pile.push(op_draw_pile.pop())
                    break
                else:
                    print("INVALID INPUT")
            if did_quit:
                break
            print("")
            if turn == 1:
                turn = 2
            else:
                turn = 1
    except Exception as e:
        if ANSI:
            print("\033[0;30;41mTHE GAME HAS RUN INTO AN ERROR\033[0m")
            print(e)
        else:
            print("THE GAME HAS RUN INTO AN ERROR")
            print(e)

main()