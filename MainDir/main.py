import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
key = -1


mouseCords: list[int] = [0, 0]

""" Функция, вызывающаяся при каждом дествии с мышью (движение, клик, скролл) """
""" У каждого действия своё значение event (cv2.EVENT_*НАЗВАНИЕ ИВЕНТА*) """
def mouse_callback(event: int, x: int, y: int, flags, params):
   mouseCords[0] = x
   mouseCords[1] = y

   # print(f'x = {x}, y = {y}')


""" Константы """
ESC_KEY: int = 27
MAIN_WINDOW: str = 'window'

""" Инициализация основного окна """
cv2.imshow(MAIN_WINDOW, cap.read()[1])
cv2.setMouseCallback(MAIN_WINDOW, mouse_callback)

while key != ESC_KEY and cv2.getWindowProperty(MAIN_WINDOW, cv2.WND_PROP_VISIBLE):

    """ Чтение кадра из вебки """
    isRead, image = cap.read()
    height, width, _ = image.shape

    # print(f"HEIGHT = {height}, WIDTH = {width}")

    """ Проход по центральному пикселю в каждом квадрате 20х20 """
    count = 0
    for m in range(20, width, 40):
        for n in range(20, height, 40):

            pixel = image[n, m]
            b, g, r = pixel

            """ Обнаружение негра """
            if b < 60 and g < 60 and r < 60:
                count += 1
                cv2.circle(image, (m, n), 5, (int(0), int(0), int(255)), -1)

    """ Рисование круга на позиции мыши """
    cv2.circle(image, mouseCords, 10, (0, 255, 0))

    """ Ворюга найден, если есть больше 20-и негров """
    if count >= 20:
        cv2.putText(image, 'There is an outsider in the house!', (50, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    """ Рисование сетки, резмечающей квадраты 20х20 """
    for i in range(0, height, 40):
        image[i, 0:width] = [255, 255, 255]
    for i in range(0, width, 40):
        image[0:height, i] = [255, 255, 255]

    """ Вывод изображения на экран """
    cv2.putText(image, str(count), (320, 210), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
    cv2.imshow(MAIN_WINDOW, image)
    key = cv2.waitKey(1)

cv2.destroyAllWindows()
