from src import users


LOGO: str = '    ⣀⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀\n' \
            '⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢙⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⡋⠀⠀⠀⠀⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⢸⠀⠀⣿⠛⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⢸⠀⠀⣿⠀⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⢸⠀⣾⡇⠀⠀⠀\n' \
            '⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡆⠀⣿⡿⠀⠀⠀\n' \
            '⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀⠀\n' \
            '⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀⠀⠀\n' \
            '⠀⠀⠀⣿⣿⣤⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⠀⠀⠀⠀\n' \
            '⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀\n' \
            '⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀\n' \
            '⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀\n' \
            '     Welcome to Goosino!         \n'


STEP_LIST: str = \
    'Possible steps:\n' \
    '1. Player places a bet\n' \
    '2. Oldest bet is resolved\n' \
    '3. War goose attacks player\n' \
    '4. Honk goose screams at player\n' \
    '5. Goose (any kind of) tries to steal from a player\n' \
    '6. Player goes all-in\n'

INIT_USERS: list[users.Player | users.Goose | users.WarGoose | users.HonkGoose] = \
    [
        users.Player("Ethan"), users.Player("Ivan"), users.Player("Roma"), users.Player("Mihail"),
        users.Player("Dmitry"), users.Player("Konstantin"), users.Player("Andrey"), users.Player("Sergey"),
        users.Player("Anton"), users.Player("Pavel"), users.Player("Artem"), users.Player("Nikolay"),

        users.Goose("Boris"), users.Goose("Viktor"), users.Goose("Oleg"), users.Goose("Peter"),
        users.WarGoose("Denis"), users.WarGoose("Grigoriy"), users.WarGoose("Fedor"), users.WarGoose("Igor"),
        users.HonkGoose("Gosha", 0.3), users.HonkGoose("Kirill", 0.5), users.HonkGoose("Maksim", 0.2), users.HonkGoose("Valera", 0.9)
    ]
