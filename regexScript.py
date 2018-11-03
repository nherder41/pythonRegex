import argparse
import re

parser = argparse.ArgumentParser(description="Match patters of files using regex")

parser.add_argument("-s", "--regex", metavar="", type=str, required=True, help="regex to find")

parser.add_argument("-f", "--file", type=str, metavar="", required=True, help="file to search")

parser.add_argument("-r", "--replace", type=str, metavar="", required=False, help="replacement string")
args = parser.parse_args()


#@ regex - python regular expression
#@ file - path to file to search
#return a list of strings
#return a list of regex patterns found in a specific file
def search(regex, file):
    results = []

    with open(file, "r") as searchFile:
        for line in searchFile:
            results.append(re.search(regex, line))
        print(results)

#@ regex - python regular expression
#@ file - path to file to search
#@ replace - replacement for found item
#this method is a find and replace on a specified file using regex
#def search_and_replace(regex, file, file2):

if __name__ == '__main__':

    if args.replace is None:
        search(args.regex, args.file)
    # else:
    #     search_and_replace(args.regex, args.file, args.replace)
