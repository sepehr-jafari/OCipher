# OCipher Encryption Algorithm

This repository contains the implementation of the OCipher encryption algorithm, including its key management and round function algorithms.

## Algorithm Specifications

### 2-1 Algorithm Details

- **Block Length:** 64 bits
- **Key Length:** 128 bits
- **Number of Rounds:** 15

## Key Management Algorithm

### Input:
- A 128-bit key

### Output:
- 16 subkeys, each 32 bits

### Steps:

1. **Step 1:**
   - Divide the initial 128-bit key into four 32-bit subkeys (the first subkey is obtained).
   - Rotate the key left by 17 bits.
   - Divide the key again into four 32-bit subkeys.

2. **Step 2:**
   - Repeat the above process to obtain the next subkey until reaching the 16th subkey.
   - For the final subkey, sum the primary key from Table P with the values from register 2.


### P Table:

| 0x1640e3d3 | 0x6e163697 | 0x5449a36f | 0xaa08839e1 |
|------------|------------|------------|-------------|
| 0xf2bc18f  | 0xf1290dc7 | 0x2756d43b | 0xd9155ea3  |
| 0xa5fc3c53 | 0xaa0363cf | 0x96c10b36a| 0x3cb574b2  |
| 0x2ffd72db | 0xf4933d7e | 0x7c72e993 | 0x7d84a5c3  |

## OCipher Encryption Algorithm

### Steps:

1. **Step 1:**
   - Calculate 16 subkeys of 32 bits according to the key management algorithm.
   - Divide the plaintext into two 32-bit halves: (L<sub>i</sub>, R<sub>i</sub>).

2. **Step 2:**
   - For 14 rounds, compute the following equations:
     - R<sub>i+1</sub> = L<sub>i</sub>
     - L<sub>i+1</sub> = f(L<sub>i</sub>, K<sub>i</sub>) ⊕ R<sub>i</sub>

### Round Function Algorithm

### Input:
- 32-bit L<sub>i</sub> from the left half of the plaintext

### Output:
- 32-bit T

### Steps:

* **Step 1:**
   - Add the 32-bit left half L<sub>i</sub> and the 32-bit subkey K<sub>i</sub> from the key management algorithm.
   - Split the 64-bit result into eight 8-bit parts: T'.

* **Step 2:**
   - Apply the s-box substitution:
     - S<sub>1</sub>(T'<sub>1</sub>) → O1, S<sub>2</sub>(T'<sub>2</sub>) → O2, S<sub>3</sub>(T'<sub>3</sub>) → O3, S<sub>4</sub>(T'<sub>4</sub>) → O4.

* **Step 3:**
   - Sum the first and second s-box outputs and the third and fourth s-box outputs.
   - Combine and permute the result according to the permutation table.

* **Step 4:**
   - Sum the final results and adjust based on the permutation table to generate the final 32-bit output T.



### permutation: 
|  |  |  |  |
|--|--|--|--|
|21|20|7 |16|
|17|28|12|29|
|26|23|15|1 |
|10|31|18|5 |
|14|24|8 |2 |
|9 |3 |27|32|
|6 |30|13|19|
|25|4 |11|22|

Note: s-box does not consider bits 0 and 5. Then, with bit 6 and 7, it specifies the row and using bit 1, 2, 3, 4 the column in the table.


