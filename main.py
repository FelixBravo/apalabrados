from sqlalchemy.orm.exc import NoResultFound
import re
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

from modelo import Numero, Texto, Caracter
from base import Base, engine, Session

def main(userInput, option):
    Base.metadata.create_all(engine)
    session = Session()

    if (option == 1):
        userInput = int(userInput)
        try:
            obj = session.query(Numero.acumulado).order_by(Numero.id.desc()).first()
            if obj != None:
                #print(type(obj))
                currentAcumulate = str(getattr(obj, 'acumulado'))
                #print(currentAcumulate)
                newAcumulate = int(currentAcumulate) + userInput
                print('Loading Number {} into DB'.format(userInput))
                number = Numero(userInput, newAcumulate)
                session.add(number)

        except NoResultFound:
            print('BD without data')

        if obj == None:
            newAcumulate = userInput
            print('Loading First Number {} into DB'.format(userInput))
            number = Numero(userInput, newAcumulate)
            session.add(number)

    if (option == 2):
        print('Loading Texto {} into DB'.format(userInput))
        firstChar = userInput[0]
        lastChar = userInput[-1]
        #print('{} {}'.format(firstChar, lastChar))
        texto = Texto(userInput, firstChar, lastChar)
        session.add(texto)

    if (option == 3):
        for c in userInput:
            print('Loading Character {} into DB'.format(c))
            character = Caracter(c)
            session.add(character)


    session.commit()
    session.close()


def has_special_char(charInput):
    special_characters = "!@#$%^&*()'-+?_=,<>/.;:`~[]"
    if any(c in special_characters for c in charInput):
        return True
    else:
        return False


if __name__ == '__main__':
    num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
    userInput = input("Enter something: ") 

    isnumber = re.match(num_format,userInput)
    if isnumber:
        print ('given string is number ', userInput)
        main(userInput, 1)

    else:
        i = 0
        specialCharList = []
        for char in str(userInput):
            if has_special_char(char):
                #print('char finded ' + char)
                specialCharList.append(char)
                i = i + 1
                
        print('i == ', i)
        if i == 0 :
            print('Es un string Limpio ' + userInput)
            main(userInput, 2)
        else:
            characteres = []
            print('Es un string con caracteres especiales')
            for c in specialCharList:
                characteres.append(c)
            main(characteres, 3)




