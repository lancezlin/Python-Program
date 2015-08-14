def longestWords(dictionary):
	dicDic = dict()
	for word in dictionary:
		dicDic[word] = len(word)
	longest = max(dicDic.values())
	longestWord = dicDic.keys()[dicDic.values().index(longest)]
	print longestWord
