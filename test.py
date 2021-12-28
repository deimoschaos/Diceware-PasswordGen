import pandas as pd
import secrets
import argparse
import random

secretRandom = secrets.SystemRandom()

testlist = ['j','k','l','1','2']

print(random.sample(testlist, len(testlist)))