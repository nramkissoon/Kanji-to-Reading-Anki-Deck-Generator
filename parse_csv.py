import csv

parsed_data = open('./data/parsed_data.csv', 'w', newline='')
writer = csv.writer(parsed_data, delimiter=',')
writer.writerow(['Vocabulary-Kanji', 'Vocabulary-Furigana', 'Vocabulary-Kana', 'Vocabulary-English', 'Vocabulary-Pos', 'Expression', 'Reading', 'Sentence-Kana', 'Sentence-English', 'Sentence-Clozed'])


with open('./data/Core_2k6k_Optimized_Japanese_Vocabulary.csv', newline='') as data:
  reader = csv.reader(data, delimiter=',')
  next_line = reader.__next__() # discard first line that contains table headers
  while True:
    try:
      next_line = reader.__next__()
      next_line = [ next_line[i] for i in range(len(next_line)) if i in [1, 2, 3, 4, 6, 8, 9, 10, 11, 12] ]
      writer.writerow(next_line)
    except StopIteration:
      break;

print("DONE")
parsed_data.close()

