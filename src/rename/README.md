# rename.py

ファイル名を指定フォーマットの連番名に変更する。

## Examples

```
$ ls sample/
IMG_1.png  IMG_10.png  IMG_2.png  IMG_3.png  IMG_4.png  IMG_5.png  IMG_6.png  IMG_7.png  IMG_8.png  IMG_9.png
```

上記のようなディレクトリがあるとして、

```
$ python rename.py sample/ "IMG_{num}.{ext}" --dry-run
sample/IMG_01.png
--> sample/IMG_1.png
sample/IMG_02.png
--> sample/IMG_2.png
sample/IMG_03.png
--> sample/IMG_3.png
sample/IMG_04.png
--> sample/IMG_4.png
sample/IMG_05.png
--> sample/IMG_5.png
sample/IMG_06.png
--> sample/IMG_6.png
sample/IMG_07.png
--> sample/IMG_7.png
sample/IMG_08.png
--> sample/IMG_8.png
sample/IMG_09.png
--> sample/IMG_9.png
sample/IMG_10.png
--> sample/IMG_10.png
```

といった形でファイル名が変更される。