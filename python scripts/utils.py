import cv2 as cv
import keyboard
import time


def resize_image(image_path, output_path, dimensions):
    image = cv.imread(image_path)
    image = cv.resize(image, dimensions)
    cv.imwrite(output_path, image)


def crop_image(image_path, output_path):
    image = cv.imread(image_path)
    min_width = 0
    min_height = 0
    max_width = image.shape[1]
    max_height = image.shape[0]

    image_ready = False
    while image_ready is False:
        cropped_image = image[min_height:max_height, min_width:max_width]
        cv.imshow('image', cropped_image)
        cv.waitKey(0)

        if keyboard.is_pressed('up'):
            print(max_height)
            if max_height > 10:
                max_height -= 10

        if keyboard.is_pressed('down'):
            if min_height < max_height-10:
                min_height += 10

        if keyboard.is_pressed('left'):
            if max_width > 10:
                max_width -= 10

        if keyboard.is_pressed('right'):
            if min_width < max_width-10:
                min_width += 10

        if keyboard.is_pressed('return'):
            cv.imwrite(output_path, cropped_image)
            image_ready = True


# crop_image('../img/segev_and_me.jpg', '../img/segev_and_me2.jpg')
resize_image('../img/segev_and_me2.jpg', '../img/me_and_segev.jpg', (1920, 1080))
