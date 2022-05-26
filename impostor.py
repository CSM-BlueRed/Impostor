import sys
import os

from pystyle import *
import marshal as marshal
import base64
import random

class Impostor():

    serializer = marshal

    def Alt(text: str, evalCode: bool = True) -> str:
        formated = '+'.join(f'chr({char})' for char in [ord(char_) for char_ in text])
        return f'eval(eval({formated!r}))' if evalCode else f'eval({formated!r})'

    hidedText = 'GG! You deobfuscated the code! obfuscated by Impostor'
    exceptionCode = 'input("Don\'t try to skid Impostor obfuscation !");exit(0)'
    gitLink = 'https://github.com/CSM-BlueRed/Impostor'

    infos = {
        '__author__': 'BlueRed_',
        '__madeBy__': 'Impostor',
        '__git__': gitLink,
    }
    gatewayKey = random.randint(0, 10000)
    def Gateway() -> str:
        obj = globals()['__selfObject__']
        interpreterObj = globals()['__InterpreterObject__']
        key = globals()['__key__']
        code = interpreterObj.code['bytes']
        obj.executed = True
        return ((key * 8 / 1.5), code)
    comment = 'Obfuscated with Impostor'
    encCommend = ' + '.join(f'chr({char})' for char in [ord(char_) for char_ in comment])
    checkInfos = ' and '.join(f'globals().get("{key}") == {value!r}' for key, value in infos.items()) + \
        f' and ("# " and {encCommend}) in open(__import__("os").path.abspath(__file__), "r", encoding = "utf-8").read() '
    interpreterClass = """
class Interpreter():
  def __init__(self, code: str, layersFunction: bytes, module, globals_, backend: bytes = b'') -> None: self.__module = module;self.layersFunction = layersFunction;self.__globals = globals_;self.code = {'bytes': code, 'str': str(code)}; self.__backend = backend
  def __tunnel(self) -> Gateway: return Gateway(self.__backend, GATEWAYKEY, __module = self.__module, __globals = self.__globals, interpreter = self)
  def Run(self) -> None: decoder = self.__getobject__(); gate = self.__tunnel().Pass();exec(eval(MARSHALMODULE.loads(decoder), {'__selfObject__': self, '__module': self.__module, '__sr_m': MARSHALMODULE, '__globals': self.__globals, 'gate': gate}), self.__globals)
  def __getobject__(self) -> object: func = self.layersFunction; return self.__module.b64decode(func)
"""[1:-1].replace('MARSHALMODULE', Alt('__import__("marshal")')).replace('GATEWAYKEY', str(gatewayKey))

    gatewayClass = """
class Gateway():
  def __init__(self, way: bytes, key: int, **ext) -> None: self.way = way;self.key = key; self.module__ = ext.get('__module', None);self.__globals = ext.get('__globals', None);self.__module = ext.get('__module', None); self.__interpreter = ext.get('interpreter', None)
  def Pass(self): exec(MARSHALMODULE.loads(self.module__.b16decode(self.way)), {'__selfObject__': self, '__key__': self.key, '__module': self.module__, '__globals': self.__globals, '__InterpreterObject__': self.__interpreter}); return self
"""[1:-1].replace('MARSHALMODULE', Alt('__import__("marshal")'))

    def RemoveLayers() -> str:
        _globals = globals()['__globals']
        if not globals().get('gate'): return
        obj = globals()['__selfObject__']
        module = globals()['__module']
        code = obj.code['bytes']
        code = module.b85decode(code)
        code = module.b64decode(code)
        code = module.b32decode(code)
        code = module.b16decode(code)
        code = globals()['__sr_m'].loads(code)
        return code

    def Obfuscate(code: str) -> str:
        sys.setrecursionlimit(1000000)

        _code = code
        program = r"{'__name__': '__main__'}"
        runCode = f"""
if not ({Impostor.checkInfos}): {Impostor.exceptionCode}
exec({_code!r}, {program})
"""[1:-1]

        code__ = Impostor.serializer.dumps(compile(runCode, 'Impostor', 'exec'))
        infos_ = '\n'.join(f'{key} = {value!r}' for key, value in Impostor.infos.items())

        code__ = base64.b16encode(code__)
        code__ = base64.b32encode(code__)
        code__ = base64.b64encode(code__)
        code__ = base64.b85encode(code__)

        code_ = f"""
{infos_}

# {Impostor.comment}

{Impostor.gatewayClass}
{Impostor.interpreterClass}

Interpreter({code__!r},
            {base64.b64encode(Impostor.serializer.dumps(Impostor.RemoveLayers.__code__))!r},
            {Impostor.Alt('__import__("base64")')}, globals(),
            {base64.b16encode(Impostor.serializer.dumps(Impostor.Gateway.__code__))!r}
).Run()
"""[1:-1]
        return code_

colors = Col.red_to_purple
space = '\n' * 3
interval = 0.01
banner = """
██╗███╗   ███╗██████╗  ██████╗ ███████╗████████╗ ██████╗ ██████╗
██║████╗ ████║██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║██╔████╔██║██████╔╝██║   ██║███████╗   ██║   ██║   ██║██████╔╝
██║██║╚██╔╝██║██╔═══╝ ██║   ██║╚════██║   ██║   ██║   ██║██╔══██╗
██║██║ ╚═╝ ██║██║     ╚██████╔╝███████║   ██║   ╚██████╔╝██║  ██║
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""[1:-1]

def Intro():
    System.Clear()
    Anime.Fade(text = Center.Center(banner), color = colors, mode = Colorate.Vertical, enter = True)
    while True:
        System.Clear()
        Main()

def Main():
    whiteChars = list('═╝╚╔╗║') # █
    print(space +
        Colorate.Format(Center.XCenter(banner), whiteChars, Colorate.Vertical, colors, Col.white)
    + space)
    path = Write.Input('Drag and drop the file to obfuscate => ', colors, interval)
    path = os.path.normpath(path)
    if not os.path.exists(path):
        Colorate.Error('File not found.')
        return
    if not os.path.isfile(path):
        Colorate.Error('Not a file.')
        return
    Write.Input('[!] WARN: The __name__ variable will be set to "__main__". Press Enter to continue...', Col.DynamicMIX([Col.orange, Col.yellow]), interval)
    with open(path, 'r', encoding = 'utf-8') as file:
        code = file.read()
    code = Impostor.Obfuscate(code)
    filename = os.path.basename(path).removesuffix('.py')
    with open(filename + '-Impostor.py', 'a+', encoding = 'utf-8') as file:
        file.write(code)
    Write.Print(f'[!] Successfully obfuscated !', Col.green, interval)
    input()

if __name__ == '__main__':
    System.Title('Impostor - by BlueRed_')
    System.Size(200, 50)
    Intro()
