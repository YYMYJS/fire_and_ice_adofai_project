import sys
from fire_and_ice_adofai.adofai import validate_adofai

p = sys.argv[1]
errs = validate_adofai(p)
print("OK" if not errs else "FAIL")
for e in errs:
    print(e)
