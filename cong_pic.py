from aip import AipOcr
 
# 定义常量
APP_ID = '23981884'
API_KEY = 'grtlt8VeYbY01lrmoZqRNOZC'
SECRET_KEY = '8Wl1kPmxYfURvOOYHkDum0MiHV37XBtf'
 
# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
# 读取图片
filePath = "test.png"
 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
 
# 调用通用文字识别接口
def main():
    words = []
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    #print(result)
    words_result=result['words_result']
    for i in range(len(words_result)):
        words.append(words_result[i]['words'])
        #print(words_result[i]['words'])

    result_words = "".join(words)
    #print(result_words)

    return result_words

if __name__ == "__main__":
    main()

