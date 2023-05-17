import Square


class maps:
    map_size: tuple[int, int]  # 一个二元元组，确定maps有几行几列
    map_Square: list[list[Square.Square]]  # 一个二维数组，维护地图所有的方格

    def __init__(self, size: tuple[int, int]):
        """
        maps的构造函数
        :param size: 传入该地图的大小
        """
        self.map_size = size
        for i in range(size[0]):
            self.map_Square.append(list())
            for j in range(size[1]):
                self.map_Square[i].append(Square.Square())
