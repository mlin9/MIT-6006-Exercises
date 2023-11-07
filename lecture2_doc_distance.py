from collections import Counter
import math
import time
import operator

word_dict1 = Counter()
word_dict2 = Counter()

product = dict()
common_words = dict()
word_dict1_sq = dict()
word_dict2_sq = dict()

doc1 = ""
doc2 = ""

def word_split_1(array):

  if len(array) < 2:
    return
  
  mid = int(len(array) / 2)
  split = array[mid] == " "

  if not split:
    for x in range(mid, len(array)):
      split = array[x] == " "
      if split:
        mid = x
        break
  if not split:
    for x in range(0, mid):
      split = array[x] == " "
      if split:
        mid = x
        break
      
  if split:
    word_split_1(array[0:mid])
    word_split_1(array[mid+1:len(array)])
  else:
    word_dict1[str(array)] += 1

def word_split_2(array):

  if len(array) < 2:
    return
  
  mid = int(len(array) / 2)
  split = array[mid] == " "

  if not split:
    for x in range(mid, len(array)):
      split = array[x] == " "
      if split:
        mid = x
        break
  if not split:
    for x in range(0, mid):
      split = array[x] == " "
      if split:
        mid = x
        break
   
  if split:
    word_split_2(array[0:mid])
    word_split_2(array[mid+1:len(array)])
  else:
    word_dict2[str(array)] += 1

def dict_sum(input_dict):
  
  result = 0
  
  for key, value in input_dict.items():
    result += int(input_dict[key])

  return result
    

def calculate_angle():

  for key, value in word_dict1.items():
    if key in word_dict2:
      product[key] = int(word_dict1[key]) * int(word_dict2[key])

  for key, value in word_dict1.items():
    word_dict1_sq[key] = int(word_dict1[key]) * int(word_dict1[key])

  for key, value in word_dict2.items():
    word_dict2_sq[key] = int(word_dict2[key]) * int(word_dict2[key])

  magnitude_dict1 = math.sqrt(dict_sum(word_dict1_sq))
  magnitude_dict2 = math.sqrt(dict_sum(word_dict2_sq))
  
  dot_product = dict_sum(product)/(magnitude_dict1 * magnitude_dict2)

  return math.degrees(math.acos(dot_product))

def main():
  filename_1 = "lecture2_doc1.txt"
  filename_2 = "lecture2_doc2.txt"

  with open(filename_1, encoding="utf8") as iofile:
    doc1 = iofile.read()
  
  with open(filename_2, encoding="utf8") as iofile:
    doc2 = iofile.read()

  start_time = time.time() * 1000
  word_split_1(doc1)
  word_split_2(doc2)
  
  print ("The document distance is %s degrees" % calculate_angle())
  end_time = time.time() * 1000
  print ("Time elapsed: %s milliseconds" % (end_time - start_time))
  input("Press return to exit...")

main()
