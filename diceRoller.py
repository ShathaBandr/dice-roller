import random
from colorama import init, Fore, Style

init(autoreset=True)

dice_art = {
    1: (
        "┌────────┐",
        "│        │",
        "│    ●   │",
        "│        │",
        "└────────┘",
    ),
    2: (
        "┌────────┐",
        "│ ●      │",
        "│        │",
        "│      ● │",
        "└────────┘",
    ),
    3: (
        "┌────────┐",
        "│ ●      │",
        "│   ●    │",
        "│      ● │",
        "└────────┘",
    ),
    4: (
        "┌────────┐",
        "│ ●    ● │",
        "│        │",
        "│ ●    ● │",
        "└────────┘",
    ),
    5: (
        "┌────────┐",
        "│ ●    ● │",
        "│    ●   │",
        "│ ●    ● │",
        "└────────┘",
    ),
    6: (
        "┌────────┐",
        "│ ●    ● │",
        "│ ●    ● │",
        "│ ●    ● │",
        "└────────┘",
    )
}

dice = []
total = 0

num_of_dice = int(input(Fore.CYAN + "How many dice?: "))

for _ in range(num_of_dice):
    dice.append(random.randint(1, 6))

dice_color = Fore.RED + Style.BRIGHT

print("\n" + Fore.YELLOW + "Your dice roll:")

for line in range(5):
    for die in dice:
        print(dice_color + dice_art[die][line], end=" ")
    print()

for die in dice:
    total += die

print(Fore.GREEN + f"\nTotal: {total}")
