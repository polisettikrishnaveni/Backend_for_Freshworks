import main as x
#importing the main file("main" is the name of the file I have used) as a library

x.Create("krishnaveni",50)
#to Create a key with key_name,value given and with no time-to-live property

x.Create("polisetti",80,3000)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

x.Read("krishnaveni")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

x.Read("krishna veni")
#it returns an error message as the key is not in the required format.

x.Read("polisetti")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

x.Create("krishnaveni",60)
#it returns an ERROR since the key_name already exists in the database

x.Delete("krishnaveni")
#it deletes the respective key and its value from the database(memory is also freed)

x.Delete("kri$hnaveni")
#it returns an error message as the keyname contains special character.

#the code also returns other errors like
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
