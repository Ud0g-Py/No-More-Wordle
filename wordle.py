import re
import repo

words = repo.WORDS


def input_getChars(userInput):
    """
    Get user input and create a list without spaces
    """

    inputChars = [x for x in list(userInput) if x != ' ']

    return inputChars

def re_matchChars_good(words):
    """
    From a list of words, filter by matching words only
    """

    maybeWords = []

    # from a list, join every element to create a string used later to rex any word that contains EVERY character in the given string.
    readyChars = input_getChars(input("\n\033[32;1m[*]Introduce los caracteres VÁLIDOS, SEPARADOS POR UN ESPACIO y pulsa enter bb:\033[0m \n"))

    # Iterate until every positive word has been added, excluding others
    for word in words:
        for char in readyChars:
            if (char in word) and (char == readyChars[-1]):
                maybeWords.append(word)
            elif char not in word:
                break

    maybeWords = get_charPosition(readyChars, maybeWords)

    return maybeWords


def re_matchChars_bad(words):
    """
    From a list of words, filter by non-excluding words
    """

    maybeWords = []

    # from a list, join every element to create a string used later to rex any word that contains EVERY character in the given string.
    readyChars = ''.join(input_getChars(input("\n\033[31;1m[*]Introduce los caracteres NO válidos, SEPARADOS POR UN ESPACIO y pulsa enter bb:\033[0m\n")))
    
    # Iterate over a given list and append to a new list is the element hasn't any of the bad chars
    maybeWords = [x for x in words if not re.findall(f'["{readyChars}"]', x)]
             
    return maybeWords


def get_charPosition(readyChars, words):
    """
    From a list of words, and a list of needed chars, assures filter only good words with matchings characters in specific position inside a word.
    """

    charsPositions = {}

    maybeWords = []

    positions = []

    for char in readyChars:

        positions.append(int(input(f"\n\033[33;1m[*]Si sabes la posición de '{char}' introducela y pulsa enter (del 1 al 5). Si no la sabes, introduce 0:\033[0m\n")))

    for position in positions:

        key = readyChars[positions.index(position)]

        if position != 0:

            charsPositions[f'{key}'] = position -1

    # Switch to execute only if we know the exact position of at least 1 char
    if bool(charsPositions):  
           
        for word in words:

            for key, value in charsPositions.items():

                if (word[value] == (key)) and (key == list(charsPositions)[-1]):

                    maybeWords.append(word)

                elif (word[value] != (key)):

                    break
                
        return maybeWords

    else:

        return words

def print_result(words):

    print("\n\033[35;1m[*]Prueba con una de estas palabras y rueda de nuevo:\033[0m\n")
    print(*words, sep=' | ')

if __name__ == "__main__":

    print("""

                                                 ~::==~                                             
                                             ~:==oooooo=:                                           
                                       ~~:==ooooooooooooo==:~~                                      
                                    ~:=ooooooooooooooooooooooo:~                                    
                                   :oooooooooooooooooooooooooooo=:                                  
                                  =ooooooooooooooooooooooooooooooo=~                                
                                ~=ooooooooooooooooooooooooooooooooo=~                               
                               :=ooooooooooooooooooooooooooooooooooo=                               
                              =oooooooooooooooooooooooooooooooooooooo~                              
                             :ooooooooooooooooooooooooooooooooooooooo=                              
                             =oooooooooooooooooooooooooooooooooooooooo:                             
                             =oooooooooooooooooooooooooooooooooooooooo=                             
                            :ooooooooooooooooooooooooooooooooooooooooo=                             
                            :ooooooooooooooooooooooooooooooooooooooooo=                             
                            :ooooooooooooooooooooooooooooooooooooooooo=                             
                            ~ooo: ~:=oooooooooooooooooooooooooo=:~~~oo=                             
                        ~~~ ~ooo:    ~:=oooooooooooooooooooo==~    ~oo=  ~~~                        
                     ~~:=oo~ =oo=       ~:==ooooooooooooo=:~~      :oo: :oo=:~~                     
                    :~=oooo= :ooo:          ~~::=ooo::~~          :=oo: :oooo:~:                    
                   ~= :oooo= ~oooo:            ~=ooo:            :oooo~ =oooo: =~                   
                   ~o=~~:=oo~ =oooo=:~~   ~~::=oooooo=::~~~   ~:=oooo= ~oo=:~~=o~                   
                    =oo=:~~:~ :oooooooo=ooooooooooooooooooooooooooooo: ::~~:==o=                    
                    ~=ooo==:~~ ~:===oooooooooooooooooooooooooooo===::  ~:==ooo=~                    
                      ==oooooo==:~~~~:==ooooooooooooooooooooo::~~~~::=ooooooo=                      
                       :=oooooooo===:~ ~ooooooooo=:::~:ooooo~ ~:===oooooooo=:                       
                      ~==ooooooo=~ ~:o~ :ooooo=:~     ~oooo: ~o=~  =ooooooo==:                      
                      ~ooooooooo=:  ~o=  =oooo=====:::=ooo=  =o:  ~=ooooooooo~                      
                       =oooooooo=o==ooo: ~ooooooooooooooo=~ :ooo==oooooooooo=                       
                       ~=ooooooooooooooo~ :oooooooooooooo: :ooooooooooooooo=~                       
                        ~=ooooooooooooooo~ =oooooooooooo: ~ooooooooooooooo=~                        
                          :oooooooooooooo=~ ~=ooooooooo: ~=oooooooooooooo:                          
                           ~:oooooooooooooo~  ~:==oo=:~ ~ooooooooooooo=:~                           
                             ~:=ooooooooooo=:          :oooooooooooo=:~                             
                                ~:=oooooooooo:        :oooooooooo=:~                                
                                   ~~:==oooooo=~    ~=oooooo==:~                                    
                                         ~~::::=~  ~:=:::~~ 


     ███▄    █  ▒█████      ███▄ ▄███▓ ▒█████   ██▀███  ▓█████     █     █░ ▒█████   ██▀███  ▓█████▄  ██▓    ▓█████ 
     ██ ▀█   █ ▒██▒  ██▒   ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀    ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓█   ▀ 
    ▓██  ▀█ ██▒▒██░  ██▒   ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▒███      ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒███   
    ▓██▒  ▐▌██▒▒██   ██░   ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ▒▓█  ▄    ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ▒▓█  ▄ 
    ▒██░   ▓██░░ ████▓▒░   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░▒████▒   ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░▒████▒
    ░ ▒░   ▒ ▒ ░ ▒░▒░▒░    ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░
    ░ ░░   ░ ▒░  ░ ▒ ▒░    ░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░     ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░
       ░   ░ ░ ░ ░ ░ ▒     ░      ░   ░ ░ ░ ▒    ░░   ░    ░        ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░      ░   
         ░     ░ ░            ░       ░ ░     ░        ░  ░       ░        ░ ░     ░        ░        ░  ░   ░  ░
                                                                                         ░                     
""")

    words = list(dict.fromkeys(words))

    while (len(words)) != 0:

        words = re_matchChars_bad(words)

        words = re_matchChars_good(words)

        print_result(words)


