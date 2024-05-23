# ANKI Language Deck Creator

This is a simple script created in python to generate a package for Anki from a csv file. It uses Google TTS to generate audio files for better language learning.

## How to use

1. Install python on your machine by following the instructions [here](https://www.python.org/downloads/).
2. Download the zip file from this repository or clone the repository using the following command:

```bash
git clone https://github.com/Fabianofski/anki-lang-deck-creator
```

3. Open a terminal and navigate to the folder where the script is located using the following command:

```bash
cd path/to/folder
```

4. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

5. Create a csv file with the following columns:

  | Base Language | Target Language |
  | ------------- | --------------- |
  | word1         | translation1    |
  | word2         | translation2    |
  | word3         | translation3    |
  | ...           | ...             |

  An example of the csv format is available [here](./vocabs.csv).  
  You can use ChatGPT to generate a list of words in your target language.

6. Update the variables in [main.py](./main.py)

- 'vocabs_file': the path to the csv file
- 'target_language': the target language code (e.g. 'fr' for French)
- 'anki_deck_name': the name of the Anki Deck

7. Run the script using the following command:

```bash
python main.py
```

8. The script will generate a package with the name 'anki_deck_name'. You can import this package into Anki and start learning your target language!

## Supported Language Codes

| Language Code | Language Name             |
| ------------- | ------------------------- |
| af            | Afrikaans                 |
| ar            | Arabic                    |
| bg            | Bulgarian                 |
| bn            | Bengali                   |
| bs            | Bosnian                   |
| ca            | Catalan                   |
| cs            | Czech                     |
| cy            | Welsh                     |
| da            | Danish                    |
| de            | German                    |
| el            | Greek                     |
| en            | English                   |
| eo            | Esperanto                 |
| es            | Spanish                   |
| et            | Estonian                  |
| fi            | Finnish                   |
| fr            | French                    |
| gu            | Gujarati                  |
| hi            | Hindi                     |
| hr            | Croatian                  |
| hu            | Hungarian                 |
| hy            | Armenian                  |
| id            | Indonesian                |
| is            | Icelandic                 |
| it            | Italian                   |
| iw            | Hebrew                    |
| ja            | Japanese                  |
| jw            | Javanese                  |
| km            | Khmer                     |
| kn            | Kannada                   |
| ko            | Korean                    |
| la            | Latin                     |
| lv            | Latvian                   |
| mk            | Macedonian                |
| ms            | Malay                     |
| ml            | Malayalam                 |
| mr            | Marathi                   |
| my            | Myanmar (Burmese)         |
| ne            | Nepali                    |
| nl            | Dutch                     |
| no            | Norwegian                 |
| pl            | Polish                    |
| pt            | Portuguese                |
| ro            | Romanian                  |
| ru            | Russian                   |
| si            | Sinhala                   |
| sk            | Slovak                    |
| sq            | Albanian                  |
| sr            | Serbian                   |
| su            | Sundanese                 |
| sv            | Swedish                   |
| sw            | Swahili                   |
| ta            | Tamil                     |
| te            | Telugu                    |
| th            | Thai                      |
| tl            | Filipino                  |
| tr            | Turkish                   |
| uk            | Ukrainian                 |
| ur            | Urdu                      |
| vi            | Vietnamese                |
| zh-CN         | Chinese                   |
| zh-TW         | Chinese (Mandarin/Taiwan) |
| zh            | Chinese (Mandarin)        |

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
