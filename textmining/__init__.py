from textmining.model import SamsungReport

if __name__ == '__main__':
    sam = SamsungReport()
    #sam.download()
    #print(sam.extract_noun());
    print(sam.remove_stopword());