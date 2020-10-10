import pandas as pd
from underthesea import sentiment
from underthesea import classify




# file = "/home/duongth/personal/preprocess/git/preprocess_word/dataset/maybe_negative.csv"
#
# df = pd.read_csv(file)
#
# df['sentiment'] = df['data'].apply(sentiment)
#
# df.to_csv('maybe_negative_sentiment.csv')
#
#
# file = "/home/duongth/personal/preprocess/git/preprocess_word/dataset/unknown.csv"
#
# df = pd.read_csv(file)
#
# df['sentiment'] = df['data'].apply(sentiment)
predict = sentiment('hello world')
b = classify('Ủng hộ chính phủ')
print(b)
# df.to_csv('unknown.csv')