# <p align="center">👑・Impostor・👑</p>

<br>
<p align="center">Impostor is a Python obfuscator, it using crypting and object serialization so its hard to deobfuscating it.</p>
<br>

## <p align="left">📚・Example・📚</p>

<br>

### Normal
```python
input('Hello World!')
```

### Obfuscated
```python
__author__ = 'BlueRed_'
__madeBy__ = 'Impostor'
__git__ = 'https://github.com/CSM-BlueRed/Impostor'

# Obfuscated with Impostor

class Gateway():
  def __init__(self, way: bytes, key: int, **ext) -> None: self.way = way;self.key = key; self.module__ = ext.get('__module', None);self.__globals = ext.get('__globals', None);self.__module = ext.get('__module', None); self.__interpreter = ext.get('interpreter', None)
  def Pass(self): exec(eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')).loads(self.module__.b16decode(self.way)), {'__selfObject__': self, '__key__': self.key, '__module': self.module__, '__globals': self.__globals, '__InterpreterObject__': self.__interpreter}); return self
class Interpreter():
  def __init__(self, code: str, layersFunction: bytes, module, globals_, backend: bytes = b'') -> None: self.__module = module;self.layersFunction = layersFunction;self.__globals = globals_;self.code = {'bytes': code, 'str': str(code)}; self.__backend = backend
  def __tunnel(self) -> Gateway: return Gateway(self.__backend, 3673, __module = self.__module, __globals = self.__globals, interpreter = self)
  def Run(self) -> None: decoder = self.__getobject__(); gate = self.__tunnel().Pass();exec(eval(eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')).loads(decoder), {'__selfObject__': self, '__module': self.__module, '__sr_m': eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')), '__globals': self.__globals, 'gate': gate}), self.__globals)
  def __getobject__(self) -> object: func = self.layersFunction; return self.__module.b64decode(func)

Interpreter(b'QZZ~{Rz*fmQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?S5|CAQB^TRRaIm{S5;C<R8>k+QZPnZQbk5iQEWy?PDXH5QZYthRaIn0S5;C%R8>k+QZZ|JRz*fmQEY5TR90+7QC3DvRaIm{S5{I^RBK97QZPzFRz*%uQEW;`S5!(xQB^TZRxoTzS5;C*R4{N-QZPnZRz*2ZRcuO1QdCYwQ!p_@RaIz0S8P&3R8>wxQZPnZQbkTrRcuyBQC4t9Q7|z}RaIn0O)yeQR8>k<QZaBtQbk5iRcvrbQC4h4Q7|=ORWM{nQC3n;RBLcjQZPj@QblA=QEWy^QdVq5QB^TZRxo5zS5;C<RaJ0PQZPnZRz)#SQEWy?R#Z+#QdKcSRWN8qS5;C%R8??UQZQ^<R#i?<RcuyBQB+PvR8~q<QZQ&jO)yeSR8>k;QZZ|JQbk5jS8QxZR90+7Q7|=AR%>KJS8GyERBK97Q$<BEQblA=QEW;`QdCY=QB^TRRxo5%S5;C*RBTFCQZPj@Rz^lnS8PT|QdVqLR4_3^RaInKO>9y^R8~q@QZYtaQdLe+QEXC3QC4hKQ7|=ORaIm{O)yeSR8>k;QZZ|JQbk5mRcvfXR90+7Q7|z}S4Ct(S5;C@RBLcjQZQ?JQblY|Q7}?TQC4tOQB^TZRcm7~S5;C%RBTFDQZPngQbjROQEWy^Ra8<%QZO+?RcmBMO)*kJR8>k?QZZIqQbkrzRcuyBQEN_BRaG%zRaIn0S5{I`R8>k+QZZ|JRz*fmRcvHPRaR_9R8=`cRz+k&S5{I)RBUikQZPk&Qblx5QEW~~S5!(xQ7|z>S5;(AS5;C(R8??UQZPnZQbjROQ*1^^Q&dhxQ&llbRcmNMS8P&3R8??OQhHKaQbk5jRcu;FQC4t8R8=)YRcmBQPDN5kR8>k-QZQ9|Rz*fmQEX&LR#t39QdKomR#jw1S8P&JR90|OQZQCpRz*2ZQEWy?S5!(>QB^ThRxo5zS5;O_R4__aQZPnZRz*%vS8PT|QB+PvQ!p_@RWM{)O>0s_RBK9FQZO-EQbkTqQ*3BRQC4h4R8=)gRaIn4O)yeQR8??OQ$<E$Rz*fmQ*25|PDX4+QB^flR%>KJS8GyERBK98QZZF9QblA=QEW;`QdCY=QB^TRRxo5%S5;C*RBTFCQZQ9|QbtBjS8PT|QdVqLR4_3^RaInKO>9y^R8~q@QZYtaRz*2bQEXC3QC4hKQ7|=ORaIm{O)yeSR8>k;QZZ|JQbkTsQEY5TR90+7Q7|z}S4Ct(S5;C@RBLcjQZQ?JQblY|Q7}$PQC4tOQB^TZRcm7~S5;C%RBTFDQZPngQbjROQEWy^R#Z|&QZO+?RcmBMO)*kJR8>k?QZZIqQbkrzRcuyBQdCk!RaG%zRaIn0S5{I`R8>k+QZZ|JRz*fmRcvHPRaR_ORWLb2Rz+k&S5{I)RBUikQZPk&Qblx5QEXC3S5!(>QB^fVRxo5zS5{U;R4__aQZPnZRz)#VQ*1^^R%=F8QB^TRRxo5*O>9y^RBB2?QZQCpQbkTrRcuyBQfo>@R8=)YRcmZcO)yeQR8@3FQ$<QdQbk5iO>0U>QC4h4RaQnzRcmBIS5;C_RBTF8QZPj@Rz*fmQEW;`PDXH5QdUMwRxo5%S5;C}RBTFCQZQOXRz^lnS8PT|QdVq5Q7|z>RaInKO>9y^RaJ0UQZYtaR#h=jQEXC3QC4hKQB^TZRaIm{O)yeSR8>wyQZZ|JQbkryQEX&LRaS6CQ7|=AR#jw5S8GyER4{N-QZQ98QblA=QEW~~QC4hKQB^TRRxo5zS8Gy8RBLcmQZPnZQbkr!Q*2I1RclU0Q7|z?QEOyZQbkfsRcuOFQZQ9|Rz-AAS8P^DS5#6(R8~q;S4Ct>O>9<9RBLodQ&vhsRz*foQEXO7Q&dhyQZO}PR%>KhO>9z3R8~q@QZZF}QblY}Q!r#oRcl67QC3DvR%>ipO>9<9RBTR0QZZ~=Rz)#SQEX&LR#ZwwQdKo!S8HTfQbkfsRcua1Q&m=4QbtBkQEYHXS8Gm1R4_3^RxoT@O)*kPRBUioQZaBvQbjpVRWMdcQdVq5R4_G6QZQs!QbkfuRBUiqQ$<yJRz+-2Q!r#mR%=p4R53<NRWM^PO)yeYRBUioQhHH&QbjpVQEX^PR90|SQ7|!7QZQsoQbkfuRBUiqQ$<yJRz+-2RcvfXPDDyoR8=ukRWNK;O)yeORBTR2QZaBuQbkr%RcuyBR8&e;QZO|{QdMM2Q7}?UR8~q@Q&li}Rz-AARcu;FR#tFDR8=)gRxo5zS8G;IRBK9MQZaBuQbjpVQEX&NS5!__QZO}PR#jwSQbkfwR8~q^Q&m=4QbkryRcum7Q&wz7Q!qJ8R#j|TS5;C%R8>k+QZPnZQdM+NQ*2~NQ&wz6QB^TRRaIm{S5;O_R4{N@QZZ~=Qbk5iQEWy?QC4h5Q!qJ8S4Cu2S5;C%R8>k+QZPnZQdM+NQ*3BRR90+7QB^TRRaIm{S5;O_R4{N@QZO-EQbk5iQEWy?QC4h5Q!qJ8Rxo5nS5;C%R8>k+QZPnZQdM+NQ*3BRRaR_8QB^TRRaIm{S5;O_R4{N@QZZIqQbk5iQEWy?QC4h5Q!qJ8Rxo5zS5;C%R8>k+QZPnZQdM+NQ*2I1QC4h4QB^TRRaIm{S5;O_R4{N^QhHKaQbk5iQEWy?QC4h5Q!qJ8RxoHrS5;C%R8>k+QZPnZQdM+NQ*2~OQC4h4QB^TRRaIm{S5;O_R4{N>Q$<!<Qbk5iQEWy?QC4h5Q!qJ8RxoT*S5;C%R8>k+QZPnZQdM+NQ*3BRQC4h4QB^TRRaIm{S5;O_R4{N@Q&wzRQbk5iQEWy?QC4h5Q!qJ8S4Ct>S5;C%R8>k+QZPnZQdMkHQ*1^^Q&dhyR8=)$Rz+-6QC3nyR8??UQZQ?JR#i?;QEXaBPDDyoR4_F|Rxo5*S8G;ER90|WQZQ>URz*fmQ!rLaQdVq5RaG@pR%>KoQ87|ZR90|UQ&wwwQblY}RcvrbS8GmHR8=)$S4C__S8GyIRBK9BQZaBvQbjRSQ*2I1PDD;sQ&lljRaIj!O>0t6R8~q^Q$<!`Qbk5jS8P^DS8Gy5QdKcSS4Ct_O)yqQRBTFNQZZ|JQbkryQEXO8QdCYxQ&lx#RaInRQbkfwR90|VQZYq(QdKceS8Ps5Q&wz6R8~q;Rxo5rO)yeURBUipQhHKhRz)#RS8QZRQdCY=Q&lxnS8HTpQbkfuRcmlmQZPngQbkTvQ*3ZZQC4h4QB^TRRaIm{S5;C%RBB2?QZQ9{Rz)#TQ*2~PR#Z+^QB^fzR%>H0O>0s{R4__ZQhHH&QbtBkRcu;FS8GaDR8~e|RxoT@S8Gy2RBLcqQZaBvQbjpVRcvHRR8&qyQ&lljRcmBQO)*kNR4{Z#Q&m=4QbtBkQ!r#mR%=p4R8~q$Rxo5nO)yqURBTFDQZZUZQblxARWMdcQdVq5RaG@iQZQs!QbkfuRclIEQZQ9|QbtZsRWMpeR%=p4Q!z?YR#j|PS8GyKR8>wzQ&vhsRz*fnS8QZRPDD;dQZO}CQZQs%S8GyER8??TQ&li}Rz+k}Q7}qKQC4tOR8=)$Rxo5%O)*kRRclT|QZPngRz)#RS8QZSQB+P<QdUYtQEOyEO>0t4RcuOGQZPk&Qblx6RWMpgRcl67QC3DvR%>ipO>9<9RBTFNQZaBuQbjpVQEX&NS5!__QdKo!R#jwIQbkfsRcua1Q&m=4QblY}S8PT|S5|CQR4_F|RxoHoQ7~3SR8>k@QZZ~=Rz)#RRcvTTR8&q?QB^flRcm7~O>0t4R4`6PQ&m=4QbtBkQ!r#mR%=p4R8=)oRxoHrO)yqSRBTFDQZZUZQblxARWMdcQdVq5Q&lx#RWM{)O>9z5R8??TQZY(IQdLe)QEXaBS5#6}R8~q$S4Ct(O)*kTRBUioQ&vhsRz*fnQEX&LR#Z+^RaG@pS8HQ1O>0(4RaJ0OQZYq(Qblx6S8QxZS5!(>R8=r}QEO;MS5;C%RBUimQZR5rRz*fmQEWy?QC4h4QB^fzRWM{rQC3nyR8>k+QZPnZQbk5jS8Ps5QC4tOQB^TRRaIm{S5;C%RclT|QZPj@QblA^S8QZTRa8z!R8=)oR#js#O>9z5RaS6VQZZIxR#kLPQEW;`QC4h4QB^TRRaIm{O)*kPR8>k=QZPnZQbk5iQEWy?QEO60R8=uURaIn5QEO5{R8?y^',
            b'4wAAAAAAAAAAAAAAAAQAAAADAAAAQwAAAHN0AAAAdACDAGQBGQB9AHQAgwCgAWQCoQFzGmQAUwB0AIMAZAMZAH0BdACDAGQEGQB9AnwBagJkBRkAfQN8AqADfAOhAX0DfAKgBHwDoQF9A3wCoAV8A6EBfQN8AqAGfAOhAX0DdACDAGQGGQCgB3wDoQF9A3wDUwApB07aCV9fZ2xvYmFsc9oEZ2F0ZdoOX19zZWxmT2JqZWN0X1/aCF9fbW9kdWxl2gVieXRlc9oGX19zcl9tKQjaB2dsb2JhbHPaA2dldNoEY29kZdoJYjg1ZGVjb2Rl2gliNjRkZWNvZGXaCWIzMmRlY29kZdoJYjE2ZGVjb2Rl2gVsb2FkcykE2ghfZ2xvYmFsc9oDb2Jq2gZtb2R1bGVyCQAAAKkAchIAAAD6MkM6XFVzZXJzXElzYWFjXERlc2t0b3BcSW1wb3N0b3JcR2l0aHViXGltcG9zdG9yLnB52gxSZW1vdmVMYXllcnM0AAAAcxYAAAAAAQoBEAEKAQoBCgEKAQoBCgEKARAB',
            eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)+chr(34)+chr(41)')), globals(),
            b'E3000000000000000000000000040000000200000043000000733E00000074008300640119007D0074008300640219007D0174008300640319007D027C016A01640419007D0364057C005F027C026406140064071B007C036602530029084EDA0E5F5F73656C664F626A6563745F5FDA155F5F496E7465727072657465724F626A6563745F5FDA075F5F6B65795F5FDA05627974657354E908000000E7000000000000F83F2903DA07676C6F62616C73DA04636F6465DA0865786563757465642904DA036F626ADA0E696E7465727072657465724F626ADA036B65797208000000A900720D000000FA32433A5C55736572735C49736161635C4465736B746F705C496D706F73746F725C4769746875625C696D706F73746F722E7079DA07476174657761791B000000730C00000000010A010A010A010A010601'
).Run()
```

<br>

## <p align="left">📢・Informations・📢</p>
- `✅` The code can be compiled with PyInstaller and Nuitka.
- `✅` The code can't be brutforced
- `⏹` The code require a good recursion limit (1.000.000)

<br>

## <p align="left">⭐・Repository・⭐</p>
If you like this repository, **star it** ! And if you want to share your opinion, please go to the **repository discussion**. 

<br>

-----

<p align="center"><strong>By BlueRed : <a href="https://github.com/CSM-BlueRed/">github.com/CSM-BlueRed</a></strong></p>
