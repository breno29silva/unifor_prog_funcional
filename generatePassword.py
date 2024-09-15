import string as st
import random

getLetters = st.ascii_letters
getDigits = st.digits
getPunctuation = st.punctuation

# Lambda
concatString = lambda x, y: x + y

partialElements = concatString(getLetters, getDigits)
allElements = concatString(partialElements, getPunctuation)
allElementsList = list(allElements)

def getRandomNumbers(size):
    # List Comprehension para gerar um array de números aleatórios
    return [random.randint(0, len(allElementsList) - 1) for _ in range(size)]

#Closure
def getPassword(size):
    random_numbers = getRandomNumbers(size)
    sortElements = list()
    def generatePassword():
        for i in random_numbers:
            sortElements.append(allElementsList[i])

        return sortElements

    return generatePassword

# Função de alta ordem
def joinList(func):
    return ''.join(map(str, func()))

def markPassword(password):
    print('Senha gerada: \033[1;4;32m' + password + '\033[m')


if __name__ == '__main__':
    print('Insira a quantidade de caracters que deseja sua senha:')
    number = int(input())

    getPasswordListFunc = getPassword(number)
    password = joinList(getPasswordListFunc)

    markPassword(password)