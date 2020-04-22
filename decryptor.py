import base64
import hashlib

print("-"*50)
print("-"*4,"Encryption & Decryption with ASCII Model","-"*4)
print("-"*50)

pilih = input("Do You Want to Encrypt(E) or Decrypt(D) ? ")
def decryptor():
    if pilih == "E" or pilih == "Encrypt":
        print("-" * 7, "I Have Some Option Ecryption Mode", "-" * 8)
        print(" SHA1---SHA2---Caesar---BASE64---ASCII---Reverse ")
        pilih_mode_enkripsi = input("Choose Encryption Mode : ")

        if pilih_mode_enkripsi == "1" or pilih_mode_enkripsi == "SHA1" or pilih_mode_enkripsi == "sha1":
            data_input_sha1 = input("Input Data Do You Want to Encrypt : ")
            konvert = hashlib.sha1(data_input_sha1.encode())
            print(f"Encrypted Succesfully : {konvert.hexdigest()}")
            print("FYI Encrypted Message SHA1 Called 'Hash'")

        elif pilih_mode_enkripsi == "2" or pilih_mode_enkripsi == "SHA2" or pilih_mode_enkripsi == "sha2":
            pass

        elif pilih_mode_enkripsi == "3" or pilih_mode_enkripsi == "Caesar" or pilih_mode_enkripsi == "caesar":
            data_input_enkripsi_caesar = input("Input Data Do You Want to Encrypt : ")
            data_enkripsi_caesar = ""

            key_lower = "abcdefghijklmnopqrstuvwxyz"
            key_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            offset = 4

            for i in data_input_enkripsi_caesar:
                if i in key_lower:
                    l = (key_lower.index(i) + offset) % 26
                    data_enkripsi_caesar += key_lower[l]

                elif i not in key_lower and i not in key_upper:
                    data_enkripsi_caesar += i

                elif i in key_upper:
                    l = (key_upper.index(i) + offset) % 26
                    data_enkripsi_caesar += key_upper[l]

            print(f"Data Encrypted : {data_enkripsi_caesar}")
            # path = "C:\\Caesar"
            # mode = "w"
            # f = open(path, mode)


        elif pilih_mode_enkripsi == "4" or pilih_mode_enkripsi == "BASE64" or pilih_mode_enkripsi == "base64":
            data_input_enkripsi_base64 = input("Input Data Do You Want to Encrypt : ")

            data_enkripsi_base64 = base64.b64encode(data_input_enkripsi_base64.encode())
            data_enkripsi_base64 = str(data_enkripsi_base64)
            print(f"Data Encrypted : {data_enkripsi_base64[2:-1]}")

        elif pilih_mode_enkripsi == "5" or pilih_mode_enkripsi == "ASCII" or pilih_mode_enkripsi == "ascii":
            data_input_enkripsi = input("Input Data Do You Want to Encrypt : ")
            data_enkripsi = []
            for i in data_input_enkripsi:
                l = ord(i)
                data_enkripsi.append(l)

            # print(data_enkripsi)

            data_kosong = ""

            for data_enkripsi_final in data_enkripsi:
                z = str(data_enkripsi_final)
                data_kosong += z + " "

            print(f"Data Encrypted : {data_kosong}")

        elif pilih_mode_enkripsi == "6" or pilih_mode_enkripsi == "REVERSE" or pilih_mode_enkripsi == "reverse":
            data_input_enkripsi_reverse = input("Input Data Do You Want to Encrypt : ")
            data_enkripsi_konversi_reverse = len(data_input_enkripsi_reverse) - 1
            data_enkripsi_reverse = ""

            while data_enkripsi_konversi_reverse >= 0:
                data_enkripsi_reverse += data_input_enkripsi_reverse[data_enkripsi_konversi_reverse]
                data_enkripsi_konversi_reverse -= 1

            print(f"Encrypted Succesfully : {data_enkripsi_reverse}")

        else:
            print("Type \"Help\" For More Information !!!")

    elif pilih == "D" or pilih == "Decrypt":
        print("-" * 7, "I Have Some Option Decryption Mode", "-" * 8)
        print(" SHA1---SHA2---Caesar---BASE64---ASCII---Reverse ")
        pilih_mode_dekripsi = input("Choose Decryption Mode : ")

        if pilih_mode_dekripsi == "1" or pilih_mode_dekripsi == "SHA1" or pilih_mode_dekripsi == "sha1":
            pass

        elif pilih_mode_dekripsi == "2" or pilih_mode_dekripsi == "SHA2" or pilih_mode_dekripsi == "sha2":
            pass

        elif pilih_mode_dekripsi == "3" or pilih_mode_dekripsi == "Caesar" or pilih_mode_dekripsi == "caesar":
            data_input_dekripsi_caesar = input("Input Encrypted Data : ")
            data_dekripsi_caesar = ""

            key1 = "abcdefghijklmnopqrstuvwxyz"
            key2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            offset = 4

            for i in data_input_dekripsi_caesar:
                if i in key1:
                    l = (key1.index(i) - offset) % 26
                    data_dekripsi_caesar += key1[l]

                if i in key2:
                    l = (key2.index(i) - offset) % 26
                    data_dekripsi_caesar += key2[l]

                if i not in key1 and i not in key2:
                    data_dekripsi_caesar += i

            print(f"Decrypting Succesfully : {data_dekripsi_caesar}")

        elif pilih_mode_dekripsi == "4" or pilih_mode_dekripsi == "BASE64" or pilih_mode_dekripsi == "base64":
            print("-" * 4, "Input Encrypted Data With Format Base64", "-" * 4)
            data_input_dekripsi_base64 = input("Input Encrpted Data : ")
            data_dekripsi_base64 = base64.b64decode(data_input_dekripsi_base64)
            data_dekripsi_base64 = str(data_dekripsi_base64)
            print(f"Decrypting Succesfully : {data_dekripsi_base64[2:-1]}")

        elif pilih_mode_dekripsi == "5" or pilih_mode_dekripsi == "ASCII" or pilih_mode_dekripsi == "ascii":
            print("-" * 4, "Input Encrypted Data With 'Space'", "-" * 4)
            data_input_dekripsi = input("Input Encrypted Data : ")
            data_input_dekripsi_split = data_input_dekripsi.split(" ")

            hasil_dekripsi = ""

            for i in data_input_dekripsi_split:
                l = int(i)
                l = chr(l)
                hasil_dekripsi += l

            print(f"Decrypting Succesfully : {hasil_dekripsi}")

        elif pilih_mode_dekripsi == "6" or pilih_mode_dekripsi == "REVERSE" or pilih_mode_dekripsi == "reverse":
            print("-" * 4, "Input Encrypted Data With Format Reverse", "-" * 4)
            data_input_dekripsi_reverse = input("Input Encrypted Data : ")
            data_dekripsi_reverse = ""
            data_dekripsi_konversi_reverse = len(data_input_dekripsi_reverse) - 1

            while data_dekripsi_konversi_reverse >= 0:
                data_dekripsi_reverse += data_input_dekripsi_reverse[data_dekripsi_konversi_reverse]
                data_dekripsi_konversi_reverse -= 1

            print(f"Decryption Succesfuly : {data_dekripsi_reverse}")

        else:
            print("Type \"Help\" For More Information !!!")

    elif pilih == "Help" or pilih == "H":
        print("-" * 47)
        print("Type \"E\" or \"Encrypt\" to Choose Encryption Mode")
        print("Type \"D\" or \"Decrypt\" to Choose Decryption Mode")
        print("-" * 9, "Type \"Exit\" or \"X\" to Quit", "-" * 10)

    else:
        print("Type \"Help\" or \"H\" to More Information")
        
        
 decryptor()
