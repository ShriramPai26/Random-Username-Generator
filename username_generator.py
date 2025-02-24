import random
import string


adjectives = ["Cool", "Happy", "Swift", "Brave", "Clever", "Epic", "Mighty", "Jolly"]
nouns = ["Tiger", "Dragon", "Falcon", "Panda", "Warrior", "Knight", "Rider", "Samurai"]
def generate_username(add_number=True, add_special=False):
    
    adj = random.choice(adjectives)  
    noun = random.choice(nouns)  
    username = adj + noun 

    if add_number:
        username += str(random.randint(10, 99))  

    if add_special:
        username += random.choice(string.punctuation)  

    return username
def save_to_file(username, filename="usernames.txt"):
    """Saves the generated username to a file."""
    with open(filename, "a") as file:
        file.write(username + "\n")
def main():
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))

    add_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    print("\nGenerated Usernames:")
    for _ in range(num_usernames):
        username = generate_username(add_number, add_special)
        print(username)
        save_to_file(username)  

    print("\nUsernames saved to 'usernames.txt'.")
if __name__ == "__main__":
    main()
