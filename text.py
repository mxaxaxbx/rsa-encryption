# external libs
import rsa
# py libs
import sys
import os
import base64

class Encryptor:

  def __init__(self):
    self.validate_args()

  def validate_args(self):
    try:
      if len(sys.argv) < 2:
        raise Exception("No arguments")

      if sys.argv[1] == "get_key":
        self.generate_keys()
        print("Keys generated")
        return

      elif sys.argv[1] == 'encrypt':
        if len(sys.argv) != 3:
          print("USAGE: ")
          print("ENCRYPT MESSAGE")
          print("python main.py encrypt message")
          return
        self.encrypt(sys.argv[2])
        return
      
      elif sys.argv[1] == 'decrypt':
        if len(sys.argv) != 3:
          print("USAGE: ")
          print("DECRYPT MESSAGE")
          print("python main.py decrypt ciphertext")
          return
        self.decrypt(sys.argv[2])
        return

      else:
        print("USAGE: ")
        print("GET KEY")
        print("python3 main.py get_key")
        print("ENCRYPT MESSAGE")
        print("python main.py encrypt message")
        print("DECRYPT MESSAGE")
        print("python main.py decrypt ciphertext")

    except:
      print("USAGE: ")
      print("GENERATE KEYS")
      print("python3 main.py get_key")
      print("ENCODE MESSAGE")
      print("python main.py encrypt message")
      print("DECRYPT MESSAGE")
      print("python main.py decrypt ciphertext")
      sys.exit(1)

  def encrypt(self, message):
    try:
      p_key, _ = self.get_keys()
      # to bytes
      cipher = rsa.encrypt(message.encode(), p_key)
      # bytes to string
      ciphertext = base64.b64encode(cipher).decode()
      print(ciphertext)
    except Exception as e:
      print(e)

  def decrypt(self, ciphertext):
    try:
      _, private = self.get_keys()
      # to bytes
      cipher = base64.b64decode(ciphertext)
      message = rsa.decrypt(cipher, private).decode()
      print(message)
    except Exception as e:
      print(e)

  def check_keys(self):
    if not os.path.exists("/tmp/public.key"):
      print("Public key not found")
    if not os.path.exists("/tmp/private.key"):
      print("Private key not found")

  def generate_keys(self):
    (public, private) = rsa.newkeys(1024)
    with open("/tmp/public.key", "wb") as f:
      f.write(public.save_pkcs1())
    with open("/tmp/private.key", "wb") as f:
      f.write(private.save_pkcs1())

  def get_keys(self):
    try:
      with open("/tmp/public.key", "rb") as f:
        public = rsa.PublicKey.load_pkcs1(f.read())
      with open("/tmp/private.key", "rb") as f:
        private = rsa.PrivateKey.load_pkcs1(f.read())

      return public, private
    except:
      raise Exception("Keys not found")

if __name__ == "__main__":
  Encryptor()
