"""
password: hAck3eRr4nk  aP1p5Le heLlo34wOrLd@11
encryption:
s[i] lowercase s[i+1] upper case swap, add * after that
add each number found at the beginning and replace with 0 at it's position

encrypted: 43Ah*ck0Re*r0nk  51Pa*0p0Le  1143hLe*lo00Ow*Lr*d@00
decryption:
s[i] upper case s[i+1] lower case swap and remove *
collect all numbers from beginning and replace 0 with corresponding  number

given encrypted password, decrypt it
"""
import time


def main():
    s = input("enter encrypted string:")
    result = decrypt(s)
    print(result)


def decrypt(s):
    numbers = []
    newstr = ""
    # Extract numbers added in the beginning to another list
    for i in range(0, len(s)):
        if s[i].isdigit() and int(s[i]) != 0:
            numbers.append(s[i])
    length = len(numbers)
    i = 0
    # Take new string without numbers in beginning
    s2 = s[length:]

    while i < len(s2):
        flag = 0
        # Check for uppercase then lowercase, swap them
        if ((i + 1) < len(s2)) and ((i + 2) < len(s2)):
            if s2[i].isupper() and s2[i + 1].islower() and s2[i + 2] == "*":
                newstr += s2[i + 1] + s2[i]
                i += 3
                flag = 1
        else:
            if not s2[i].isdigit():
                newstr += s2[i]
                i += 1

        # Replace 0 with last number in numbers_list
        if (s2[i].isdigit()) and (int(s2[i]) == 0):
            length = len(numbers)
            newstr += str(numbers[length - 1])
            numbers = numbers[:-1]
            i += 1
            flag = 1

        # concatenate string as it is
        if flag != 1:
            newstr += s2[i]
            i += 1
    return newstr


if __name__ == "__main__":
    start = time.time()
    main()
    print("{} seconds".format(time.time() - start))
