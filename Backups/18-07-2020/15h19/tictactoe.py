import pygame


class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.player1 = (player1, "X")
        self.player2 = (player2, "O")

    def check_win(self, player):
        """ Verifica se o jogador ganhou de alguma das maneiras """
        a = self.board
        n = player
        win_con_h = [n, n, n]

        # Vitória horizontal
        if win_con_h in self.board:
            return f"Player {player} wins!!!"

        # Vitória vertical
        for i in range(0, 3, 1):
            if a[0][i] == n and a[1][i] == n and a[2][i] == n:
                return f"Player {player} wins!!!"

        # Vitória diagonal
        if a[0][0] == n and a[0][0] == a[1][1] and a[0][0] == a[2][2]:
            return f"Player {player} wins!!!"

        if a[0][2] == n and a[0][2] == a[1][1] and a[0][2] == a[2][0]:
            return f"Player {player} wins!!!"
        return

    def check_tie(self):
        """ Analisa se o campo está completo e ninguém venceu """
        for line in self.board:
            for column in line:
                if column == 0:
                    return
        return "Tie!!!"

    def mark_spot(self, position, player):
        """ Verifica se a posição escolhida pelo jogador está ocupada e marca
        se não estiver. """
        line = position[0]
        column = position[1]
        if self.board[line][column] != 0:
            return "Invalid Move!"

        self.board[line][column] = player
        return self.board

    @staticmethod
    def position_treat(position):
        """Recebe o input e transforma nas coordenadas da posição"""
        list_spots = {
                "UL": [0, 0],
                "UM": [0, 1],
                "UR": [0, 2],
                "ML": [1, 0],
                "MM": [1, 1],
                "MR": [1, 2],
                "DL": [2, 0],
                "DM": [2, 1],
                "DR": [2, 2]
            }
        try:
            return list_spots[position]
        except KeyError:
            return 'Invalid Position!'

    def game(self):
        player_turn = self.player1
        waiting_player = self.player2

        while True:

            # Recebe a posição que o jogador vai marcar
            position = self.position_treat(input(
                f"Qual local {player_turn[0]} deseja jogar? "
            ))
            if position == "Invalid Position!":
                print(position)
                continue

            # Armazena a situação do board e atribui a ele
            status = self.mark_spot(position, player_turn[1])
            if status == "Invalid Move!":
                print(status)
                continue

            self.board = status
            player_turn, waiting_player = waiting_player, player_turn

            # Imprime a situação atual do board
            for row in self.board:
                print(row)

            # Verifica se o jogador venceu após marcar
            if self.check_win(waiting_player[1]) is not None:
                print()
                print(f"O jogador {waiting_player[0]} venceu!!!")
                break

            # Verifica se o board foi preenchido e ninguém ganhou
            if self.check_tie() is not None:
                print(self.check_tie())
                break


if __name__ == "__main__":
    pygame.init()

    # Resolução da janela do jogo
    screen_width, screen_height = 500, 500
    window = pygame.display.set_mode((screen_width, screen_height))

    # Título do jogo
    pygame.display.set_caption("Unbeatable Tic Tac Toe")

    # Cores
    WHITE = (255, 255, 255)

    # Carregamento de imagens
    images = []
    img = pygame.image.load("images/board.png")
    img = pygame.transform.scale(img, (360, 360))
    images.append(img)
    img = pygame.image.load("images/x.png")
    img = pygame.transform.scale(img, (60, 60))
    images.append(img)

    # Configuração de taxa de quadros
    FPS = 60
    clock = pygame.time.Clock()

    running = True

    # Campos disponíveis no board
    UL = [(112, 185), (105, 179)]
    UM = [(209, 270), (105, 179)]
    UR = [(303, 360), (105, 179)]
    ML = [(122, 185), (198, 270)]
    MM = [(209, 270), (198, 270)]
    MR = [(303, 360), (198, 270)]
    DL = [(112, 185), (295, 377)]
    DM = [(199, 270), (295, 377)]
    DR = [(293, 360), (295, 377)]

    places = [UL, UM, UR, ML, MM, MR, DL, DM, DR]

    while running:
        clock.tick(FPS)
        pygame.time.delay(40)

        window.fill(WHITE)
        window.blit(images[0], (70, 70))
        pygame.display.update()

        cursor_p = pygame.mouse.get_pos()

        for pos in places:
            if cursor_p[0] in range(pos[0][0], pos[0][1]) and cursor_p[
             1] in range(pos[1][0], pos[1][1]):
                window.blit(images[1], (pos[0][0], pos[1][0]))
                pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
