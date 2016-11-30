
def calc_score(word):
    score = 0
    for char in word:
        score += score_dict[char]
    return score


def is_word_in_letters(word, letters):
    for char in word:
        if char in letters:
            letters = remove_char(letters, char)
        else:
            return False
    return True
        

def remove_char(word, char):
    position = word.find(char)
    return word[:position]+word[position+1:]

score_dict = {}
scores = [("eaionrtlsu", 1), ("dg", 2), ("bcmp", 3), ("fhvwy", 4), ("k", 5), ("jx", 8), ("qz", 10)]
for chars, score in scores:
    for ch in chars:
        score_dict[ch] = score
# print >> sys.stderr, score_dict
liste = []
n = int(raw_input())
for i in xrange(n):
    w = raw_input()
    liste.append(w)
letters = raw_input()

max_score = 0
max_word = None
for word in liste:
    if is_word_in_letters(word, letters):
        actual_score = calc_score(word)
        if actual_score > max_score:
            max_score = actual_score
            max_word = word

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print max_word
