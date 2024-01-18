import argparse
parser = argparse.ArgumentParser(description = 'Replacing the letter in a given poem')
parser.add_argument('-l','--letter', help = 'Enter which letter should be replaced', required = True)
parser.add_argument('-s', '--symbol', help = 'Enter with what you would like to replace the chosen letter', required = True)
parser.add_argument('--upper_case', action="store_true", help = 'Capitalises the poem')

def read_poem(poem):
    poem_file = open(poem, encoding='utf-8')
    content = poem_file.read()
    return content 
    poem_file.close()

def create_output_file(poem_content):
    with open('output_file.txt', mode = 'w', encoding='utf-8') as output_file:
        output_file.write(poem_content)

def replace_letter(letter, symbol, upper_case = False):
    poem_file = "poem.txt" 
    poem_content = read_poem(poem_file)    
    
    if upper_case: 
        return poem_content.capitalize()
    
    if letter in poem_content:
        return poem_content.replace(letter, symbol)
    
    create_output_file(poem_file)

args = parser.parse_args()
print(replace_letter(args.letter, args.symbol))