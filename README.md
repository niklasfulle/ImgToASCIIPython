# Img to ASCII Converter Python

## Overview

-   [Description](#description)
-   [Build Dependencies](#build-dependencies)
-   [Build](#build)
-   [Example](#example)

## Description

The program converts an image to ASCII art. The image is first converted to grayscale and then to ASCII characters. The ASCII characters are chosen based on the brightness of the pixels. Pillow is used to convert the image to grayscale and to get the brightness of the pixels. The program was build for a university project and is an conversion of the [Img to ASCII Converter Haskell ](https://github.com/niklasfulle/ImgToASCIIHaskell) program.

The program uses the following formula to calculate the brightness of the pixels:

```python
grayValue = int((red+green+blue)/3)
```

The program uses the following characters to represent the brightness of the pixels:

| Brightness | Character |
| ---------- | --------- |
| 1 - 30     | @         |
| 30 - 40    | #         |
| 40 - 50    | &         |
| 50 - 60    | %         |
| 60 - 70    | $         |
| 70 - 80    | h         |
| 80 - 90    | i         |
| 90 - 100   | j         |
| 100 - 110  | k         |
| 110 - 120  | l         |
| 120 - 130  | m         |
| 130 - 140  | n         |
| 140 - 150  | o         |
| 150 - 160  | p         |
| 160 - 170  | ~         |
| 170 - 180  | \_        |
| 180 - 190  | ;         |
| 190 - 200  | ,         |
| 200 - 210  | .         |
| 210 - 220  | '         |
| 220 - 230  | ´         |
| 230 - 255  |           |

## Build Dependencies

| Name   | Version | Link                              |
| ------ | ------- | --------------------------------- |
| python | 3.11.0  | https://www.python.org/downloads/ |
| Pillow | 9.5.0   | https://pypi.org/project/Pillow/  |

## Build

To build the program run the following command in the root directory of the project:

```bash
python ascii.py
```

The converted image will be saved in the root directory of the project as `output.txt`.

## Example

![mario_small](images/mario.png)

```
                         k k k k k k k k k k k k k k k k k k k k k k
                        k k k k k k k k k k k k k k k k k k k k k k
                        k k k k k k k k k k k k k k k k k k k k k
                k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k
                k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k
                k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k
                k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k
                k k k k k k k k k k k k k l l l l l l l k k k k k l l l k k k k k k k k k k
                k k k k k k k k k k k k m p ~ ~ ~ ~ ~ ~ o k k k m p ~ ~ p i j k k k k k k
                j j k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~
                k j j j j k k k k j j j m ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~
        k k k j k k k k k k k k k k k k m ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m p p ~ o k j j l p p p ~ ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o j j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o k j j l o o o p ~ ~ ~ ~ ~ ~ ~ p m m m m o o o p ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o k j k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o k j k k j j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j m ~ ~ ~ o j j j j j j j l ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        k k k j l o o o n m m m m m m l n ~ ~ ~ ~ ~ ~ ~ p o o o n k k j l o o o o o o o p p ~ ~ ~ ~
        k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k l ~ ~ ~
        k k k k k j j j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k j j k k k k k j j j j j j j k #
        k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o j j j j j j j j j j j j k k k k j
        k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k
        k k k k k k k & o ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ p p p p p p p p p p p p j j k k
                        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                        p ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                k k k $ o p p p p ~ ~ ~ p p p p p p p p p p p p ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                k k k k k k k k k l l l l k k k k k k k k k k k l ~ ~ ~ ~ ~ ~ ~ ~
                k k k k k j j j k j j j k j j j j j j j j j j j k
                k k k k k k k j k k k k k j j k k k k k j j j j j
        k k k k k k k k k k k j k k k k k j j k k k k j k k k k k j j k k k k k k k k k k k
        k k k k k k k k k k k j k k k k k j j k k k k j k k k k k j k k k k k k k k k k k k
        k k k k k k k k k k k j k k k k k j j k k k k j k k k k k j j k k k k k k k k k k k
        k k k k k k k k k k k j k k k k k j j j j j j j k k k k k j j k k k k k k k k k k
k k k k k k k k k k k k k k k j k k k k k k k k k k k k k k k k k j j k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k j k k k k k k k k k k k k k k k k k j j k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k j k k k k k k k k k k k k k k k k k j j k k k k k k k k k k k k k k k
j j j j j j j j j k k k k k k j k j j k k k k k k k k k k k k j k j j k j k k k k j j j j j j j j j
k k k k k k k k k k k k k k k k k k l l k k k k k k k k k l l l k k k k k k k k k k k k k k k k k k
p p p p p p p ~ o k j j k k k k m p ~ ~ o k k k k k k j m p ~ ~ o k k k k j k j l p p p p p p p p p
~ ~ ~ ~ ~ ~ ~ ~ o k j j k k k j m ~ ~ ~ o k k k k k k j m ~ ~ ~ o k k k k j j j m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o j j j k k k j m ~ ~ ~ o k k k k k k j m ~ ~ ~ o k k k k j j j m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k j m p ~ ~ o k k k k k k j m p ~ ~ o k k k k k k k m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ p p ~ o k k k k l l l k k k k k k k k k l l l k k k j m p p p ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ p o o o n k k k k k k k k k k k k k k k k k k k k k k j l o o o p ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o j k k k k k k k k k k k k k k k k k k k k k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k j m ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ o k k k k k k k k k k k k k k k k k k k k k k k k k k k k k k j l p ~ ~ ~ ~ ~ ~ ~ ~
  ~ ~ ~ ~ ~ ~   k k k k k k k k k k k k k k k k k k k   k k k k k k k k k k k k k i l ~ ~ ~ ~ ~ ~
                k k k k k k k k k k k k k k             k k k k k k k k k k k k k h
                k k k k k k k k k k k k k k             k k k k k k k k k k k k k
        k k k i k k k k k k k k k k k k k k             k k k k k k k k k k k k k j j k k
        k k k k k k k k k k k k k j j k k               k k k i k k k k k k k k k k k k k k
        k k k k k k k k k k k k j                               j j k k k k k k j k k k k k
        k k k k k k k k k k k k k j                             k k k k k k k k k k k k k
k k k k k k k k k k k k k k k k k k                             k k k k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k k k k                             k k k k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k k k k                             k k k k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k k k k                             k k k k k k k k k k k k k k k k k k
k k k k k k k k k k k k k k k k k k                             k k k k k k k k k k k k k k k k k k
```
