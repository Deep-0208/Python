key1 = "Make a lot of money"
key2 = "Buy now"
key3 = "Subscibe this"
key4 = "Click this"

message = input("Enter Message :")


if((key1.lower() in message.lower()) or (key2.lower() in message.lower()) or (key3.lower() in message.lower())):
    print("This message is spam")
else:
    print("This message is not spam")