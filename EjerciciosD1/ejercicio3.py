def words_counter(word : str) -> int:
    separate_word = word.split(" ")
    return len(separate_word)

if __name__ == "__main__":
    word = input("Digite una Oracion: ")
    word_count = words_counter(word)
    print(f"There is {word_count} words in total.")