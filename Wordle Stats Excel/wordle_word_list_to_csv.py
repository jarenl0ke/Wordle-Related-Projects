import csv
from os import listdir

def wordle_list_to_csv(list, file):
  f = open(file, "w", newline="")
  writer = csv.writer(f)
  for word in list:
    writer.writerow([word])
  f.close()

def wordle_words_list(file):

  all_words = []
  wordle_words = []

  with open(file, "r") as words:
    all_words = words.read().split()

  for word in all_words:
    word = word.strip().replace('"', '')
    wordle_words.append(word.replace(",", ""))
  
  wordle_words.sort()

  return wordle_words  

if __name__ == "__main__":
  inFile = input("Txt file path: ")
  list =  wordle_words_list(inFile)

  outFile = input("CSV file output path: ")
  wordle_list_to_csv(list, outFile)