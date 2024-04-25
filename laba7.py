
import os
from PIL import Image, ImageFilter
def zadanie1():
    image = Image.open('xom.jpg')
    image.show()
    print (f"размер: {image.size}")
    print (f"формат: {image.format}")
    print(f"Цветовая модель: {image.mode}")

def zadanie2():
    image = Image.open('xom.jpg')
    image.show()

    small_img2 = image.reduce(3)
    small_img2.save('small_xom.jpg')
    small_img2.show()

    horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal.save('horizontal.jpg')
    horizontal.show()

    vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
    vertical.save('vertical.jpg')
    vertical.show()

def zadanie3():
    import os
    # Путь к исходной папке с изображениями
    source_folder = 'D:/Чикурова хомяк 1-МД-4/xomm'
    # Путь к папке, куда будут сохранены обработанные изображения
    destination_folder = 'D:/Чикурова хомяк 1-МД-4/xomm1'

    # Создаем папку для сохранения обработанных изображений, если она еще не существует
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Список имен файлов, которые нужно обработать
    file_names = ['хом1.jpg', 'хом2.jpg', 'хом3.jpg', 'хом4.jpg', 'хом5.jpg']

    for file_name in file_names:
        # Открываем изображение
        img = Image.open(os.path.join(source_folder, file_name))

        # Применяем фильтр "черно-белое"
        img_gray = img.convert('L')

        # Сохраняем обработанное изображение в новой папке с новым именем
        new_file_name = 'new_' + file_name
        img_gray.save(os.path.join(destination_folder, new_file_name))

    print("Обработка изображений завершена.")

def zadanie3():
    nach = 'pythonProject1'
    obrabot = 'pythonProject1/pugpug'
    if not os.path.exists(obrabot):
        os.makedirs(obrabot)
    imag = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for image_name in imag:
        image = Image.open(os.path.join(nach, image_name))

        image_filtered = image.filter(ImageFilter.CONTOUR)

        new_image_name = 'filtered_' + image_name
        image_filtered.save(os.path.join(obrabot, new_image_name))
    print("Обработка изображений завершена.")

def zadanie4():
    iznach = 'pythonProject1'
    water = 'pythonProject1/WW.jpg'
    gotov = 'pythonProject1/gupgup'
    if not os.path.exists(gotov):
        os.makedirs(gotov)
    image_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for image_name in image_names:
        image = Image.open(os.path.join(iznach, image_name))
        watermark = Image.open(water)
        size = (100, 50)
        watermark = watermark.resize(size)
        watermark_width, watermark_height = watermark.size
        image_width, image_height = image.size
        wtyt = (image_width - watermark_width, image_height - watermark_height)
        image.paste(watermark, wtyt, watermark)
        new_image_name = 'watermarked_' + image_name
        image.save(os.path.join(gotov, new_image_name))
    print("Добавление водяного знака завершено.")

while True:
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print('5. ')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        print(zadanie3())
    elif a == 4:
        print(zadanie4())
    elif a == 5:
        break
    else:
        print('Неверное действие')