import pygame

pygame.init()

# Resolução da janela do jogo
screen_width, screen_height = 500, 500
window = pygame.display.set_mode((screen_width, screen_height))

# Título do jogo
pygame.display.set_caption("Unbeatable Tic Tac Toe")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fontes
TEXT_FONT = pygame.font.SysFont('comicsans', 70)

# Carregamento de imagens
images = []
img = pygame.image.load("images/board.png")
img = pygame.transform.scale(img, (360, 360))
images.append(img)
img = pygame.image.load("images/x.png")
img = pygame.transform.scale(img, (60, 60))
images.append(img)
img = pygame.image.load("images/y.png")
img = pygame.transform.scale(img, (60, 60))
images.append(img)

# Configuração de taxa de quadros
FPS = 60
clock = pygame.time.Clock()

running = True

# Campos disponíveis no board
places = [
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

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

player1 = ("X", 1, input("Nome do jogador 1 "))
player2 = ("O", 2, input("Nome do jogador 2 "))


def render_screen():
    window.fill(WHITE)
    window.blit(images[0], (70, 70))
    for pos in places:
        if pos[2] == "X":
            window.blit(images[1], (pos[0][0], pos[1][0]))
        if pos[2] == "O":
            window.blit(images[2], (pos[0][0], pos[1][0]))
    pygame.display.update()


def check_win(player):
    """ Verifica se o jogador ganhou de alguma das maneiras """
    a = board
    n = player
    win_con_h = [n, n, n]

    # Vitória horizontal
    if win_con_h in board:
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


def check_tie():
    """ Analisa se o campo está completo e ninguém venceu """
    for line in board:
        for column in line:
            if column == 0:
                return
    return "Tie!!!"


player_turn, waiting = player1, player2
next_p = False
while running:
    clock.tick(FPS)
    pygame.time.delay(40)

    render_screen()

    cursor_p = pygame.mouse.get_pos()

    # Mapeamento do mouse e checagem para marcação do jogador
    for pos in places:
        if cursor_p[0] in range(pos[0][0], pos[0][1]) and cursor_p[
         1] in range(pos[1][0], pos[1][1]):
            if pos[2] == "":
                window.blit(images[player_turn[1]], (pos[0][0], pos[1][0]))
            pygame.display.update()
            if pygame.event.get(pygame.MOUSEBUTTONDOWN) and pos[2] == "":
                pos[2] = player_turn[0]
                board[pos[3]][pos[4]] = player_turn[0]
                next_p = True  # Aqui garante a passagem do turno

    # Checando e anunciando vitória do jogador
    if check_win(player_turn[0]) is not None:
        window.fill(WHITE)
        text = TEXT_FONT.render(f"{player_turn[2]} VENCEU!!!", 1, BLACK)
        window.blit(
            text,
            (screen_width/2 - text.get_width()/2,
             screen_height/2 - text.get_height()/2)
        )
        pygame.display.update()
        pygame.time.delay(3000)
        break

    # Checando e anunciando empate
    if check_tie() is not None:
        window.fill(WHITE)
        text = TEXT_FONT.render("EMPATE!!!", 1, BLACK)
        window.blit(
            text,
            (screen_width/2 - text.get_width()/2,
             screen_height/2 - text.get_height()/2)
        )
        pygame.display.update()
        pygame.time.delay(3000)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Passagem de turno
    if next_p:
        waiting, player_turn = player_turn, waiting
        next_p = False

pygame.quit()
