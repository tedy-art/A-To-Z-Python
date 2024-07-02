"""
Question 7:
Implement a program that checks if a given character is a vowel.
Print "Vowel" if it is, otherwise print "Consonant."
characters: a, b, c, d, e, f, g, h, i, j, k, l, m,n , o, p, q, r, s, t, u, v, w, x,y ,z
Vowel: a, e, i, o, u, y
"""

consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
Vowel = ["a", "e", "i", "o", "u", "y"]

ch = input("Enter : ").lower()
if ch in consonant:
    print(f"consonant : {ch}")
if ch in Vowel:
    print(f"Vowel : {ch}")