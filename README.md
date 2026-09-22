\#  Inventory-record




\###  History

Christian Bermeo a civil engineer working with contracts full of documents, fiscalization, administration and so on. 
All contracts need a complex path of documents to make the projects done.


### What does this repo do?

- Track documents 
- Measure these documents
- Test and consistensy-check of documents

* Make/Write reports and documents as result
* We have 629 file so far and making more



\*\*Read-only by design:\*\* the tool never modifies the archive it measures,

and its reports never enter this repo (see `.gitignore`) — institutional

data stays out of Git





\### What does this repo need?

* pathlib/ rglob
* stat()
* with open(....)
* f-strings for reports


### We have incorporated a IA Layer, a API call.
\#what does this call need.
1. Keep your key on secret
we created a .streamlit folder and inside the key
.streamlit\secrets.toml"
inside we have
ANTHROPIC_API_KEY = "your-API-key"
Inside .gitignore we have this path .streamlit\secrets.toml and here we are totally secure

### We have a client window (Streamlit)
\ what does it need?

1. streamlit run app.py
2. Its need some requirements. pip install -r requirements.txt
3. requirements.txt comes from -freeze

### when using streamlit be careful of versions
1. For that reason we create an python ENV.

### Finaly we have a csv document.
### What does it have?
six columns

date,n_files,n_directories,n_elements,total_mb,n_unclassified
date: date time format 2026-08-26
n_files: counts every file in the folder
n_directory: counts directories
n_elements: nfiles + n_directories
total_mb: using stat().st_size we measure the size of all files within the directory
n_unclasified: get neither files nor directories

Instrument log (read this before interpreting jumps in the series):
- empty cell = not measured that day; 0 = measured, none found
- 2026-08-26: the census started counting elements that answer neither
  is_file() nor is_dir() (long-path items). Before this date the column is
  empty because it was not measured, not because there were none.

- 2026-09-07:
 - For that the number of docs have increased considerably, but not for the reason of high productivity , but we have documents that we haven't seen
 - we have expanded the windows long path therefore since here we have zero (0) n_unclassified because all files done.
