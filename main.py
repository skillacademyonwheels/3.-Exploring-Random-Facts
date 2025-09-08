import requests


url1 = "http://numbersapi.com/random/date"
url2 = "http://numbersapi.com/56/math"
url3 = "http://numbersapi.com/random/year"
url4 = "http://numbersapi.com/random/trivia"


def fetch_fact(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to retrieve data: {response.status_code}"

def main():

 print("Fetching a random date fact...")

 while True:
        print("\nSelect a URL to fetch a fact:")
        print("1. Random Date Fact")
        print("2. Math Fact about 56")
        print("3. Random Year Fact")
        print("4. Random Trivia Fact")
        print("5. Exit")
        choice = int(input("Choose a URL (1-4 / 5 for Exit): "))

        if choice == 1:
            fact = fetch_fact(url1)
            print(f"Date Fact: {fact}")
        elif choice == 2:
            fact = fetch_fact(url2)
            print(f"Math Fact: {fact}")
        elif choice == 3:
            fact = fetch_fact(url3)
            print(f"Year Fact: {fact}")
        elif choice == 4:
            fact = fetch_fact(url4)
            print(f"Trivia Fact: {fact}")
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()

# https://github.com/skillacademyonwheels/3.-Exploring-Random-Facts.git