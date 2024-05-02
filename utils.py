import urllib3, requests, nanoid, traceback, os
from colorama import init, Fore
from multiprocessing import Lock
from requests_html import HTMLSession

lock = Lock()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class colors:
    @staticmethod
    def info(msg):
        lock.acquire()
        print("[" + Fore.BLUE + "#" + Fore.RESET + "] " + str(msg))
        lock.release()

    @staticmethod
    def correct(msg):
        lock.acquire()
        print("[" + Fore.GREEN + "+" + Fore.RESET + "] " + str(msg))
        lock.release()

    @staticmethod
    def error(msg):
        lock.acquire()
        print("[" + Fore.RED + "-" + Fore.RESET + "] " + str(msg))
        lock.release()

    @staticmethod
    def warning(msg):
        lock.acquire()
        print("[" + Fore.YELLOW + "!" + Fore.RESET + "] " + str(msg))
        lock.release()


init()


def session(proxy=True, random=False, html=False, timeout2=60):
    if html: session = HTMLSession()
    else: session = requests.Session()
    if proxy:
        session.verify = False
        session.timeout = timeout2
        country = "_country-Brazil"
        if random:
            country = ""
        #session.proxies.update({"https": "http://127.0.0.1:8888"})
        #session.proxies.update({'http': f'http://bclhgmsb:5fSVn3JX3uMRkn4e{country}@3.217.123.113:31112','https': f'http://bclhgmsb:5fSVn3JX3uMRkn4e{country}@3.217.123.113:31112'})
        #session.proxies.update({'http': f'http://mariamuller-dc-any:K1xFbFhXZwde@gw.ntnt.io:5959', 'https': 'http://mariamuller-dc-any:K1xFbFhXZwde@gw.ntnt.io:5959'})
        session.proxies.update({'http': f'http://hdgipwrz:HmTY4iMVvLASgsfR@proxy.proxy-cheap.com:31112', 'https': 'http://hdgipwrz:HmTY4iMVvLASgsfR@proxy.proxy-cheap.com:31112'})
    return session


class random:
    def randAtoZ(len):
        return nanoid.generate("abcdefghijklmnopqrstuvwxyz", len)
    def rand0to9(len):
        return nanoid.generate("0123456789", len)
    def randStr(len):
        return nanoid.generate("abcdefghijklmnopqrstuvwxyz1234567890", len)
    def people(use_session=False, sexo='I', pontuacao='N', idade='0', cep_estado='', quantidade='1', cep_cidade=''):
        """
        sexo = ['I'=Aleatório 'H'=Homem 'M'=Mulher]
        pontuação ['N'=Não, 'S'=Sim]
        idade = int number
        quantidade de pessoas geradas = int number
        cep_estado = ['RJ', 'RS', 'PR', etc]
        cep_cidade = Necessário cep_estado -> int number
        """
        if use_session: s = session
        else: s = requests
        return s.post("https://www.4devs.com.br/ferramentas_online.php",data={"acao": "gerar_pessoa","sexo": sexo,"pontuacao": pontuacao,"idade": idade,"cep_estado": cep_estado,"txt_qtde": quantidade,"cep_cidade": cep_cidade,}).json()
   
def bin(bin):
    try:
        return (requests.get(f"https://bin-checker.net/api/{bin}", verify=False).json()["scheme"].lower())
    except Exception:
        colors.info(traceback.print_exc())
        colors.error("Failed at get BIN info")
        
def get_len(file):
    return len(open(f'{file}.txt', "r").readlines())

class save:
    def getFirstLine(filename):
        lock.acquire()
        with open(f"{filename}.txt", "r+", encoding='utf-8') as f:
            firstLine = f.readline()
        lock.release()
        return firstLine

    def removeFirstLine(filename):
        lock.acquire()
        with open(f"{filename}.txt", "r+", encoding='utf-8') as f:
            firstLine = f.readline()
            data = f.read()
            f.seek(0)
            f.write(data)
            f.truncate()
        lock.release()
        return firstLine
        
    def get_filepaths(directory):
        lock.acquire()
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        lock.release()
        return file_paths

    def savetofile(filename, texttosave, place='./'):
        lock.acquire()
        with open(f"{place}{filename}.txt", "a", encoding='utf-8') as f:
            f.write(f"\n{texttosave}")
            f.close()
        lock.release()