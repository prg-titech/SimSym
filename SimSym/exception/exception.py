class VarAlreadyDefinedException(Exception):
  def __init__(self, var_name: str) -> None:
    super().__init__(f'変数 {var_name} はすでに定義されています。')


class VarNotDefinedException(Exception):
  def __init__(self, var_name: str) -> None:
    super().__init__(f'変数 {var_name} は定義されていません。')


class ObjAlreadyDefinedException(Exception):
  def __init__(self, obj_name: str) -> None:
    super().__init__(f'オブジェクト {obj_name} はすでに定義されています。')
