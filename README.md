## About
This application cleans text by removing stopwords and blacklisted words, allowing these texts to be used in artificial intelligence applications and natural language processing.

### Install Requirements
```bash
pip install -r requirements.txt
```

#### Requirements
- Python 3.x
- nltk library
- pandas library
- tqdm library
- enchant library

### How To Run
```bash
python main.py
```

### Settings
```python
# main.py

class CleanData(App):
    index = 'comment' #The name of the table that will be cleaned
    input_csv_file_path = 'data.csv' # Name of the file to be played
    output_csv_file_path = 'cleaned_data.csv' # The name of the file where the changes will be saved

```
You can add words to the blacklist and put a space between each word to be deleted from the text
```txt
# blacklist.txt
game commit hello
```
  

## Note

Please make sure to use this application responsibly according to local and global data protection laws and policies.
