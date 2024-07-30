# Cipher Algorithms

This Python project implements four types of cipher algorithms for encrypting text. The implemented ciphers include:

- Additive Cipher
- Multiplicative Cipher
- Affine Cipher
- Mapping Cipher

## Table of Contents

- [Cipher Algorithms](#cipher-algorithms)
  - [Table of Contents](#table-of-contents)
  - [Additive Cipher](#additive-cipher)
  - [Multiplicative Cipher](#multiplicative-cipher)
  - [Affine Cipher](#affine-cipher)
  - [Mapping Cipher](#mapping-cipher)
- [Examples](#examples)
  - [Example 1](#example-1)
  - [Example 2](#example-2)
- [Installation](#installation)
- [Usage](#usage)


## Additive Cipher
The Additive Cipher shifts each letter in the text by a specified key value.

```
additive-cipher -text "<text>" -key <key>
```

## Multiplicative Cipher
The Multiplicative Cipher multiplies the position of each letter by a specified key value.

```
multiplicative-cipher -text "<text>" -key <key>
```

## Affine Cipher
The Affine Cipher combines both multiplicative and additive transformations.


```
affine-cipher -text "<text>" -a <a-value> -b <b-value>
```
## Mapping Cipher
The Mapping Cipher replaces each letter in the text with a corresponding letter from a specified mapping string.


```
mapping-cipher -text "<text>" -mapping "<mapping>"
```
# Examples
Here are some examples to illustrate how to use the different cipher algorithms:

## Example 1
Input:
```
2
additive-cipher -text "HELP me" -key 1
additive-cipher -text " HELP me " -key 1
```
Output:
```
IFMQ NF
IFMQ NF
```

## Example 2
Input:
```
2
multiplicative-cipher -text "danger" -key 3
multiplicative-cipher -key 3 -text "danger"
```
Output:

```
JANSMZ
JANSMZ
```


# Installation

To run this project, ensure you have Python installed on your system. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/amirbaa1/Cipher_Algorithms.git
cd cipher-algorithms
```

# Usage
To execute the ciphers, you need to run the Python script from the command line. Here is how you can do it:

1. Open your terminal or command prompt.
2. Navigate to the directory where you have cloned the repository.
3. Run the script using the following command:

```bash
python Cipher.py
```
You will then be prompted to input the number of commands you want to execute and the commands themselves. For example:

```
additive-cipher -text "HELP me" -key 1
multiplicative-cipher -text "danger" -key 3
```
This will output the encrypted text using the specified ciphers.
