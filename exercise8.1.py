
text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
text = text.lower().replace(",", "").replace(".", "").split()


counts = {}
for words in text:
    counts[words] = counts.get(words, 0) + 1

for key1, value1 in counts.items():
    print(f"{key1}: {value1}")

repeated_word = ""
max_count = 0

for word, count in counts.items():
    if count > max_count:
        max_count = count
        repeated_word = word

print(f"ყველაზე ხშირი: '{repeated_word}' ({max_count}-ჯერ)")

print(f"სხვადასხვა სიტყვა: {len(counts)}")