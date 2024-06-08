class OCipher:
    
    def __init__(self) -> None:
        self._P = [
            ["0x1640e3d3", "0x6e163697", "0x5449a36f", "0xa08839e1"],
            ["0xf2bcc18f", "0xf1290dc7", "0x2765d43b", "0xd9155ea3"],
            ["0xa5fc3c53", "0xaa0363cf", "0x9c10b36a", "0x3cb574b2"],
            ["0x2ffd72db", "0xf4933d7e", "0x7c72e993", "0x7d84a5c3"]
        ]
        self._S1 = [
            ["28958677", "3b8f4898", "6b4bb9af", "c4bfe81b", "66282193", "61d809cc", "fb21a991", "487cac60", "5dec8032", "ef845d5d", "e98575b1", "dc262302", "eb651b88", "23893e81", "d396acc5", "0f6d6ff3"],
            ["9e1f9b5e", "21c66842", "f6e96c9a", "670c9c61", "abd388f0", "6a51a0d2", "d8542f68", "960fa728", "ab5133a3", "6eef0b6c", "137a3be4", "ba3bf050", "7efb2a98", "a1f1651d", "39af0176", "66ca593e"],
            ["3b8b5ebe", "e06f75d8", "85c12073", "401a449f", "56c16aa6", "4ed3aa62", "363f7706", "1bfedf72", "429b023d", "37d0d724", "d00a1248", "db0fead3", "49f1c09b", "075372c9", "80991b7b", "25d479d8"],
            ["04c006ba", "c1a94fb6", "409f60c4", "5e5c9ec2", "196a2463", "68fb6faf", "3e6c53b5", "1339b2eb", "3b52ec6f", "6dfc511f", "9b30952c", "cc814544", "af5ebd09", "bee3d004", "de334afd", "660f2807"]
        ]
        self._S2 = [
            ["e93d5a68", "948140f7", "f64c261c", "94692934", "411520f7", "7602d4f7", "bcf46b2e", "d4a20068", "d4082471", "3320f46a", "43b7d4b7", "500061af", "1e39f62e", "97244546", "14214f74", "bf8b8840"],
            ["bfbc09ec", "03bd9785", "7fac6dd0", "31cb8504", "96eb27b3", "55fd3941", "da2547e6", "abca0a9a", "28507825", "530429f4", "0a2c86da", "e9b66dfb", "68dc1462", "d7486900", "680ec0a4", "27a18dee"],
            ["aace1e7c", "d3375fec", "ce78a399", "406b2a42", "20fe9e35", "d9f385b9", "ee39d7ab", "3b124e8b", "1dc9faf7", "4b6d1856", "26a36631", "eae397b2", "3a6efa74", "dd5b4332", "6841e7f7", "ca7820fb"],
            ["55533a3a", "20838d87", "fe6ba9b7", "d096954b", "55a867bc", "a1159a58", "cca92963", "99e1db33", "a62a4a56", "3f3125f9", "5ef47e1c", "9029317c", "fdf8e802", "04272f70", "80bb155c", "05282ce3"]
        ]
        self._S3 = [
            ["3a39ce37", "d3faf5cf", "abc27737", "5ac52d1b", "5cb0679e", "4fa33742", "d3822740", "99bc9bbe", "d5118e9d", "bf0f7315", "d62d1c7e", "c700c47b", "b78c1b6b", "21a19045", "b26eb1be", "6a366eb4"],
            ["530ff8ee", "468dde7d", "d5730a1d", "4cd04dc6", "2939bbdb", "a9ba4650", "ac9526e8", "be5ee304", "a1fad5f0", "6a2d519a", "63ef8ce2", "9a86ee22", "c089c2b8", "43242ef6", "a51e03aa", "9cf2d0a4"],
            ["2826a2f9", "a73a3ae1", "4ba99586", "ef5562e9", "c72fefd3", "f752f7da", "3f046f69", "77fa0a59", "80e4a915", "87b08601", "9b09e6ad", "3b3ee593", "e990fd5a", "9e34d797", "2cf0b7d9", "022b8b51"],
            ["e019a5e6", "47b0acfd", "ed93fa9b", "e8d3c48d", "283b57cc", "f8d56629", "79132e28", "785f0191", "ed756055", "f7960e44", "e3d35e8c", "15056dd4", "88f46dba", "03a16125", "0564f0bd", "c3eb9e15"]
        ]
        self._S4 = [
            ["ed545578", "08fca5b5", "d83d7cd3", "4dad0fc4", "1e50ef5e", "b161e6f8", "a28514d9", "6c51133c", "6fd5c7e7", "56e14ec4", "362abfce", "ddc6c837", "d79a3234", "92638212", "670efa8e", "406000e0"],
            ["ed545578", "08fca5b5", "d83d7cd3", "4dad0fc4", "1e50ef5e", "b161e6f8", "a28514d9", "6c51133c", "6fd5c7e7", "56e14ec4", "362abfce", "ddc6c837", "d79a3234", "92638212", "670efa8e", "406000e0"],
            ["f0177a28", "c0f586e0", "006058aa", "30dc7d62", "11e69ed7", "2338ea63", "53c2dd94", "c2c21634", "bbcbee56", "90bcb6de", "ebfc7da1", "ce591d76", "6f05e409", "4b7c0188", "39720a3d", "7c927c24"],
            ["61d99735", "a969a7aa", "c50c06c2", "5a04abfc", "800bcadc", "9e447a2e", "c3453484", "fdd56705", "0e1e9ec9", "db73dbd3", "105588cd", "675fda79", "e3674340", "c5c43465", "713e38d8", "3d28f89e"]
        ]
        
        self._P_box = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26,
                       5, 15, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19,
                       13, 30, 6, 22, 11, 7, 25]
        
    def _S_box_1(self, eight_bit:str)->str:
        bin_input = bin(int(eight_bit, 16))[2:].zfill(8)
        result = self._S1[int(f'{bin_input[6]}{bin_input[7]}', 2)][int(bin_input[1:5], 2)]
        return result
    
    def _S_box_2(self, eight_bit:str)->str:
        bin_input = bin(int(eight_bit, 16))[2:].zfill(8)
        result = self._S2[int(f'{bin_input[6]}{bin_input[7]}', 2)][int(bin_input[1:5], 2)]
        return result

    def _S_box_3(self, eigth_bit:str)->str:
        bin_input = bin(int(eigth_bit, 16))[2:].zfill(8)
        result = self._S3[int(f'{bin_input[6]}{bin_input[7]}', 2)][int(bin_input[1:5], 2)]
        return result
    
    def _S_box_4(self, eight_bit:str)->str:
        bin_input = bin(int(eight_bit, 16))[2:].zfill(8)
        result = self._S3[int(f'{bin_input[6]}{bin_input[7]}', 2)][int(bin_input[1:5], 2)]
        return result
    
    def _Permutation(self, input:str)->str:
        on_op_input = bin(int(input, 16))[2:].zfill(32)
        result = ""
        
        for i in range(0,32):
            result += on_op_input[self._P_box[i]-1]
        
        return hex(int(result,2))
    
    def _xor(self, first, second):
        f = int(first, 16)
        s = int(second, 16)
        result = hex(f ^ s)
        return result
    
    def _add(self, first, second):
        f = int(first, 16)
        s = int(second, 16)
        return hex( (f + s) % (2 ** 32) )
    
    def _cyclic_shift(self, number:str, step:int)->str:
        bin_number = bin(int(number,16))[2:].zfill(128)
        
        new_right = bin_number[0:step]
        new_left = bin_number[step:]
        
        shifted = hex(int(f'{new_left}{new_right}', 2))
        
        return shifted
       
    def _spliter(self, number:str, chunk_size:int, pad_size:int)->list:
        bin_number = bin(int(number, 16))[2:].zfill(pad_size)
        
        n = len(bin_number)

        result = []
        
        for i in range(0,n, chunk_size):
            result.append(hex(int(bin_number[i:i+chunk_size], 2)))
        
        return result
    
    def _plaintext_chunk(self, plaintext:str)->list:
        bin_plaintext = bin(int(plaintext, 16))[2:]
        bin_length = len(bin_plaintext)
    
        result = [] 
         
        for i in range(0,bin_length, 64):
            result.append(hex(int(bin_plaintext[i:i+64], 2)))

        return result
    
    def _key_schedule(self, key:str)->list:
        
        on_op_key = key
        sub_keys = []
        
        for i in range(0,4):
            p = self._spliter(on_op_key, 32, 128)
            
            for j in range(0, 4):
                sub_keys.append(self._xor(self._P[i][j], p[j]))
            
            on_op_key = self._cyclic_shift(on_op_key, 17)

        return sub_keys
    
    def _round_functoin(self, plaintext:str, key:str)->str:
        plain_on_op = self._xor(plaintext, key)
        splited = self._spliter(plain_on_op, 8, 32)
        
        S1_out = self._S_box_1(splited[0])
        S2_out = self._S_box_2(splited[1])
        S3_out = self._S_box_3(splited[2])
        S4_out = self._S_box_4(splited[3])
        
        sum_S1_S4 = self._add(S1_out, S4_out)
        sum_S2_S3 = self._add(S2_out, S3_out)
        
        xor_sum1_sum2 = self._xor(sum_S1_S4, sum_S2_S3)
        
        result = self._Permutation(xor_sum1_sum2)
        
        return result
    
    def _encrypt(self, plaintext:str, key:str)->str:
        keys = self._key_schedule(key)
        splited = self._spliter(plaintext, 32, 64)
        
        X_left = splited[0]
        X_right = splited[1]
        
        for i in range(0,14):
            f_out = self._round_functoin(X_left, keys[i])
            xor_f_l = self._xor(f_out, X_right)
            
            X_right = X_left
            X_left = xor_f_l
        
        # last round
        xor_left = self._xor(X_left, keys[14])
        xor_right = self._xor(X_right, keys[15])
        
        X_left = xor_right
        X_right = xor_left
        
        result = hex(int(X_left[2:]+X_right[2:], 16))
        
        return result
    
    def _Ochiper(self, plaintext, key)->str:
        return self._encrypt(plaintext, key)
    
    def EBC_encrypt(self, plaintext:str, key)->str:
        plaintext_bolcks = self._plaintext_chunk(plaintext)
        
        result = ''
        for p in plaintext_bolcks:
            result += self._Ochiper(p, key)[2:]
        
        return hex(int(result, 16))


O = OCipher()

plainText = "0xaaaaaaaaffffffff1ca5c5c8b5475132aaaaaaaaffffffff435435457cbbae14aaaaaaaaffffffff"
key = "0xc742f442ef6abbb5654f3b1d41cd2105"

cipher = O.EBC_encrypt(plainText, key)
print("plainText:")
print(plainText)
print("cipherText:")
print(cipher)