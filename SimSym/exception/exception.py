class VarAlreadyDefinedException(Exception):
  """
  変数 {var_name} はすでに定義されています。
  """

  def __init__(self, var_name: str) -> None:
    super().__init__(f'変数 {var_name} はすでに定義されています。')


class VarNotDefinedException(Exception):
  """
  変数 {var_name} は定義されていません。
  """

  def __init__(self, var_name: str) -> None:
    super().__init__(f'変数 {var_name} は定義されていません。')


class ObjAlreadyDefinedException(Exception):
  """
  オブジェクト {obj_name} はすでに定義されています。
  """

  def __init__(self, obj_name: str) -> None:
    super().__init__(f'オブジェクト {obj_name} はすでに定義されています。')


class EmptyException(Exception):
  """
  {name} が空です。
  """

  def __init__(self, name: str) -> None:
    super().__init__(f'{name}が空です。')


class IllegalEquationException(Exception):
  """
  関係式には等号を一つだけ含めてください。
  """

  def __init__(self) -> None:
    super().__init__('関係式には等号を一つだけ含めてください。')
