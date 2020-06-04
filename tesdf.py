class Person:
  # объявление конструктора
  def __init__(self,initialAge):
    if initialAge < 0:
      print("Age is not valid, setting age to 0.")
      self.initialAge = 0
    else:
      self.initialAge = initialAge

  # объявление конструктора amIOld
  def amIOld(self): # странное название
    if self.initialAge < 13:
      print("You are young.")
    elif 13 <= self.initialAge < 18:
      print("You are a teenager.")
    else:
      print("You are old.")

  # объявление метода yearPasses
  def yearPasses(self):
    self.initialAge = self.initialAge + 1
# цикл ниже я не писал, он был дан в задании.

## Комментарии
# ====== работа с обйектами класса Person И код программы ======

# инициализация переменной t (вывод с клавиатуры, или инициализация значением)
t = int(input()) #эту переменную можно инициализировать просто значением, например 5  t = 5
# лучше не инициализировать переменные инпутом, потому, что потом непонятно сразу при запуске, что с программой происх /
# ====начало цикла 1 =====
for i in range(0, t): # цикл управления
    age = int(input()) # то же, нужно инициировать цифрой (инициализировать переменную age цифровым литералом )

    # здесь основное место работы нашего класса

    # появляется объет p типа Person
    p = Person(age)
    # запуск(вызов метода) нашего метода
    p.amIOld()
    #запуск внутреннего цикла
    for j in range(0, 3):
        #запуск (вызов) метода печати фраз
        p.yearPasses()
    # повторный запуск(вызов метода) нашего метода ЗАЧЕМ
    p.amIOld()
    print("")
#==== конец цикла 1========