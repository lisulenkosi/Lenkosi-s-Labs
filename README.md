sub3:
 -Input
 The first line of input is a number 2 ≤ b ≤ 36, which represents the base we want to convert to.
 The rest of the input consists of a series of non-negative integers, one per line. You can assume
 that there will always be at least one number given. The end of the input will be signalled by
 the number −1, which simply tells you when to stop reading in, and should not be processed.
 -Output
 For each decimal number, output its base-b representation. Use the capital letters for bases
 greater than 10
sub4:
 -Input
 The first line of input is a number2≤b≤36,which represents the base we want to convert
 from. Therestof the input consists of a series of strings, oneper line. Be aware that these
 cannot be treated simply as integers,because they may contain letters. If there are letters,they
 are always uppercase.You can assume that there will always be atleast one number given.The
 end of the input will be signalled by −1, which simply tells you when to stop reading in,and
 should not be processed.
-Output
 For each base-b number,output its decimal representation.
sub5:
 -Input consists of three lines. The first line is a string that has either the value encrypt or decrypt
 and represents the mode. The next line contains a single integer 2 ≤ b ≤ 36 which represents
 the base you’ll be working with. The third line is the message (which is either a normal text
 message, or a series of base-b numbers separated by spaces, depending on the mode). You can
 assume the third line is never empty.
 -Output
 Your output will be a single line that depends on the mode.
 - Encryption Mode
 If the mode is encrypt, then the message line is a normal message that needs to be encrypted.
 Convert each character to its ASCII value, and then convert each of those numbers to their base
b representations. Output these base-b numbers on a single line, with each number separated by
 a single space.
 -Decryption Mode
 If the mode is decrypt, then the message line is a series of base-b numbers, each separated by a
 single space. The message line does not end with a −1. Convert each number into its decimal
 representation, and then into its ASCII character. Output all of these characters on a single line
sub6:
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
