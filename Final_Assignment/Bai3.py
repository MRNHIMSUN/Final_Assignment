import csv

class Game:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class GameCatalog:
    def __init__(self, filename):
        self.filename = filename
        self.games = []

    def load_games_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    category = row[1]
                    game = Game(name, category)
                    self.games.append(game)
            print("Danh sách trò chơi đã được tải từ tệp tin.")
        except FileNotFoundError:
            print("Không tìm thấy tệp tin danh sách trò chơi.")

    def save_games_to_file(self):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for game in self.games:
                    writer.writerow([game.name, game.category])
            print("Danh sách trò chơi đã được lưu vào tệp tin.")
        except:
            print("Lỗi khi lưu danh sách trò chơi vào tệp tin.")

    def display_games(self):
        if len(self.games) > 0:
            print("Danh sách trò chơi:")
            for game in self.games:
                print(f"- {game.name} ({game.category})")
        else:
            print("Danh sách trò chơi rỗng.")

    def add_game(self, name, category):
        game = Game(name, category)
        self.games.append(game)
        print(f"Trò chơi '{name}' đã được thêm vào danh mục.")

    def update_game(self, name, new_category):
        found = False
        for game in self.games:
            if game.name == name:
                game.category = new_category
                found = True
                break
        if found:
            print(f"Thông tin trò chơi '{name}' đã được cập nhật.")
        else:
            print(f"Không tìm thấy trò chơi '{name}' trong danh mục.")

    def remove_game(self, name):
        found = False
        for game in self.games:
            if game.name == name:
                self.games.remove(game)
                found = True
                break
        if found:
            print(f"Trò chơi '{name}' đã được xóa khỏi danh mục.")
        else:
            print(f"Không tìm thấy trò chơi '{name}' trong danh mục.")

    def search_game(self, keyword):
        result = []
        for game in self.games:
            if keyword.lower() in game.name.lower() or keyword.lower() in game.category.lower():
                result.append(game)
        if len(result) > 0:
            print(f"Kết quả tìm kiếm cho từ khóa '{keyword}':")
            for game in result:
                print(f"- {game.name} ({game.category})")
        else:
            print(f"Không tìm thấy trò chơi nào phù hợp với từ khóa '{keyword}'.")

    def sort_games(self):
        self.games.sort(key=lambda game: game.name.lower())
        print("Danh sách trò chơi đã được sắp xếp theo tên.")

if __name__ == '__main__':
    filename = "Final_Assignment\danhsachgame.txt"
    catalog = GameCatalog(filename)
    catalog.load_games_from_file()

    while True:
        print("\n=== ỨNG DỤNG QUẢN LÝ TRÒ CHƠI ===")
        print("1. Xem danh sách trò chơi")
        print("2. Thêm trò chơi mới")
        print("3. Cập nhật thông tin trò chơi")
        print("4. Xóa thông tin trò chơi")
        print("5. Tìm kiếm trò chơi")
        print("6. Sắp xếp danh sách trò chơi")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            catalog.display_games()
        elif choice == "2":
            name = input("Nhập tên trò chơi mới: ")
            category = input("Nhập danh mục của trò chơi mới: ")
            catalog.add_game(name, category)
            catalog.save_games_to_file()
        elif choice == "3":
            name = input("Nhập tên trò chơi cần cập nhật: ")
            new_category = input("Nhập danh mục mới cho trò chơi: ")
            catalog.update_game(name, new_category)
            catalog.save_games_to_file()
        elif choice == "4":
            name = input("Nhập tên trò chơi cần xóa: ")
            catalog.remove_game(name)
            catalog.save_games_to_file()
        elif choice == "5":
            keyword = input("Nhập từ khóa tìm kiếm: ")
            catalog.search_game(keyword)
        elif choice == "6":
            catalog.sort_games()
            catalog.save_games_to_file()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
