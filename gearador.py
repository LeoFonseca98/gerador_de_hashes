import hashlib
 
string = input("Digite o texto a ser  gerado a hash: ")

menu = int(input(''' \t MENU \n ESCOLHA O TIPO DE HASH 
  [1]\t MD5
  [2]\t SHA1
  [3]\t SHA256
  [4]\t SHA512
Digite o número do hash a ser gerado: '''))


if menu == 1:
    resultado = hashlib.md5(string.encode('UTF-8'))
    print('A hash MD5 da string: ', string, ' é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('UTF-8'))
    print('A hash SHA1 da string: ', string, ' é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('UTF-8'))
    print('A hash SHA256 da string: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('UTF-8'))
    print('A hash SHA512 da string: ', string, 'é: ', resultado.hexdigest())
else:
    print("ERROR")