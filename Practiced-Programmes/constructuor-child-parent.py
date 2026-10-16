class Laptop:

    def __init__(self):
        print("Laptop Constructor")


class Dell(Laptop):

    def __init__(self):
        super().__init__()
        print("Dell Constructor")


d1 = Dell()