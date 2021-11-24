from janome.tokenizer import Tokenizer

def wakati(text):
    text = text.replace('\n','') #改行を削除
    text = text.replace('\r','') #スペースを削除
    t = Tokenizer()
    result =t.tokenize(text)
    return result

words = wakati("さあ、お前の罪を数えろ")

for word in words:
  print(word)
