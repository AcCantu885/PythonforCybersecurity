from passlib.hash import sha256_crypt

#Load our passwaor attempts and our hashed values

shadow_file = 'shadow.txt'
password_list = 'password123.txt'

#Create a function that will crack passwords
def crack_password(shadow_file, password_list):
    with open(shadow_file, 'r') as sf, open(password_list, 'r') as pl:
        shadow_lines = sf.readlines()
        passwords = pl.readlines()


        for line in shadow_lines:
            #Split line into parts
            parts = line.split(':')
            #Ensure that there are at least two parts
            if len(parts) < 2:
                print("Skipping malformed line:", {line})
                continue
            username = parts[0] 
            hashed_password = parts[1].strip()
        print(f'Checking for user: {username}')
        for password in passwords:
            password = password.strip()
            print(f"Trying password: {passwords}")
            if sha256_crypt.verify(password, hashed_password):
                print(f"Password for {username} found: {password}")
                break


#Call the function
crack_password(shadow_file, password_list)
