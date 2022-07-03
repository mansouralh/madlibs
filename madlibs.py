def main():
	# write your code here
  print("Mad libs where libs get mad.")
  print("Start below:")
  time= input("Enter a number from 1 to 12")
  items= input("Enter a noun (plural)")
  name= input("Enter a name:")
  scream= input("Enter any sentence:")
  scream= scream.upper()
  action= input("Enter a verb:")

  print("The story goes...")


  print(f"It was {time} o'clock when I heard a knock at the door.")
  print(f"I opened the door and there was a box full of {items} with a note saying From Mr. {name}")
  print(f"Just as I closed the door I heard a scream {scream}")
  print(f"I froze in place and all I could do was {action}")
# plural= "dolls"
# name= "stephen sedoll"
# sentence= "the future is made of dolls"
# verb= "shake my head"



if __name__ == '__main__':
	main()