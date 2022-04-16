# external libs
from cryptography.fernet import Fernet
# py libs
import sys

class Encryptor:

  def __init__(self):
    self.key = Fernet.generate_key()
    self.validate_args()
  
  def validate_args(self):
    try:
      if len(sys.argv) < 2:
        raise Exception("No arguments")

      if sys.argv[1] == "get_key":
        print(self.key.decode("utf-8"))
        sys.exit(1)
      
      elif sys.argv[1] == 'encrypt':
        if len(sys.argv) != 4:
          print("USAGE: ")
          print("ENCRYPT FILE")
          print("python main.py encrypt <input_file> key")
          sys.exit(1)
        self.validate_file(sys.argv[2])
        key = sys.argv[3]
        self.encrypt(sys.argv[2], key)
        sys.exit(1)
      
      elif sys.argv[1] == 'decrypt':
        if len(sys.argv) != 4:
          print("USAGE: ")
          print("DECRYPT FILE")
          print("python main.py decrypt <input_file> key")
          sys.exit(1)
        self.validate_file(sys.argv[2])
        key = sys.argv[3]
        self.decrypt(sys.argv[2], key)
        sys.exit(1)
      
      else:
        print("USAGE: ")
        print("GET KEY")
        print("python3 main.py get_key")
        print("ENCRYPT FILE")
        print("python main.py encrypt <input_file> key")
        print("DECRYPT FILE")
        print("python main.py decrypt <input_file> key")
      
      sys.exit(1)

    except Exception as e:
      print("USAGE: ")
      print("GET KEY")
      print("python3 main.py get_key")
      print("ENCRYPT FILE")
      print("python main.py encrypt <input_file> key")
      print("DECRYPT FILE")
      print("python main.py decrypt <input_file> key")
    
  def validate_file(self, file):
    try:
      with open(file, "rb") as f:
        f.read()
    except FileNotFoundError:
      print("File not found")
      sys.exit(1)

  def encrypt(self, file, key):
    with open(file, "rb") as f:
      data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    filename = file + ".encrypted"
    with open(filename, "wb") as f:
      f.write(encrypted)
    print("File encrypted {}".format(filename))

  def decrypt(self, file, key):
    try:
      with open(file, "rb") as f:
        data = f.read()
      fernet = Fernet(key)
      decrypted = fernet.decrypt(data)
      filename = file.replace(".encrypted", "")
      with open(filename, "wb") as f:
        f.write(decrypted)
      print("File decrypted {}".format(filename))
    except Exception as e:
      print("Error decrypting file", e)
      sys.exit(1)


if __name__ == "__main__":
  Encryptor()
