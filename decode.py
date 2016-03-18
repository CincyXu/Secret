# 2016/03/14 22:56
# __author__ = 'Cindy'
# coding:utf-8

import codecs


def read_telegragh_code():
    # 加载电报码
    telegragh_code = {}
    with codecs.open(r"telegraph_code1.txt", "r", "utf-8") as fr:
        for line in fr:
            code = line.strip().split(" ")
            telegragh_code[code[1]] = code[0]
    return telegragh_code


def morse_to_fence(morse_sentence):
    morse_code = {"-----": "0",  "*----": "1",  "**---": "2", "***--": "3", "****-": "4",
                  "*****": "5", "-****": "6", "--***": "7", "---**": "8", "----*": "9"}
    fence = []
    morse = morse_sentence.strip().split("/")
    for code in morse:
        fence.append(morse_code[code])
    print("".join(fence))
    return "".join(fence)


def fence_to_telegragh(fence):
    telegragh = ""
    cut = int(len(fence)/2)
    print(cut)
    x = fence[0:cut]
    y = fence[cut:len(fence)]
    for a, b in zip(x, y):
        telegragh += "{}{}".format(a, b)
    return telegragh


def telegragh_to_hanzi(telegragh, telegragh_code):
    characters = ""
    print(telegragh)
    for i in range(0, len(telegragh), 4):
        characters += telegragh_code[telegragh[i:i+4]]
    return characters


def read_and_write_article(r_file, w_file):
    # 读取已加密的文章，并解密
    article = []
    with codecs.open(r_file, "r", "utf-8") as fr:
        for line in fr:
            morse_sentence = line.strip()
            telegragh_code = read_telegragh_code()
            fence = morse_to_fence(morse_sentence)
            telegragh = fence_to_telegragh(fence)
            characters = telegragh_to_hanzi(telegragh, telegragh_code)
            article.append(characters + "\r\n")
    # 写入已经解密好的文章
    with codecs.open(w_file, "w", "utf-8") as fw:
        fw.writelines(article)


def encrypt_to_string(morse_sentence):
    telegragh_code = read_telegragh_code()
    fence = morse_to_fence(morse_sentence)
    telegragh = fence_to_telegragh(fence)
    print(telegragh)
    characters = telegragh_to_hanzi(telegragh, telegragh_code)
    print(characters)
    return characters

if __name__ == "__main__":
    # sentence = "所有的热情最终都会被稀释！"
    # read_and_write_article(r"article_code.txt", r"code_to_article.txt")
    string = encrypt_to_string("***--/****-/*****/*****/-----/**---/----*/--***/***--/***--/***--/--***/-----/**---/"
                               "****-/-----/-----/--***/****-/**---/-----/-----/*----/--***/*----/****-/----*/---**/"
                               "***--/-----/--***/*----/--***/*----/----*/-****/----*/**---/*----/**---/-----/**---/"
                               "*----/****-/-****/--***/****-/----*/-----/---**/*----/**---/----*/**---/----*/**---")
    print(string)
