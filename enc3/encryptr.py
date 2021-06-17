import pip, os, shutil, sys, time
system = sys.platform
global slash
if system == "linux":
    slash = "/"
elif system == "win32":
    slash = "\\"

cwd = os.getcwd()

try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    aw = ["install","cryptography"]
    pip.main(aw)
    exit("restart the app due to required dependencies where not installed")

try:
    from colorama import Fore, Style,Back
except ModuleNotFoundError:
    ins = ["install","simple-chalk"]
    pip.main(ins)
    exit("restart the app due to required dependencies where not installed")
try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    penis = ["install", "cryptography"]
    pip.main(penis)

green = Fore.GREEN
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
lightBlue = Fore.LIGHTCYAN_EX
blue = Fore.CYAN
reset = Fore.RESET
purple = Fore.LIGHTMAGENTA_EX
lightWhite = Fore.LIGHTWHITE_EX
bold = Style.BRIGHT
normal = Style.NORMAL
logo = """
██████╗ ██╗   ██╗      ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝     ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝ ╚████╔╝█████╗██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝
██╔═══╝   ╚██╔╝ ╚════╝██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗
██║        ██║        ╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║
╚═╝        ╚═╝         ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                """

print(f"{lightBlue}{logo}{reset}")
print("[+]═══════[ Author : @poiper \033[1;36m_-\|/-_\033[1;m Discord: The ceo of gamestop#36 ]═══════[+]\n\n")


def MoveEncFile(name):
    shutil.move(f"{cwd}{slash}{name}",f"{cwd}{slash}Encrypted{slash}")

def MoveDeencFile(name):
    shutil.move(f"{cwd}{slash}{name}",f"{cwd}{slash}Decrypted{slash}")


def gen_key(file):
    key = Fernet.generate_key()
    with open(f"{cwd}{slash}key{slash}{file}", 'wb') as mykey:
        mykey.write(key)



def get_key(file):
    with open(f"{cwd}{slash}key{slash}{file}", 'rb') as mykey:
        key = mykey.read()
    return key

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def findrel(file_endswith):  
    dir_path = os.path.dirname(os.path.realpath(__file__))
  
    for root, dirs, files in os.walk(dir_path):
        for file in files: 
  
            # change the extension from '.mp3' to 
            # the one of your choice.
            if file.endswith(file_endswith):
                nsad = root+'/'+str(file)

    return nsad

def enc(key,infile,outfile):

    f = Fernet(key)

    with open(f"{cwd}{slash}Encrypt-IT{slash}{infile}", 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open (outfile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)



def deenc(key,infile,outfile):
    f = Fernet(key)

    with open(f"{cwd}{slash}Decrypt-IT{slash}{infile}", 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(outfile, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

files = ["Decrypt-IT","Decrypted","Encrypt-IT","Encrypted","key"]
cwd = os.getcwd()

def make_folders(check):
    firstrun = True
    if check == 1:
        firstrun = False

    def mf():
        count = 0
        result = []
        a = True
        while a ==True:
            for thing1, thing2, thing3 in os.walk(cwd):
                for file in thing2:
                    try:
                        if file not in files[count]:
                            result.append(files[count])
                        else:
                            pass
                    except IndexError:
                        a=False
                        break
                    count+=1

        return result

    result = mf()
    count = len(result)
    if firstrun == False:
        if count == 0:
            print(f"\n{reset}{bold}[{red}-{reset}]{lightWhite} It looks like you've already created the required foldes{reset}\n")
        else:
            pass
    if count >= 1:
        dasw = input(f"\n{reset}{bold}[{red}?{reset}]{lightWhite} It appears that don't have all of the 5 necessary folders for this app to function properly would you still like to continue?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
        if dasw == "2":
            sad = input(f"\n{reset}{bold}[{blue}?{reset}]{lightWhite} would you the program to generate the files automatically?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
            if sad == "1":
                count -= 1
                while count != -1:
                    print(f"\n{reset}{bold}[{green}+{reset}]{lightWhite} Folder {blue}{result[count]}{reset} created{reset}\n")
                    os.system(f"mkdir {result[count]}")
                    count -= 1
        if dasw == "1":
            asd = input(f"\n{reset}{bold}[{red}?{reset}]{lightWhite} are you sure you would like to continue?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
            if asd == "1":
                pass
            if asd == "2":
                asad = input(f"\n{reset}{bold}[{blue}?{reset}]{lightWhite} would you the program to generate the files automatically?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
                if asad == "1":
                    count -= 1
                    while count != -1:
                        print(count)
                        print(f"\n{reset}{bold}[{green}+{reset}]{lightWhite} Folder {blue}{result[count]}{reset} created{reset}\n")
                        os.system(f"mkdir {result[count]}")
                        count -= 1
    time.sleep(0.5)