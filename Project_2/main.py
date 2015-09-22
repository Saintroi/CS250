from wordfrequency import WordFrequency
from wordcloud import WordCloud, HtmlWordCloud

def main(argv):                 #Given by Dr. Brown on Piazza
    argc = len(argv)

    if 2 > argc:
       print("More arguments, please.")
       return 1

    frequency = WordFrequency()
    for i in range(1, argc):
        frequency.open(argv[i])

    count = 23
    stop_words = ['A', 'An', 'And', 'But', 'That', 'The', 'Which',
                  'a', 'an', 'and', 'but', 'that', 'the', 'which']

    for count in [5, 20, 33, 50]:
        cloud = WordCloud(count, frequency, stop_words)
        cloud.save('cloud-{0}.txt'.format(count))

        cloud = HtmlWordCloud(count, frequency, stop_words)
        cloud.save('cloud-{0}.html'.format(count))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
