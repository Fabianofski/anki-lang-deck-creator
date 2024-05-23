import os
import genanki 
import csv
from gtts import gTTS

vocabs_file = 'vocabs.csv'
target_language = 'pl'
anki_deck_name = 'Polish Cards'

anki_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{MyMedia}}',
    },
  ]
)

new_deck = genanki.Deck(
        237483247983748,
        anki_deck_name
)

media_files = []
os.makedirs('audio_files', exist_ok=True)
with open(vocabs_file, newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        file_name = row[1].lower().replace(' ', '') + '.wav'
        file_path = f"audio_files/{file_name}"

        output = gTTS(text=row[1], lang=target_language, slow=False)
        output.save(file_path)

        media_files.append(file_path) 

        print("Adding:", row[0], row[1])
        new_note = genanki.Note(
                    model=anki_model,
                    fields=[row[0], row[1], f"[sound:{file_name}]"]
                   )
        new_deck.add_note(new_note)

new_package = genanki.Package(new_deck)
new_package.media_files = media_files
new_package.write_to_file(f"{anki_deck_name.lower().replace(' ', '-')}.apkg")

## Clean up
for file in media_files:
    if os.path.exists(file):
        os.remove(file)

