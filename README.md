# Spoken English to Written English
This is a library that converts spoken English (text) into the correct written English as per a given set of rules which are listed below:

## 1)  Conversion of numbers:
- This code has the functionality of converting numbers that can be written as a single word or are a multiple of 100 or 1000.
- The array 'number_words' is meant for extending the functionality to all the expressions that represent numbers. This functionality is yet to be implemented.

## 2) Adjusting for tuples:
- Where tuple words (double, triple, quadruple, ...) are encountered before a capital letter, we are replacing the expression by the relevant number of occurrences of the letter. For example, "triple A" will be converted to "AAA".

## 3) Currency adjustement:
- Whenever any currency term is encountered, the expression is converted to the correct written representation. For example "twenty rupees" will be converted to "Rs.20".
- For now, this feature has been implemented only for Rupees and Dollars. However, any currency name and symbol can be added to the relevant dictionary to add functionality.

## 4) Short form adjustemnt:
- All short forms are printed in the appropriate manner without spaces in between. For example "A B C" will become "ABC".

The code can be tested in the following manner (There seems to be a problem with the PyPI registraton at the moment, so it is suggested to download the /src/s2w_pkg/SpokenToWritten.py for now.
![image](https://user-images.githubusercontent.com/59921667/112733407-e87e6b00-8f65-11eb-958d-6961c24198a9.png)

