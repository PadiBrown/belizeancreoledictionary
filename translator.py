import bzcreole

#print(bzcreole.creole_words)

sentence = input(f"give me a creole sentence")
#txt = "Whe de gwaan"

x = sentence.split()
for v in x:
	print(bzcreole.creole_words[v])






