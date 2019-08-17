import gensim
# Download vector file from https://fasttext.cc/docs/en/english-vectors.html
model = gensim.models.KeyedVectors.load_word2vec_format('wiki-news-300d-1M.vec')


def main():
    input_word = input("Enter the word: ")
    while input_word.lower() != 'q':
        try:
            similar = model.most_similar(positive=[input_word], topn=5)
            print("{0}  :{1}".format("Word", "Similarity"))
            for word, similarity in similar:
                print("{0}  :{1}".format(word, similarity))
            input_word = input("Enter another word : ")
        except:
            print("{0} word not found in the vector".format(input_word))
            input_word = input("Enter another word : ")


if __name__ == "__main__":
    main()
