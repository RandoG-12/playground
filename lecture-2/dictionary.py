words = {"cat": "die Katze", "dog": "der Hund"}

print(words["cat"])
print("\n\n")

#add 
words["bear"] = "der Bär"

for i in words:
    print(f"{i}\t {words[i]}")
print("\n\n")
