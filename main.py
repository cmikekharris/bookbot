def main():
    print("--- Begin report of books/frankenstein.txt ---");

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = len(file_contents.split())
    print(f"{word_count} words found in the document")

    file_contents_to_lower = file_contents.lower()

    letter_counts = {}

    for i in range(len(file_contents_to_lower)):
        if(file_contents_to_lower[i] not in letter_counts):
            letter_counts[file_contents_to_lower[i]] = 1
        else:
            letter_counts[file_contents_to_lower[i]] += 1

    letter_counts_list = []

    for l in letter_counts:
        if(l.isalpha()):
            temp = {"name" : l, "num": letter_counts[l]}
            letter_counts_list.append(temp)

    letter_counts_list.sort(reverse=True, key=sort_on)

    for row in letter_counts_list:
        print(f"The '{row["name"]}' character was found {row["num"]} times")

def sort_on(dict):
    return dict["num"]

main()
