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
__git__ = 'https://github.com/CSM-BlueRed/'

# Obfuscated with Impostor

class Interpreter():
    def __init__(self, code: str, layersFunction: bytes, module, globals_) -> None:
        self.__module = module
        self.layersFunction = layersFunction
        self.__globals = globals_
        self.code = {
            'bytes': code,
            'str': str(code),
        }

    def Run(self) -> None:
        decoder = self.__getobject__()
        exec(
            eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')).loads(decoder), {'__selfObject__': self, '__module': self.__module, '__sr_m': eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(109)+chr(97)+chr(114)+chr(115)+chr(104)+chr(97)+chr(108)+chr(34)+chr(41)')), '__globals': self.__globals}
        )

    def __getobject__(self) -> object:
        func = self.layersFunction
        return self.__module.b64decode(func)

__object__ = Interpreter(b'QZZ~{Rz*fmQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?QC4h4QB^TRRaIm{S5;C%R8>k+QZPnZQbk5iQEWy?S5|CAQB^TRRaIm{S5;C<R8>k+QZPnZQbk5iQEWy?PDXH5QdUY!RaIn0S5;C%R8>k+QZZ|JRz*fmQEY5TR90+7QC3DvRaIm{S5{I^RBK97QZPzFRz*%uQEW;`S5!(xQB^TZRxoTzS5;C*R4{N-QZPnZRz*2ZRcuO1QdCYwQ!p_@RaIz0S8P&3R8>wxQZPnZQbkTrRcuyBQC4t9Q7|z}RaIn0O)yeQR8>k<QZaBtQbk5iRcvrbQC4h4Q7|=ORWM{nQC3n;RBLcjQZPj@QblA=QEWy^QdVq5QB^TZRxo5zS5;C<RaJ0PQZPnZRz)#SQEWy?R#Z+#QdKcSRWN8qS5;C%R8??UQZQ^<R#i?<RcuyBQB+PvR8~q<QZQ&jO)yeSR8>k;QZZ|JQbk5jS8QxZR90+7Q7|=AR%>KJS8GyERBK97Q$<BEQblA=QEW;`QdCY=QB^TRRxo5%S5;C*RBTFCQZPj@Rz^lnS8PT|QdVqLR4_3^RaInKO>9y^R8~q@QZYtaQdLe+QEXC3QC4hKQ7|=ORaIm{O)yeSR8>k;QZZ|JQbk5mRcvfXR90+7Q7|z}S4Ct(S5;C@RBLcjQZQ?JQblY|Q7}?TQC4tOQB^TZRcm7~S5;C%RBTFDQZPngQbjROQEWy^Ra8<%QZO+?RcmBMO)*kJR8>k?QZZIqQbkrzRcuyBQEN_BRaG%zRaIn0S5{I`R8>k+QZZ|JRz*fmRcvHPRaR_9R8=`cRz+k&S5{I)RBUikQZPk&Qblx5QEW~~S5!(xQ7|z>S5;(AS5;C(R8??UQZPnZQbjROQ*1^^Q&dhxQ&llbRcmNMS8P&3R8??OQhHKaQbk5jRcu;FQC4t8R8=)YRcmBQPDN5kR8>k-QZQ9|Rz*fmQEX&LR#t39QdKomR#jw1S8P&JR90|OQZQCpRz*2ZQEWy?S5!(>QB^ThRxo5zS5;O_R4__aQZPnZRz*%vS8PT|QB+PvQ!p_@RWM{)O>0s_RBK9FQZO-EQbkTqQ*3BRQC4h4R8=)gRaIn4O)yeQR8??OQ$<E$Rz*fmQ*25|PDX4+QB^flR%>KJS8GyERBK98QZZF9QblA=QEW;`QdCY=QB^TRRxo5%S5;C*RBTFCQZQ9|QbtBjS8PT|QdVqLR4_3^RaInKO>9y^R8~q@QZYtaRz*2bQEXC3QC4hKQ7|=ORaIm{O)yeSR8>k;QZZ|JQbkTsQEY5TR90+7Q7|z}S4Ct(S5;C@RBLcjQZQ?JQblY|Q7}$PQC4tOQB^TZRcm7~S5;C%RBTFDQZPngQbjROQEWy^R#Z|&QZO+?RcmBMO)*kJR8>k?QZZIqQbkrzRcuyBQdCk!RaG%zRaIn0S5{I`R8>k+QZZ|JRz*fmRcvHPRaR_ORWLb2Rz+k&S5{I)RBUikQZPk&Qblx5QEXC3S5!(>QB^fVRxo5zS5{U;R4__aQZPnZRz)#VQ*1^^R%=F8QB^TRRxo5*O>9y^RBB2?QZQCpQbkTrRcuyBQfo>@R8=)YRcmZcO)yeQR8@3FQ$<QdQbk5iO>0U>QC4h4RaQnzRcmBIS5;C_RBTF8QZPj@Rz*fmQEW;`PDXH5QdKciRxo5%S5;C}RBTFCQZQOXRz^lnS8PT|QdVq5Q7|z>RaInKO>9y^R4{N@QZYtaR#h=jQEXC3QC4hKQB^TZRaIm{O)yeQR8~q-QZZIxRz*fmQEX00QdV$9Q87wHQEOyFQC3n+RcuOEQ&wwwQbkTrS8Q5HPDDyYR8=`cRxoT@O)*kNRBLodQZZUZQdMkHQ*1^_QB+DrQdKonQbl7hO>9z5RBLcoQZQ?JQblx6RcuyBR%=p5Q&vVxRaI<8O>9<9RBLodQZaBuQbjRNQ*2~NRa8zzQ!q6{RWM^PPDWBpRcuOEQ&w<9QdLe)QEY5TRa8<{R8~quS4Ct(O)yqYRBUinQhHH&QbjRSRcvTTQ)^B}Q7|z>S4Cu3QbkfsRcuOFQhHH(QbtZsS8P^DR%=p4Q!z?YS4C__S5{U|RBTFGQhHH&QbjpWQEX^PQB+P<QZO)iQEOyNQbkfmRcuOFQhHH(QbtZsS8P^DS5#6(R4_G5Rxo5rS8G;GRBTFBQZaBvQbjRSQEX01S5!(xQZO}3Rz+k}Q7}?QRclICQZQ?JQdMM6S8Q5HS5!(>Q!p`8Rxo5%O)yeQR8~$%QhHWGRz*fmRcua3R90|BQC3PzS8HTbQbkfiR8>k+QZPnZQbk5nQ*3ZZS5|OEQB^TRRaIm{S5;C%RcmlzQZZ|KQbk5iQEWy?QC4h4QC3PzS8HQ1O>9y^R8>k+QZPnZQbk5nQ*3ZZPDXH5QB^TRRaIm{S5;C%RcmlzQZZ~{Rz*fmQEWy?QC4h4QC3PzS8HTiS5{I&R8>k+QZPnZQbk5nQ*3ZZPDDyYQB^TRRaIm{S5;C%RcmlzQZZ|JRz*fmQEWy?QC4h4QC3PzS8HTiO>0s@R8>k+QZPnZQbk5nQ*3ZZQ&wz6QB^TRRaIm{S5;C%RcmlzQhHH(Rz*fmQEWy?QC4h4QC3PzS8HTiPDWBfR8>k+QZPnZQbk5nQ*3ZZS5#6(QB^TRRaIm{S5;C%RcmlzQZYp^Rz*fmQEWy?QC4h4QC3PzS8HTpQ7}?MR8>k+QZPnZQbk5nQ*3ZZPDX4+QB^TRRaIm{S5;C%RcmlzQZaBvQbk5iQEWy?QC4h4QC3PzS8HQ1S8Gy2R8>k+QZPnZQbk5nQ7}qKQC4t8R8~q;S4Ct`Q7~3SR8>k-QhHKhQbjpZQ*1^^R#Z+^Q!q7QR#jwLO)yeMRclIBQ$<E$QbtZrQEW;|Rcl67QB^rZRxo5%O)yqWRBTFBQZaBvQbjROQEX&MQdCYxQ!q7CS4CqnQC3n$R4__bQZYq(QdKceRWMpeQ&dh>R4_F|RWM{iO)*kRRBUimQhHG^Rz+4$QEX^PRa8z!R8=ukRaIj!S8P&FRaQz^Q$<yJQblY|RcuB`Ra8<{R8~quS4Ct(O)yqYRBUinQhHH&QbjRSRcvTTQ&w<AQB^fmQZQs%S8GyERBTFFQZZF}Rz+k_Rcum7S5|CQR4_F|RxoHrO)yqYRBTR1QZQ^<QbkryQ*3BTQdVq6QZO|`S5;(MO>9z5RaS6VQ&li}QdKcdRcuB`R#Z+^R8~q;S4Ct>O)yqSRBTFCQZQ^<Rz+-6Q*2I2QdVq6Q87wHQEOyEO)*kVRBUiqQ&li}QdKceRcua3S5|CQR8~e|S4Ct`Q7~3SR8>k<QZZ|KRz)#SQ*3BRRclU0Q7|z>Rz+l5S8P&FR4__eQZR5tQdLe)QEXO7S8Gy5R4_3^Rxo5%O)yqWRclT|QZPzFRz-AERcu;HS5!_#RWLPFQdMIxS5;C@RcuOGQZQ?JRz+-2Q!r#mR%=p5Q&vVxRaInCO)*kJRBTF9QhHH&QbjRPQ7~3YQdVq5R4_GDRcmBgS8GyGR90|VQZPk&QbkTrS8P^DS5#6)Q&vVxRaIz0O>9<9RBLodQZZ|KQbjRPQ*2~PR8&qyQ!q75QZQs!QbkruRaJ0OQZYq(Rz+4%Rcu;FS5|CQR8=)ZQdMk5S5;C>RBTFNQZaBuRz*2ZQEX^PR#Z+^Q&vVxS8HTKS5;C_R8~q<QZZIqQbk5iQEWy?QC4h4R4_49RWM{$S5;C%R8>k+QZPnZQbjpVRcuB`R90+7QB^TRRaIm{S5;O@RaJ0OQ$<E$R#jwARWMdaS8Gy5R8=)YS4Cu2O)yqSRBTFDQZO|{Rz*fmQ*1^^QC4h4QB^TRRaIj!S8P&3RBK97QZPnZQbk5iQEWy^S8Gy5QB^TRRWM{uS5;C(P*gBE', b'4wAAAAAAAAAAAAAAAAQAAAADAAAAQwAAAHNuAAAAdACDAGQBGQB9AHQAgwBkAhkAfQF0AIMAZAMZAH0CfAFqAWQEGQB9A3wCoAJ8A6EBfQN8AqADfAOhAX0DfAKgBHwDoQF9A3wCoAV8A6EBfQN0AIMAZAUZAKAGfAOhAX0DdAd8A3wAgwIBAHwDUwApBk7aCV9fZ2xvYmFsc9oOX19zZWxmT2JqZWN0X1/aCF9fbW9kdWxl2gVieXRlc9oGX19zcl9tKQjaB2dsb2JhbHPaBGNvZGXaCWI4NWRlY29kZdoJYjY0ZGVjb2Rl2gliMzJkZWNvZGXaCWIxNmRlY29kZdoFbG9hZHPaBGV4ZWMpBNoIX2dsb2JhbHPaA29iatoGbW9kdWxlcgcAAACpAHIRAAAA+itDOlxVc2Vyc1xJc2FhY1xEZXNrdG9wXEltcG9zdG9yXGltcG9zdG9yLnB52gxSZW1vdmVMYXllcnMzAAAAcxYAAAAAAQoBCgEKAQoBCgEKAQoBCgEQAQoB', eval(eval('chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(34)+chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)+chr(34)+chr(41)')), globals())
__object__.Run()
```

<br>

## <p align="left">📢・Informations・📢</p>
- `✅` The code can be compiled with PyInstaller and Nuitka.
- `✅` The code can't be brutforced
- `⏹` The code require a good recursion limit (1.000.000)

<br>

## <p align="left">⭐・Repository・⭐</p>
If you like this repository, **star it** ! And if you want to share your opignon, please go to the **repository discussion**. 

<br>

-----

<p align="center"><strong>By BlueRed : <a href="https://github.com/CSM-BlueRed/">github.com/CSM-BlueRed</a></strong></p>