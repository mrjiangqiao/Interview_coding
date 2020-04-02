import re
import math
def matchfunc(relpace_word):
	def replace(m):
		text = m.group()
		lenflg = len(text)
		return relpace_word*lenflg
	return replace
a =int(input().strip())
word_list = []
for i in range(a):
	cur_word = str(input().strip())
	word_list.append(cur_word)
sentence = input()
result_sentence = re.sub("|".join(word_list), matchfunc("*"), sentence, flags=re.I)
print(result_sentence)