import pygame
from PIL import Image
import webbrowser as wb
import sys

a=str(input("Enter one here : "))
if a== "I do" :
    image_path = "image\\ido.jpg"
    image = Image.open(image_path)
    image.show()
    pygame.init() 
    pygame.mixer.music.load("C:\\Users\\LENOVO\\pyvision\\file music\\y2mate.com - I Do  911 Lyrics  Vietsub_64kbps.mp3")
    pygame.mixer.music.play(-1)  # Phát âm nhạc (lặp lại -1 để phát vô hạn)
    while True:  # Lặp vô hạn để chương trình không kết thúc ngay lập tức
        pass
elif a=="Diva troll" :
    image_path = "C:\\ST\\Pictures\\pictures thành tâm\\received_219092817852233.png"
    image = Image.open(image_path)
    image.show()
    pygame.init()  
    pygame.mixer.music.load("C:\\Users\\LENOVO\\pyvision\\file music\\y2mate.com - Thầy Lộc FuhoKhá Bảnh Hoài Lâm Tiến Bịp Anh Hảo Côvơ  Lê Hảo Khải Lốc Xoáy Pé Nâu  STAY BẢNH_64kbps.mp3")
    pygame.mixer.music.play(-1)  # Phát âm nhạc (lặp lại -1 để phát vô hạn)
    while True:  # Lặp vô hạn để chương trình không kết thúc ngay lập tức
        pass
elif a == "See you again" :
    image_path = "C:\\Users\\LENOVO\\pyvision\\image\\seeyouagain.jpg"
    image = Image.open(image_path)
    image.show()
    pygame.init() 
    pygame.mixer.music.load("C:\\Users\\LENOVO\\pyvision\\file music\\y2mate.com - Wiz Khalifa  See You Again ft Charlie Puth Official Video Furious 7 Soundtrack_64kbps.mp3")
    pygame.mixer.music.play(-1)  # Phát âm nhạc (lặp lại -1 để phát vô hạn)
    while True:  # Lặp vô hạn để chương trình không kết thúc ngay lập tức
        pass
elif a=="We don't talk anymore" :
    image_path = "C:\\Users\\LENOVO\\pyvision\\image\\wdtam.jpg"
    image = Image.open(image_path)
    image.show()
    pygame.init()  
    pygame.mixer.music.load("C:\\Users\\LENOVO\\pyvision\\file music\\y2mate.com - Charlie Puth  We Dont Talk Anymore feat Selena Gomez Official Video_64kbps.mp3")
    pygame.mixer.music.play(-1)  # Phát âm nhạc (lặp lại -1 để phát vô hạn)
    while True:  # Lặp vô hạn để chương trình không kết thúc ngay lập tức
        pass 
else : 
     wb.open("https://www.youtube.com/")
     sys.exit()

    