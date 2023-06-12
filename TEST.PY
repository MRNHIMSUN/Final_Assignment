class Game:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print("Tên trò chơi:", self.name)

class GameCatalog:
    def __init__(self):
        self.games = []

    def display_games(self):
        if len(self.games) == 0:
            print("Danh sách trò chơi trống.")
        else:
            for game in self.games:
                game.display_info()
                print("------------")

    def add_game(self, game):
        self.games.append(game)
        print("Trò chơi đã được thêm vào danh sách.")

    def update_game(self, name, new_category):
        for game in self.games:
            if game.name == name:
                game.category = new_category
                print("Thông tin trò chơi đã được cập nhật.")
                return
        print("Không tìm thấy trò chơi trong danh sách.")

    def delete_game(self, name):
        for game in self.games:
            if game.name == name:
                self.games.remove(game)
                print("Trò chơi đã được xóa khỏi danh sách.")
                return
        print("Không tìm thấy trò chơi trong danh sách.")

    def search_game(self, keyword):
        found_games = []
        for game in self.games:
            if keyword.lower() in game.name.lower():
                found_games.append(game)
        if len(found_games) == 0:
            print("Không tìm thấy trò chơi phù hợp.")
        else:
            print("Các trò chơi phù hợp:")
            for game in found_games:
                game.display_info()
                print("------------")

    def sort_games(self):
        self.games.sort(key=lambda x: x.name.lower())
        print("Danh sách trò chơi đã được sắp xếp theo tên.")


def display_menu():
    print("===== Quản lý trò chơi =====")
    print("1. Xem danh sách trò chơi")
    print("2. Thêm trò chơi mới")
    print("3. Cập nhật thông tin trò chơi")
    print("4. Xóa thông tin trò chơi")
    print("5. Tìm kiếm trò chơi")
    print("6. Sắp xếp danh sách trò chơi")
    print("0. Thoát")


def main():
    game_catalog = GameCatalog()

    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            game_catalog.display_games()
        elif choice == "2":
            name = input("Nhập tên trò chơi: ")
            game = Game(name)
            game_catalog.add_game(game)
        elif choice == "3":
            name = input("Nhập tên trò chơi cần cập nhật: ")
            new_category = input("Nhập danh mục mới: ")
            game_catalog.update_game(name, new_category)
        elif choice == "4":
            name = input("Nhập tên trò chơi cần xóa: ")
            game_catalog.delete_game(name)
        elif choice == "5":
            keyword = input("Nhập từ khóa tìm kiếm: ")
            game_catalog.search_game(keyword)
        elif choice == "6":
            game_catalog.sort_games()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
