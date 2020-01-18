import pandas as pd
from pymystem3 import Mystem

data = pd.DataFrame({
    'keyword': ['курс гривны к рублю', 'доллары в рубли', '100 долларов в рублях', 'курс рубля'],
    'shows': [125076, 114173, 97534, 53546],
})


def does_lemmas(row):
    m = Mystem()
    lemmas = m.lemmatize(row)
    return ''.join(lemmas)


data['lemmas'] = data['keyword'].apply(does_lemmas)
print(data)
