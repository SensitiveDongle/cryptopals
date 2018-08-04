Decrypt the file 6.txt.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
2. Write a function to compute the edit distance/Hamming distance between two
strings. The Hamming distance is just the number of differing bits. The distance
between:
```
this is a test
```
and
```
wokka wokka!!!
```
is 37. Make sure your code agrees before you proceed.
3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE
worth of bytes, and find the edit distance between them. Normalize this result
by dividing by KEYSIZE.
4. The KEYSIZE with the smallest normalized edit distance is probably the key. You
could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE
blocks instead of 2 and average the distances.
5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of
KEYSIZE length.
6. Now transpose the blocks: make a block that is the first byte of every block,
and a block that is the second byte of every block, and so on.
7. Solve each block as if it was single-character XOR. You already have code to do
this.
8. For each block, the single-byte XOR key that produces the best looking histogram
is the repeating-key XOR key byte for that block. Put them together and you have
the key.
This code is going to turn out to be surprisingly useful later on. Breaking
repeating-key XOR ("Vigenere") statistically is obviously an academic exercise,
a "Crypto 101" thing. But more people "know how" to break it than can actually
break it, and a similar technique breaks something much more important.

# Why is hamming distance an effective metric for determining key length?
Yes, you are remembering correctly. Yes, this is a reasonable method to find the key length.

The reason why this works is because, typically, the plaintext is not uniformly random. For instance, rather than a random bit-string, the plaintext might be some English text, encoded in ASCII. If X,Y represent two random English letters, encoded in ASCII, then the expected value of the Hamming distance wt(X⊕Y) is maybe 2-3 bits. In contrast, if U,V are two random 8-bit bytes, then the expected value of the Hamming distance wt(U⊕V) is 4 bits, significantly larger. If you look at sequences of multiple characters, rather than a single letter at a time, the difference becomes even larger.

How does this apply to your situation?

Well, if you have correctly guessed the key length, then your ciphertext consists of X⊕K and Y⊕K (as Dilip Sarwate explains), where X,Y come from the plaintext distribution. Now notice that the Hamming distance between these two is the same as the Hamming distance between X and Y, namely, it is wt(X⊕Y). As we explained before, you can expect this might be maybe 2-3 bits times the length of X measured in bytes.

In contrast, if you guessed the key length incorrectly, then you're looking at ciphertexts of the form X⊕K and Y⊕K′. The Hamming distance between the two basically boils down to the Hamming distance between U and V, where U and V are uniformly randomly distributed (since K,K′ are uniformly randomly distributed), and thus is wt(U⊕V). As explained before, you can expect this should be approximately 4 bits times the length of X measured in bytes.

So, as you can see, the Hamming distance is significantly less when you've guessed the key length correctly.

https://crypto.stackexchange.com/questions/8115/repeating-key-xor-and-hamming-distance
