def count_each_char(contents):
    alphabet = {}
    character = ""
    #split contents into words
    words = contents.split()
    for word in words:
        # look at each word individually
        for i in range(len(word)):
            character = word[i].lower()
            # Make sure we're dealing with letters
            if character.isalpha():
                # look at each character individually
                if character not in alphabet.keys():
                    alphabet[character] = 1
                else:
                    alphabet[character] += 1
    return alphabet


def finalized_report(contents):
    ordered = {}

    # Beginning of report
    report_string = "--- Begin report of books/frankenstein.txt ---\n"

    # General information regarding total words in document
    report_string += f"{count_words(contents)} words found in the document\n\n"

    # Begin printing information regarding character count, but should be ordered most -> least
    # Unordered dictionary:
    count_of_characters = count_each_char(contents)

    ordered = ordered_dictionary(count_of_characters)

    for key in ordered:
        report_string += f"The '{key}' character was found {ordered[key]} times \n"
    report_string += "--- End report ---"


    return report_string
            
# Return an ordered version of the dictionary
def ordered_dictionary(dict):
    copy_dict = dict.copy()
    return_dict = {}

    #Set to the character 
    max_key_so_far = ''

    # While we have values in copy_dict:
    while len(copy_dict) > 0:
        #reset max_so_far
        max_so_far = float("-inf")

        # Run through the characters in copy_dict:
        for key in copy_dict:
          # if a characters count is greater than 
            if copy_dict[key] > max_so_far:
                # Set max_so_far
                max_so_far = copy_dict[key]
                # Set the greatest value character
                max_key_so_far = key
        
        # Values should be set, so remove them from copy_dict and add them to new_dict
        return_dict[max_key_so_far] = max_so_far
        del copy_dict[max_key_so_far]
    return return_dict



def count_words(contents):
    counter = 0
    words = contents.split()
    for word in words:
        counter += 1   
    return counter

def main():
    # nit: hold path in a var
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        # 14. Count total words
        # print(count_words(file_contents))
        # 15. Count Letters
        # print(count_each_char(file_contents))

        # 16. Print a Report
        print(finalized_report(file_contents))
    


main()