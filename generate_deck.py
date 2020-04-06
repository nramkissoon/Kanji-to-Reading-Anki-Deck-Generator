import genanki
import csv

deck_id_file = open('./deck_id.txt', 'r')
deck_id = deck_id_file.read()
deck_id_file.close()

model_id_file = open('./model_id.txt', 'r')
model_id = model_id_file.read()
model_id_file.close()

new_deck = genanki.Deck(
  int(deck_id),
  '6k_Vocabulary_Kanji_to_Reading'
)

note_model = genanki.Model(
  int(model_id),
  'Card Model',
  fields=[
      {'name': 'Vocabulary-Kanji'},
      {'name': 'Vocabulary-Furigana'},
      {'name': 'Vocabulary-Kana'}, 
      {'name': 'Vocabulary-English'},
      {'name': 'Vocabulary-Pos'},
      {'name': 'Expression'},
      {'name': 'Reading'},
      {'name': 'Sentence-Kana'},
      {'name': 'Sentence-English'},
      {'name': 'Sentence-Clozed'},
  ], 
  templates=[
    {
      'name': 'Japanese Kanji to Reading/Definition Card',
      'qfmt': 
      '''
        <span style="font-size: 28px;">{{Vocabulary-Kanji}}</span>
        <span style="font-size: 15px; color: #55555ff">{{Vocabulary-Pos}}</span><br>
        <span style="font-family: MS ゴシック; font-size: 32px;">{{Expression}}</span><br>
      ''',
      'afmt': 
      '''
        {{FrontSide}}
        <hr id="answer">
        {{Vocabulary-Kana}}<br>
        {{Vocabulary-English}}<br><br>
        <span style="font-family: MS ゴシック;">{{furigana:Reading}}</span><br> 
      '''
    }
  ],
  css=".card { font-family: arial; font-size: 20px; text-align: center; color: white; background-color: black; }"
)

notes = []
with open('./data/parsed_data.csv', newline='') as data:
  reader = csv.reader(data, delimiter=',')
  next_line = reader.__next__() 
  while True:
    try:
      next_line = reader.__next__()
      fields = [field for field in next_line];
      notes.append(genanki.Note(model=note_model, fields=fields))
    except StopIteration:
      break;

for note in notes:
  new_deck.add_note(note)

genanki.Package(new_deck).write_to_file('./data/6k_Vocabulary_Kanji_to_Reading.apkg')