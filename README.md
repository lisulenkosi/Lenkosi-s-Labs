
 -Input
 Input consists of at least 3 lines. The first line is a string that has either the value encrypt
 or decrypt and represents the mode. The next line contains a single integer 2 ≤ b ≤ 36 which
 represents the base you’ll be working with. The remaining lines are the message (either a normal
 text message, or a series of base-b numbers separated by spaces, depending on the mode). You
 can assume that there is at least one message line.
-Output
 Your output will be a single line that depends on the mode.
-Encryption Mode
 If the mode is encrypt, then the message lines represent a normal message that needs to be
 encrypted. Convert each character to its ASCII value (newlines should also be converted to their
 ASCII value), and then convert each of those numbers to their base-b representations. Output
 these base-b numbers on a single line, with each number separated by a single space.
 -Decryption Mode
 If the mode is decrypt, then the message line is a single line consisting of any amount of base-b
 numbers, each separated by a single space. The message line does not end with a −1. Convert
 each number into its decimal representation, and then into its ASCII character. Output all of
 these characters. Because some of these numbers may be the newline character, your output
 may appear on multiple lines
