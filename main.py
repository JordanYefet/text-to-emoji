from emoji_translate.emoji_translate import Translator as emo_translator
from emoji import EMOJI_DATA
from googletrans import Translator
from bidi.algorithm import get_display

# GLOBALS
emoji_dict = {}


def SetEmjoiLocations(sentence: str) -> None:
    str_split = sentence.split(' ')
    for i, s in enumerate(str_split):
        if s in EMOJI_DATA:
            emoji_dict[i] = s


def main():
    while True:
        src_lang = input("Choose language Hebrew/English [(he)/(en)]: ")
        if src_lang in ["he", "en"]:
            break
        else:
            print("Try again.")
    sentence = input("Write your sentence:\n")
    if src_lang in "he":
        translator = Translator()
        sentence_he = sentence
        sentence = translator.translate(
            sentence, src='he', dest='en').text

    emo = emo_translator(exact_match_only=False,
                         randomize=True, exclude_stopwords=True)
    emo_sentence = emo.emojify(sentence)
    SetEmjoiLocations(emo_sentence)

    if not emoji_dict:
        print("No emojies have found in the text.")
    else:
        if src_lang in "he":
            sentence_split = sentence_he.split(' ')
        else:
            sentence_split = sentence.split(' ')
        for e in sorted(emoji_dict.items(), reverse=True):
            sentence_split.insert(e[0]+1, e[1])
        complete_sentence = ' '.join(map(str, sentence_split))

        if src_lang in "he":
            print(get_display(complete_sentence))
        else:
            print(complete_sentence)


if __name__ == "__main__":
    main()
