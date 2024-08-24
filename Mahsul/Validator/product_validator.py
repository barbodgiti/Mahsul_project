import re

def new_validator(mhsl):
   return bool(re.match(r"^[A-Za-z\s]{2,20}$", mhsl))