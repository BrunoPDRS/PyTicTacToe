import pygame
pygame.font.init()
pygame.init()


class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = ["X", 1, player1, 0]
        self.player2 = ["O", 2, player2, 0]
        self.next_p = False
        self.running = True
        self.show_game = True

        # Resolução da janela do jogo
        self.screen_width, self.screen_height = 500, 500
        self.window = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )

        # Cores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Fontes
        self.TEXT_FONT = pygame.font.SysFont('comicsans', 70)
        self.SCORE_FONT = pygame.font.SysFont('comicsans', 30)

        # Carregamento de imagens
        self.images = []
        img = pygame.image.load("images/board.png")
        img = pygame.transform.scale(img, (360, 360))
        self.images.append(img)
        img = pygame.image.load("images/x.png")
        img = pygame.transform.scale(img, (60, 60))
        self.images.append(img)
        img = pygame.image.load("images/y.png")
        img = pygame.transform.scale(img, (60, 60))
        self.images.append(img)

        # Configuração de taxa de quadros
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.running = True

        # Campos disponíveis no board
        self.places = [
            [(112, 185), (105, 179), "", 0, 0],
            [(209, 270), (105, 179), "", 0, 1],
            [(303, 360), (105, 179), "", 0, 2],
            [(122, 185), (198, 270), "", 1, 0],
            [(209, 270), (198, 270), "", 1, 1],
            [(303, 360), (198, 270), "", 1, 2],
            [(112, 185), (295, 377), "", 2, 0],
            [(199, 270), (295, 377), "", 2, 1],
            [(293, 360), (295, 377), "", 2, 2]
        ]

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def render_screen(self):
        """ Renderiza a tela do jogo em tempo real, com placar e marcações """
        if self.show_game:
            self.window.fill(self.WHITE)
            self.window.blit(self.images[0], (70, 70))

            for pos in self.places:
                if pos[2] == "X":
                    self.window.blit(self.images[1], (pos[0][0], pos[1][0]))
                if pos[2] == "O":
                    self.window.blit(self.images[2], (pos[0][0], pos[1][0]))
        score1 = self.SCORE_FONT.render(
                f'Score {self.player1[2]}: {self.player1[3]}', 1, self.BLACK
            )
        score2 = self.SCORE_FONT.render(
                f'Score {self.player2[2]}: {self.player2[3]}', 1, self.BLACK
            )
        self.window.blit(score1, (10, 10))
        self.window.blit(score2, (10, 10 + score2.get_height()))
        pygame.display.update()

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

    def play_again(self):
        """ Imprime a tela de jogar novamente e checa resposta """
        self.show_game = False
        self.window.fill(self.WHITE)
        text = self.TEXT_FONT.render("Jogar novamente?", 1, self.BLACK)
        text_confirm = self.TEXT_FONT.render("Y  /  N", 1, self.BLACK)
        self.window.blit(
                    text,
                    (self.screen_width/2 - text.get_width()/2,
                     self.screen_height/2 - text.get_height()/2 - 20)
                )
        self.window.blit(
                    text_confirm,
                    (self.screen_width/2 - text_confirm.get_width()/2,
                     self.screen_height/2 + text_confirm.get_height()*2 - 30)
                )
        score1 = self.SCORE_FONT.render(
                f'Score {self.player1[2]}: {self.player1[3]}', 1, self.BLACK
            )
        score2 = self.SCORE_FONT.render(
                f'Score {self.player2[2]}: {self.player2[3]}', 1, self.BLACK
            )
        self.window.blit(score1, (10, 10))
        self.window.blit(score2, (10, 10 + score2.get_height()))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                # Limpa o campo e recomeça o jogo
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    self.board = [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]
                    ]
                    for pos in self.places:
                        pos[2] = ""
                    pygame.time.delay(500)
                    self.show_game = True
                    return

                # Fecha o jogo
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    pygame.time.delay(500)
                    self.running = False
                    return

                elif event.type == pygame.QUIT:
                    self.running = False
                    return

    def main(self):
        # Título do jogo
        pygame.display.set_caption("Unbeatable Tic Tac Toe")
        player_turn, waiting = self.player1, self.player2

        while self.running:
            self.clock.tick(self.FPS)
            pygame.time.delay(40)

            self.render_screen()

            cursor_p = pygame.mouse.get_pos()

            # Mapeamento do mouse e checagem para marcação do jogador
            for pos in self.places:
                if cursor_p[0] in range(pos[0][0], pos[0][1]) and cursor_p[
                 1] in range(pos[1][0], pos[1][1]):
                    if pos[2] == "" and self.show_game:
                        self.window.blit(
                            self.images[player_turn[1]], (pos[0][0], pos[1][0])
                        )
                    pygame.display.update()
                    if pygame.event.get(
                        pygame.MOUSEBUTTONDOWN
                    ) and pos[2] == "":
                        pos[2] = player_turn[0]
                        self.board[pos[3]][pos[4]] = player_turn[0]
                        self.next_p = True  # Aqui garante a passagem do turno

            # Checando e anunciando vitória do jogador
            if self.check_win(player_turn[0]) is not None:
                player_turn[3] += 1
                pygame.time.delay(300)
                self.window.fill(self.WHITE)
                text = self.TEXT_FONT.render(
                    f"{player_turn[2]} VENCEU!!!", 1, self.BLACK
                )
                self.window.blit(
                    text,
                    (self.screen_width/2 - text.get_width()/2,
                     self.screen_height/2 - text.get_height()/2)
                )
                pygame.display.update()
                pygame.time.delay(2000)

                self.play_again()
                continue

            # Checando e anunciando empate
            if self.check_tie() is not None:
                pygame.time.delay(300)
                self.window.fill(self.WHITE)
                text = self.TEXT_FONT.render("EMPATE!!!", 1, self.BLACK)
                self.window.blit(
                    text,
                    (self.screen_width/2 - text.get_width()/2,
                     self.screen_height/2 - text.get_height()/2)
                )
                pygame.display.update()
                pygame.time.delay(2000)

                self.play_again()
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Passagem de turno
            if self.next_p:
                waiting, player_turn = player_turn, waiting
                self.next_p = False


if __name__ == "__main__":
    game = TicTacToe("Bruno", "Barbara")
    game.main()

    pygame.quit()
