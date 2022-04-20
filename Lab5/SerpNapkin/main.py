iterations = input("Введите глубину фрактала: ")
iterations_n = int(iterations)
size = 100 #длина линии

import turtle

# #ниже переместим черепашку немного вправо, чтобы ближе к серединке рисовалось
turtle.penup()
turtle.forward(300)
turtle.pendown()

turtle.speed(7) #изменим скорость рисования черепашки

#наклонили черепашку вправо
turtle.right(30)
#подняли черепашку, так как рисовать будем с помощью stamp
turtle.penup()


def napkinSer(iterations_n, size):
  if (iterations_n == 0):
    turtle.stamp()  #рисуем треугольник  с помощью stamp
  else:
    for i in range(0, 3):  #идём "треугольно" и рисуем на месте остановки треугольники
      turtle.forward(size)
      napkinSer(iterations_n - 1, size / 2)
      turtle.backward(size)
      turtle.left(120)


napkinSer(iterations_n, size)

turtle.done() #чтобы окно рисования не закрылось