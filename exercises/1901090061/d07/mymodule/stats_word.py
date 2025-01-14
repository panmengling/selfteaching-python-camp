#创建一个函数，接收字符串text作为参数
def stats_text_en(text):
    """
    stats_text_en 可接收一个英文字符串text作为参数，统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
    """
    #创建一个空列表
    words = []
    #想要删除的标点符号
    symbols = '.,!-*，。？：、?"「 」'
    #将字符串text分割后赋值给elements，其中包含标点符号，英文单词，和空格，elements数据格式为列表
    elements = text.split()
    #遍历elements中的每一个element
    for element in elements:
    #遍历标点符号
        for symbol in symbols:
            #将标点符号替换为空格，并赋值给element，element是字符串
            element = element.replace(symbol,'')
            #如果element不是空字符，即element是单词，将单词添加到words列表中
        if len(element) > 0:
            words.append(element.lower())
    #print(words)
    #创建word_set集合，将重复单词去重
    word_set = set(words)
    #print(word_set)
    #创建字典
    counter = {}
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)
    #将字典按照单词词频为参数进行降序排列
    #print(sorted(counter.items(),key = lambda x:x[1],reverse = True))
#定义一个函数,以text作为参数
def stats_text_cn(text):
    """
    stats_text_cn接收一个中文字符串text作为参数，统计参数中每个汉字出现的次数，最后返回一个按字频降序排列排列的数组
    """
    #建立一个列表
    cn_characters = []
    for character in text:
    #如果是汉字，则加入列表中,\u4e00----\u9fff 是Unicode中中文字符的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    #建立一个字典
    cn_counter = {}
    #建立集合将文本去重
    character_set = set(cn_characters)
    for character in character_set:
        cn_counter[character] = cn_characters.count(character)
    #返回按字频降序排列的数组
    return sorted(cn_counter.items(),key = lambda x:x[1],reverse= True)
    #print(sorted(cn_counter.items(),key = lambda x:x[1],reverse = True))
def stats_text(text):
    """
    stats_text接收字符串text作为参数，分别调用stats_word.en和stats_text_cn函数，输出合并词频统计结果
    """
    #创建两个列表分别添加中英文
    en_words = []
    cn_characters = []
    #遍历text将中英文区分开加入列表
    for element in text:
        if '\u4e00' <= element <= '\u9fff':
            cn_characters.append(element)
        else:
            en_words.append(element)
    #将中英文列表转为字符串
    sample_text_1 = ''
    sample_text_2 = ''
    text_1 = sample_text_1.join(en_words)
    text_2 = sample_text_2.join(cn_characters)
    return stats_text_en(text_1) + stats_text_cn(text_2)

text = '''
愚公移山
太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，檔住去路，使他 和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎 樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鏊一個小丘的力量都沒有，怎 可能剷平太行、王屋二山昵？況且，鏊出的土石又丟到哪裏去昵？」
大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀 了，就是用盡你的氣力，也不能挖去山的一角昵？」
愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如昵！就算我死 了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有 一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大 力神揹走二山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong's way making it inconvenient for him and his family to get around.
One day yugong gathered his family together and said,’’Let's do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?"
All but his wife agreed with him.
"You don't have the strength to cut even a small mound,” muttered his wife. "How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will all the earth and rubble go?"
"Dump them into the Sea of Bohaii" said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea of Bohai.
Now Yugong's neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong sayingr"Aren't you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won't be able to remove even a corner of the mountain."
Yugong uttered a sigh and said,〃A biased person like you will never understand. You can't even compare with the widow's little boyl"
"Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
'''
if __name__ == '__main__':
    result = stats_text(text)
    print('统计参数中英文单词和中文汉字出现的次数 ==>\n',result)
