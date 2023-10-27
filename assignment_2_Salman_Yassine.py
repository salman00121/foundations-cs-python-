from bs4 import BeautifulSoup
import sys

def main():
    print("1 Count Digits")
    print("2 Find Max")
    print("3.1 Count Tags ")
    print("3.2 Count Normalized Columns")
    print("4 Exit")

    choice = input("Enter a choice: " )

    if choice == "1":

        def Countdigits(n):
            if n < 10:
                return 1
            else:
                return 1 + Countdigits(n // 10)

        user_input = input("Enter an integer: ")

        number1 = int(user_input)
        
        count1 = Countdigits(number1)
        print(f"Output: , {count1}")

    if choice == "2":

        def findmax(lst):
            if not lst:
                return 0
            if len(lst) == 1:
                return lst[0]
            else:
                max1 = findmax(lst[1:])
                return lst[0] if lst[0] > max1 else max1

        userInput = input("Enter a list of integers: ")

        inputList = [int(num) for num in userInput.split()]

        maxValue = findmax(inputList)
        print("Output:", maxValue)


    if choice == "3.1":

        code = """
            <html>
            <head>
            <title>My Website</title>
            </head>
            <body>
            <h1>Welcome to my website!</h1>
            <p>Here you'll find information about me and my hobbies.</p>
            <h2>Hobbies</h2>
            <ul>
            <li>Playing guitar</li>
            <li>Reading books</li>
            <li>Traveling</li>
            <li>Writing cool h1 tags</li>
            </ul>
            </body>
            </html>
        """
        soup = BeautifulSoup(code, 'html.parser')

        def countags(tagName, soup):
            tagCount = 0
            

            tag_occurrences = soup.find_all(tagName)

            for tag in tag_occurrences:
                tagCount += 1
                tagCount += countags(tagName, tag)
            
            return tagCount

        tagName = input("Enter the tag to count: ")

        last = countags(tagName, soup)
        print(f"Result of '{tagName}' tag: {last}")


    if choice == "3.2":
        def Count_Normalized_Columns():
            pass
        



    if choice == "4":
        sys.exit()


main()