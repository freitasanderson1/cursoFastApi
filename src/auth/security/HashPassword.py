from hashlib import sha256

class HashPassword:
  def compair(self, password: str, hashed_password: str) -> bool:
    return self.hash(password) == hashed_password
  
  def hash(self, password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()
