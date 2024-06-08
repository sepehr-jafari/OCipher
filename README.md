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
# S-Boxs
### S1
|          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 28958677 | 3b8f4898 | 6b4bb9af | c4bfe81b | 66282193 | 61d809cc | fb21a991 | 487cac60 | 5dec8032 | ef845d5d | e98575b1 | dc262302 | eb651b88 | 23893e81 | d396acc5 | 0f6d6ff3 |
| 9e1f9b5e | 21c66842 | f6e96c9a | 670c9c61 | abd388f0 | 6a51a0d2 | d8542f68 | 960fa728 | ab5133a3 | 6eef0b6c | 137a3be4 | ba3bf050 | 7efb2a98 | a1f1651d | 39af0176 | 66ca593e |
| 3b8b5ebe | e06f75d8 | 85c12073 | 401a449f | 56c16aa6 | 4ed3aa62 | 363f7706 | 1bfedf72 | 429b023d | 37d0d724 | d00a1248 | db0fead3 | 49f1c09b | 075372c9 | 80991b7b | 25d479d8 |
| 04c006ba | c1a94fb6 | 409f60c4 | 5e5c9ec2 | 196a2463 | 68fb6faf | 3e6c53b5 | 1339b2eb | 3b52ec6f | 6dfc511f | 9b30952c | cc814544 | af5ebd09 | bee3d004 | de334afd | 660f2807 |

### S2
|          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| e93d5a68 | 948140f7 | f64c261c | 94692934 | 411520f7 | 7602d4f7 | bcf46b2e | d4a20068 | d4082471 | 3320f46a | 43b7d4b7 | 500061af | 1e39f62e | 97244546 | 14214f74 | bf8b8840 |
| bfbc09ec | 03bd9785 | 7fac6dd0 | 31cb8504 | 96eb27b3 | 55fd3941 | da2547e6 | abca0a9a | 28507825 | 530429f4 | 0a2c86da | e9b66dfb | 68dc1462 | d7486900 | 680ec0a4 | 27a18dee |
| aace1e7c | d3375fec | ce78a399 | 406b2a42 | 20fe9e35 | d9f385b9 | ee39d7ab | 3b124e8b | 1dc9faf7 | 4b6d1856 | 26a36631 | eae397b2 | 3a6efa74 | dd5b4332 | 6841e7f7 | ca7820fb |
| 55533a3a | 20838d87 | fe6ba9b7 | d096954b | 55a867bc | a1159a58 | cca92963 | 99e1db33 | a62a4a56 | 3f3125f9 | 5ef47e1c | 9029317c | fdf8e802 | 04272f70 | 80bb155c | 05282ce3 |

### S3
|          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 3a39ce37 | d3faf5cf | abc27737 | 5ac52d1b | 5cb0679e | 4fa33742 | d3822740 | 99bc9bbe | d5118e9d | bf0f7315 | d62d1c7e | c700c47b | b78c1b6b | 21a19045 | b26eb1be | 6a366eb4 |
| 530ff8ee | 468dde7d | d5730a1d | 4cd04dc6 | 2939bbdb | a9ba4650 | ac9526e8 | be5ee304 | a1fad5f0 | 6a2d519a | 63ef8ce2 | 9a86ee22 | c089c2b8 | 43242ef6 | a51e03aa | 9cf2d0a4 |
| 2826a2f9 | a73a3ae1 | 4ba99586 | ef5562e9 | c72fefd3 | f752f7da | 3f046f69 | 77fa0a59 | 80e4a915 | 87b08601 | 9b09e6ad | 3b3ee593 | e990fd5a | 9e34d797 | 2cf0b7d9 | 022b8b51 |
| e019a5e6 | 47b0acfd | ed93fa9b | e8d3c48d | 283b57cc | f8d56629 | 79132e28 | 785f0191 | ed756055 | f7960e44 | e3d35e8c | 15056dd4 | 88f46dba | 03a16125 | 0564f0bd | c3eb9e15 |

### S4
|          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| ed545578 | 08fca5b5 | d83d7cd3 | 4dad0fc4 | 1e50ef5e | b161e6f8 | a28514d9 | 6c51133c | 6fd5c7e7 | 56e14ec4 | 362abfce | ddc6c837 | d79a3234 | 92638212 | 670efa8e | 406000e0 |
| ed545578 | 08fca5b5 | d83d7cd3 | 4dad0fc4 | 1e50ef5e | b161e6f8 | a28514d9 | 6c51133c | 6fd5c7e7 | 56e14ec4 | 362abfce | ddc6c837 | d79a3234 | 92638212 | 670efa8e | 406000e0 |
| f0177a28 | c0f586e0 | 006058aa | 30dc7d62 | 11e69ed7 | 2338ea63 | 53c2dd94 | c2c21634 | bbcbee56 | 90bcb6de | ebfc7da1 | ce591d76 | 6f05e409 | 4b7c0188 | 39720a3d | 7c927c24 |
| 61d99735 | a969a7aa | c50c06c2 | 5a04abfc | 800bcadc | 9e447a2e | c3453484 | fdd56705 | 0e1e9ec9 | db73dbd3 | 105588cd | 675fda79 | e3674340 | c5c43465 | 713e38d8 | 3d28f89e |

# OCipher Structure
<div align='center'>
   <img src="https://github.com/sepehr-jafari/OCipher/blob/main/img/OC%20Feistel.PNG" width="200" hight="500">
</div>

# One Round Of OCipher
<div align='center'>
   <img src="https://github.com/sepehr-jafari/OCipher/blob/main/img/One%20Round%20Of%20OC.PNG " width="300" hight="300">
</div>

