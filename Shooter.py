class Shooter:
    def __init__(self):
        self._your_gun = None
        self._your_bullet = None
        self._all_gun = {'Submachine Gun': (100, 10, 0.5), 'Assault Rifle': (200, 20, 1),
               'Pistol': (80, 8, 0.5), 'Shotgun': (50, 40, 4), 'Sniper Rifle': (1000, 30, 3)}
        self._bullets_name = {"A": (0.5, 1), 'B': (1, 1.5), 'C': (3, 3), 'D': (4, 2)}

    def set_gun_by_name(self, name: str) -> None:

        if name not in self._all_gun.keys():
            raise ValueError("ur  gun doesn't found")
        else:
            self._your_gun = name
            print(f'selected: {self._your_gun }')



    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        _size_exist = 0

        if self._your_gun == None:
            raise ValueError("you haven't yet selected your gun!")
        if count < 0:
            raise  ValueError("you selected minus of bullet count")

        for key, value in self._bullets_name.items():
            if value[0] == size:
                self._your_bullet = size
                _size_exist += 1
        if _size_exist == 0:
            raise ValueError("size of bullet invalid")

        if self._all_gun[self._your_gun][2] != self._your_bullet:
            raise ValueError("your gun and bullet doesnt match toghter")


    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        pass

a1 = Shooter()
a1.set_gun_by_name("Submachine Gun")
a1.add_bullet_of_given_size_to_gun(0.5 ,20)



bulletsname ={"A":(0.5, 1), 'B':(1, 1.5), 'C':(3, 3), 'D':(4, 2)}
#
# q = 'C'
#
# print(bulletsname.keys())
# if q  in bulletsname:
#     print("yes in it")
# else:
#     print("no in it")
#
# print(bulletsname)
