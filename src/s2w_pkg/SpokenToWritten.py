import string

def maps_generate():
  maps = {
          "numbers": {
              "zero": 0,
              "one" : 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9,
              "ten": 10,
              "eleven": 11,
              "twelve": 12,
              "thirteen": 13,
              "fourteen": 14,
              "fifteen": 15,
              "sixteen": 16,
              "seventeen": 17,
              "eighteen": 18,
              "nineteen": 19,
              "twenty": 20,
              "thirty": 30,
              "forty": 40,
              "fifty": 50,
              "sixty": 60,
              "seventy": 70,
              "eighty": 80,
              "ninety": 90
          },
          "multipliers": {
              "hundred": 100,
              "thousand": 1000
          },
          "currency": {
              "dollar": '$',
              "dollars": '$',
              "rupee": 'Rs.',
              "rupees": 'Rs.'
          },
          "counts": {
              "double": 2,
              "triple": 3,
              "quadruple": 4,
              "quintuple": 5
          }
  }
  return maps

def number_words():
  map = maps_generate()
  return list(map["numbers"].keys()) + list(map["multipliers"].keys()) + ["and"]

class spoken_to_written():

  def __init__(self):
    self.maps = maps_generate()
    self.number_words = number_words()
    self.input = ""
    self.output = ""

  def get_input(self):
    self.input = input("Please enter the spoken English text: ")[1:]
    if not self.input:
      raise ValueError("[Error]: You have not entered any text: ")

  def print_output(self):
    print("Spoken text: ", self.input)
    print("Written text: ", self.output)

  def short_form(self, input_string):
    j = 0
    result = ""
    para = input_string.split()
    for i, word in enumerate(para):
      if word.isupper() and not j:
        t = word
        j = 1
        while(para[i+j].isupper()):
          t += para[i+j]
          j += 1
          if j+i == len(para):
            break
        result += t + " "
      elif j:
        if word.islower():
          result += word + " "
        j -= 1
      else:
        result += word + " "
    return result

  def count_numbers(self, input_string):
    res = ""
    para = input_string.split()
    f = 0
    for i, word in enumerate(para):
      w = ''.join(word.lower().split('.')).split(',')[0]
      for case in self.maps:
        #print(w)
        if w in self.maps[case]:
          if case == "counts":
            n = ''.join(para[i+1].split('.')).split(',')[0]
            if n.isupper():
              res += n*self.maps[case][w] + " "
              f = 2
              break
          if case == "numbers":
            #print(w)
            n = ''.join(para[i+1].split('.')).split(',')[0]
            if n.lower() in self.maps["multipliers"]:
              res += str(self.maps["numbers"][w]*self.maps["multipliers"][n.lower()]) + " "
              f = 2
              break
            else:
              res += str(self.maps["numbers"][w]) + " "
              f = 1
              break
      if f == 0:
        res += word + " "
      else:
        f -= 1
    return res
    
  def currency(self, input_string):
    result = ""
    para = input_string.split()
    f = 0
    for i, word in enumerate(para):
      w = ''.join(word.lower().split('.')).split(',')[0]
      if word.isnumeric():
        n, t = para[i+1], ""
        if n[-1] in string.punctuation:
          t = n[-1]
        n = n[:-1]
        if n in self.maps['currency']:
          result += self.maps['currency'][n] + word + t + " "
          f = 2
      if f == 0:
        result += word + " "
      else:
          f -= 1
    return result

  def convert(self):
    self.output = self.short_form(self.input)
    self.output = self.count_numbers(self.output)
    self.output = self.currency(self.output)

def conversion():
  s2w = spoken_to_written()
  s2w.get_input()
  s2w.convert()
  s2w.print_output()
