import pygame
import os


class Board:
    def __init__(self):
        self.board = ['_'] * 9

    def update(self, player, number):
        if number in list(range(9)):
            if self.board[number] == '_':
                if player.playernumber == 0:
                    self.board[number] = 'O'
                    return 1
                else:
                    self.board[number] = 'X'
                    return 0
            else:
                return player.playernumber
        else:
            return player.playernumber
            # self.update(player, number)

    def checkifwin(self):
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != '_':
            return True
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != '_':
            # self.printwin(player.playernumber)
            return True
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != '_':
            return True
            # self.printwin(playernumber)
        if self.board[3] == self.board[4] == self.board[5] and self.board[3] != '_':
            return True
            # self.printwin(playernumber)
        if self.board[6] == self.board[7] == self.board[8] and self.board[6] != '_':
            return True
            # self.printwin(playernumber)
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != '_':
            return True
            # self.printwin(playernumber)
        if self.board[1] == self.board[4] == self.board[7] and self.board[1] != '_':
            return True
            # self.printwin(playernumber)
        if self.board[2] == self.board[5] == self.board[8] and self.board[2] != '_':
            return True
            # self.printwin(playernumber)
        if all(ele in ['O', 'X'] for ele in self.board):
            return True
            # self.printwin(8)
        else:
            return False


class Player:
    def __init__(self, playernumber):
        self.playernumber = playernumber

    def print(self):
        print("Spieler " + str(self.playernumber +1) + " hat gewonnen.")


FIELD = pygame.transform.scale2x(pygame.image.load(os.path.join("tictactoe.png")))
IMG_X = pygame.transform.scale(pygame.image.load(os.path.join("tictactoe_x.png")), (130, 130))
IMG_O = pygame.transform.scale(pygame.image.load(os.path.join("tictactoe_o.png")), (130, 130))


def draw_window(win, board, player):
    win.fill((255, 255, 255))
    win.blit(FIELD, (0, 0))
    text = pygame.font.SysFont("comicsans", 50).render("Player: " + str(player.playernumber+1), True, (0, 0, 0))
    win.blit(text, (0, 430))
    for c, symbol in enumerate(board.board):
        if symbol in "XO":
            draw_symbol(c, symbol, win)
    pygame.display.update()


def draw_symbol(pos, symbol, win):
    if symbol == 'X':
        img = IMG_X
    elif symbol == 'O':
        img = IMG_O
    if pos == 0:
        win.blit(img, (20, 20))
    elif pos == 1:
        win.blit(img, (160, 20))
    elif pos == 2:
        win.blit(img, (300, 20))
    elif pos == 3:
        # print("3")
        win.blit(img, (20, 160))
    elif pos == 4:
        # print("4")
        win.blit(img, (160, 160))
    elif pos == 5:
        # print("5")
        win.blit(img, (300, 160))
    elif pos == 6:
        # print("6")
        win.blit(img, (20, 300))
    elif pos == 7:
        # print("7")
        win.blit(img, (160, 300))
    elif pos == 8:
        # print("8")
        win.blit(img, (300, 300))


def main():
    board = Board()
    players = [Player(0), Player(1)]
    win = pygame.display.set_mode((450, 500))
    win.fill((255, 255, 255))
    pygame.display.set_caption("TicTacToe")
    icon = pygame.image.load("tictactoe.png")
    pygame.display.set_icon(icon)
    counter = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 0)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_2:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 1)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_3:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 2)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_4:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 3)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_5:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 4)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_6:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 5)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_7:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 6)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_8:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 7)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
                elif event.key == pygame.K_9:
                    if not board.checkifwin():
                        counter = board.update(players[counter], 8)
                    # else:
                    #     players[counter].print()
                    #     print("hat gewonnen")
                    #     pygame.quit()
                    #     quit()
        if board.checkifwin():
            draw_window(win, board, players[counter])
            players[counter].print()
            pygame.quit()
            quit()
        draw_window(win, board, players[counter])

if __name__ == "__main__":
    pygame.font.init()
    main()
