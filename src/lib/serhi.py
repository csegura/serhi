# RUNNER
# ajustes para guardar los archivos donde corresponda
import os

def initialize(entyty, name):
    global CWD
    global BASE_PATH
    global DATA_PATH
    global DOWN_PATH
    global OUT_FILE

    CWD = os.getcwd()

    if CWD.find("runner") == -1:
        # our jupyter
        BASE_PATH = "../../.."
    else:
        # we are on github action
        BASE_PATH = "/home/runner/work/serhi/serhi"

    DATA_PATH = f"{BASE_PATH}/data/process/{entyty}/"
    DOWN_PATH = f"{BASE_PATH}/tmp/download/{entyty}/"

    OUT_FILE = f"{DATA_PATH}{name}.csv"

    os.system(f"echo serhi.CWD       {CWD}")
    os.system(f"echo serhi.BASE_PATH {BASE_PATH}")
    os.system(f"echo serhi.DATA_PATH {DATA_PATH}")
    os.system(f"echo serhi.DOWN_PATH {DOWN_PATH}")
    os.system(f"echo serhi.OUT_FILE  {OUT_FILE}")

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH, exist_ok=True)

    if not os.path.exists(DOWN_PATH):
        os.makedirs(DOWN_PATH, exist_ok=True)

print('SerHi Tools')