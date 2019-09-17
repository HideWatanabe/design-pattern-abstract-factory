

class RestaurantGuide():
    def __init__(self, establishment_factory=None):
        self.restaurant_factory = establishment_factory

    def show_restaurant_list(self):
        restaurant_type = self.restaurant_factory()
        print("Lista de restaurantes do tipo {} : {}".format(restaurant_type, restaurant_type.list_all()))

class JapaneseFood():
    def list_all(self):
        return ",".join(["Kai Sushi", "Osaka Sushi"])

    def __str__(self):
        return "Japonês"

class BarbecueFood():
    def list_all(self):
        return ",".join(["Vento Haragano","Fogo de Chão"])

    def __str__(self):
        return "Churrasco"

if __name__ == "__main__":
    japanese_factory = RestaurantGuide(JapaneseFood)
    japanese_factory.show_restaurant_list()

    barbecue_factory = RestaurantGuide(BarbecueFood)
    barbecue_factory.show_restaurant_list()
