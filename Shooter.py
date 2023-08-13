class Shooter:
    def __init__(self):
        self._your_gun = None
        self._your_bullet = None
        self._type_bullet = None
        self._count_bullet = None
        self._all_gun = {'Submachine Gun': (100, 10, 0.5), 'Assault Rifle': (200, 20, 1),
               'Pistol': (80, 8, 0.5), 'Shotgun': (50, 40, 4), 'Sniper Rifle': (1000, 30, 3)}
        self._bullets_name = {"A": (0.5, 1), 'B': (1, 1.5), 'C': (3, 3), 'D': (4, 2)}

    def set_gun_by_name(self, name: str) -> None:

        if name not in self._all_gun.keys():
            raise ValueError("ur  gun doesn't found")
        else:
            self._your_gun = name
            # print(f'selected: {self._your_gun }')



    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        _size_exist = 0
        self._count_bullet = count
        if self._your_gun == None:
            raise ValueError("you haven't yet selected your gun!")
        if self._count_bullet < 0:
            raise  ValueError("you selected minus of bullet count")

        for key, value in self._bullets_name.items():
            if value[0] == size:
                self._your_bullet = size
                self._type_bullet = key
                _size_exist += 1

        if _size_exist == 0:
            raise ValueError("size of bullet invalid")

        # print(self._type_bullet)

        if self._all_gun[self._your_gun][2] != self._your_bullet:
            raise ValueError("your gun and bullet doesnt match toghter")


    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:

        if self._count_bullet <= 0:
            raise ValueError("you  haven't got bulllet")
        else:
            self._count_bullet -= 1

        if self._your_gun == None:
            raise ValueError("you haven't yet selected your gun!")




        if target_x <= aim_x <= target_x + 10 and target_y <= aim_y <= target_y + 10:
            if self._all_gun[self._your_gun][0] < target_distance:
                return 0
            else:
                return (self._all_gun[self._your_gun][1] * self._bullets_name[self._type_bullet][1])

        else:
            raise ValueError("your squre isnt overlapping")








# shooter = Shooter()
# shooter.set_gun_by_name('Submachine Gun')
# shooter.add_bullet_of_given_size_to_gun(0.5, 1)
# result = shooter.shoot_to_target(1, 1, 200000, 5, 4)
# print(result)
# result should be 10



