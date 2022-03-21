import uuid

def get_random_postfix():
   return str(uuid.uuid4())[:10].replace('-','').lower()
