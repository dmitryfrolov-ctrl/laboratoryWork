import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QLabel


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Крестики-нолики на PyQt5")
        self.setGeometry(400, 400, 400, 400)

        self.buttons = []
        self.current_player = "X"
        self.move_count = 0

        self.create_buttons()

        self.status_label = QLabel(self)
        self.status_label.setGeometry(0, 310, 300, 30)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setText(f"Ход игрока {self.current_player}")

    def create_buttons(self):
        for row in range(3):
            row_buttons = []

            for col in range(3):
                button = QPushButton(self)
                button.setText("")
                button.setGeometry(col * 100, row * 100, 100, 100)
                button.clicked.connect(self.on_click)
                row_buttons.append(button)

            self.buttons.append(row_buttons)

    def on_click(self):
        button = self.sender()

        if button.text() == "":
            button.setText(self.current_player)
            self.move_count += 1
            self.check_winner()
            self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.setText(f"Ход игрока {self.current_player}")

    def check_winner(self):
        # Получаем текущее состояние поля
        board = [[self.buttons[row][col].text() for col in range(3)]
                 for row in range(3)]

        # Проверка строк
        for row in board:
            if row[0] != "" and row[0] == row[1] == row[2]:
                self.game_over(f"Игрок {row[0]} победил!")
                return

        # Проверка столбцов
        for col in range(3):
            if (board[0][col] != "" and
                    board[0][col] == board[1][col] == board[2][col]):
                self.game_over(f"Игрок {board[0][col]} победил!")
                return

        # Главная диагональ
        if (board[0][0] != "" and
                board[0][0] == board[1][1] == board[2][2]):
            self.game_over(f"Игрок {board[0][0]} победил!")
            return

        # Побочная диагональ
        if (board[0][2] != "" and
                board[0][2] == board[1][1] == board[2][0]):
            self.game_over(f"Игрок {board[0][2]} победил!")
            return

        # Ничья
        if self.move_count == 9:
            self.game_over("Ничья!")

    def game_over(self, message):
        QMessageBox.information(self, "Конец игры", message)
        self.reset_game()

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.setText("")

        self.current_player = "X"
        self.move_count = 0
        self.status_label.setText(f"Ход игрока {self.current_player}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())