import nltk
import re
from resourse import*
def questKeys(ask):
  words = list(set(ask.lower().split(" ")))
  filtered_words = []
  for word in words:
    if word not in stop_words:
      filtered_words.append(word)
  return filtered_words

def blockSpeach(que):
	lowerq = que.lower()
	if lowerq in block_answer:
		if True:
			return print(block_answer[lowerq])
	return "0"

def lastOpp(line):
  keys = line.lower().split(" ")
  after_effect = ""
  for key in keys:
    if (key in reflections):
      after_effect += (reflections[key] + " ")
    else:
      after_effect += (key + " ")
  after_effect += ", what ?"
  return print( after_effect )


def response(que):
	if blockSpeach(que) == "0":
		keywords = questKeys(que)
		for word in keywords:
			for x in possible_answer:
				keys = questKeys(x)
				for key in keys:
					if key == word:
						return print(possible_answer[x])
		return lastOpp(que)



def chatBot():
	print("Hi, I'm Magnom and I chat alot ;)\nPlease type lowercase English language to start a conversation.\nType quit or bye to leave ")
	user_input =''
	while True:
		try:
			user_input = input(">")
		except EOFError:
			print(user_input)
		if (user_input == "bye") or (user_input == "quit" ):
			print("BBye take care. See you soon :) ")
			break
		else:
			response(user_input)
    


if __name__ == "__main__":
    chatBot()