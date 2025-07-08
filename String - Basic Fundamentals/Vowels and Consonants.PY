# Enter your code here. Read input from STDIN. Print output to STDOUT
text = input()
n = text.lower()
vowels = 0
consonants = 0
for i in range(len(n)):
    if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u' :
        vowels += 1
    else:
        consonants += 1

print(vowels,consonants)