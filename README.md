# simpledecrypt
This python script decrypts simple ciphers such as substitution and caesar ciphers. The method used by the programming is frequency analysis. By having a reference text in plain text to generate a reference frequency table, the program is able to take in ciphertext using the ciphers above and decrypt them. The reference frequency table was based on the first chapter of Harry Potter the sorcerer's stone.

For different files, the frequency placement of the letters may vary. On this fact, some texts might not be fully decrypted. Regardless, important information about the main plaintext can still be found via the program.

## Usage

Let's say we are given a ciphertext such as this [one](encryptedsub.txt).
```console
(base) stange@ericjoshua simpledecrypt % cat encryptedsub.txt
Iqkkn Hgzztk qfr zit Lgketktk'l Lzgft


EIQHZTK GFT

ZIT WGN VIG SOCTR

Dk. qfr Dkl. Rxklstn, gy fxdwtk ygxk, Hkoctz Rkoct, vtkt hkgxr zg lqn
ziqz zitn vtkt htkytezsn fgkdqs, ziqfa ngx ctkn dxei. Zitn vtkt zit sqlz
htghst ngx'r tbhtez zg wt ofcgsctr of qfnziofu lzkqfut gk dnlztkogxl,
wteqxlt zitn pxlz rorf'z igsr vozi lxei fgfltflt.
```

The program is executed as below:
```console
(base) stange@ericjoshua simpledecrypt % python3 simpledecrypt.py
/path/to/file:encryptedsub.txt
```
Upon entering, we receive an output txt file in the same directory with the name `decrypted.txt`. Printing out the content on the conse shows that the program works!

```console
(base) stange@ericjoshua simpledecrypt % cat decrypted.txt
harry potter and the sorcerer's stone


chapter one

the boy who lived

mr. and mrs. dursley, of number four, privet drive, were proud to say
that they were perfectly normal, thank you very much. they were the last
people you'd expect to be involved in anything strange or mysterious,
because they just didn't hold with such nonsense.

mr. dursley was the director of a firm called grunnings, which made
drills. he was a big, beefy man with hardly any neck, although he did
have a very large mustache. mrs. dursley was thin and blonde and had
nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the
neighbors. the dursleys had a small son called dudley and in their
opinion there was no finer boy anywhere.
```

## Installation

The files can be accessed simply by entering in the terminal `git clone https://github.com/stangeqwq/simpledecrypt`


