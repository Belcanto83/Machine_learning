import numpy as np
from scipy.spatial import distance
import re


# Читаем данные (строки с предложениями) из текстового файла
with open('Новый_текстовый_документ.txt', encoding='utf-8') as file:
    sentences = file.readlines()
print(sentences)
print(sentences[0])

words = []  # Создаем список всех слов предложений (НЕ уникальных)
listed_sentences = []  # Создаем список списков предложений (список предложений, разделенных по словам)
for sentence in sentences:
    sentence = sentence.lower()
    listed_sentence = re.split('[^a-z]+', sentence)
    try:
        listed_sentence.remove('')
    except ValueError:
        pass
    words += listed_sentence
    listed_sentences.append(listed_sentence)
print(words)

# Создаем УНИКАЛЬНЫЙ список всех слов всех предложений
unique_words = list(set(words))
# print(unique_words)
# print(len(unique_words))

# Создаем пустую матрицу необходимого нам размера n x m, где
# n - число предложений
# m - число уникальных слов во всех предложениях
matrix = np.array([[0]*len(unique_words)]*len(sentences))
# matrix[0, 0] = 15
# print(matrix)
# print(matrix.shape)

# Заполняем созданную пустую матрицу частотами встречаемости слов в предложениях
for j, word in enumerate(unique_words):
    for i, listed_sentence in enumerate(listed_sentences):
        frequency = listed_sentence.count(word)
        matrix[i, j] = frequency
print(matrix)

# Найдем косинусные расстояния от Первого предложения до всех остальных
cosine_distances = {}  # Пустой словарь, в который будем сохранять полученные косинусные расстояния
base_vector = matrix[0, :]  # Ищем похожие по смыслу
for i in range(len(sentences)):
    print(i, ':', sentences[i])
    vector = matrix[i, :]
    cosine_distance = distance.cosine(base_vector, vector)
    cosine_distances[i] = cosine_distance
result = cosine_distances

# Вывод результатов. Чем ближе косинусное расстояние к "0", тем выше ПРЕДПОЛАГАЕТСЯ совпадение по смыслу
# По факту результат получился НЕ совсем удовлетворительный, т.к. 3 и 4 найденные предложения уже не соотв. по смыслу!
print()
print('Result / cosine distance:')
print(result)
sorted_result = sorted(result, key=lambda n: result.get(n))
print('Result / cosine distance / sorted from MIN to max:')
print(sorted_result)
for i in sorted_result:
    print(f'{i} : {cosine_distances[i]} |', end=' ')
