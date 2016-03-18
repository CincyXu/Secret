# 2016/03/14 22:56
# __author__ = 'Cindy'
# coding:utf-8


import codecs


def read_telegragh_code():
    # 加载电报码
    telegragh_code = {}
    with codecs.open(r"telegraph_code.txt", "r", "utf-8") as fr:
        for line in fr:
            code = line.strip().split(" ")
            telegragh_code[code[0]] = code[1]
    return telegragh_code


def hanzi_to_telegragh(sentence, telegragh_code):
    # 把汉字转换成电报码
    hanzi_telegragh = ""
    for word in sentence:
        try:
            hanzi_telegragh += "{}".format(telegragh_code[word])
        except ValueError:
            print("‘{}’没有电报码！".format(word))
    return hanzi_telegragh


def telegragh_to_fence(hanzi_telegragh):
    # 用栅栏密码给电报码加密（用二栏密码）
    odd = ""
    even = ""
    for num, code in enumerate(hanzi_telegragh):
        if num % 2 == 0:  # 奇数位code相加
            odd += code
        else:  # 偶数位code相加
            even += code
    fence = odd + even
    return fence


def fence_to_morse(fence):
    # 用摩斯密码再度给电报码加密
    morse_code = {"0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-",
                  "5": "*****", "6": "-****", "7": "--***", "8": "---**", "9": "----*"}
    code_word = []
    for code in fence:
        code_word.append(morse_code[code])
    return "/".join(code_word)


def read_and_write_article(r_file, w_file):
    # 读取要加密的文章，并加密
    codes = []
    with codecs.open(r_file, "r", "utf-8") as fr:
        for line in fr:
            sentence = line.strip()
            telegragh_code = read_telegragh_code()
            hanzi_telegragh = hanzi_to_telegragh(sentence, telegragh_code)
            print(hanzi_telegragh)
            fence = telegragh_to_fence(hanzi_telegragh)
            print(fence)
            line_code = fence_to_morse(fence)
            codes.append(line_code + "\r\n")
    # 写入已经加密好的文章
    with codecs.open(w_file, "w", "utf-8") as fw:
        fw.writelines(codes)


def string_to_encrypt(sentence):
    telegragh_code = read_telegragh_code()
    hanzi_telegragh = hanzi_to_telegragh(sentence.strip(), telegragh_code)
    fence = telegragh_to_fence(hanzi_telegragh)
    codes = fence_to_morse(fence)
    return codes


if __name__ == "__main__":
    read_and_write_article(r"article.txt", r"article_code.txt")
    print(string_to_encrypt("XXX是个大混蛋！"))
