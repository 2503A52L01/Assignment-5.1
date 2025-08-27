def main():
    from support import support_reply

    name = input("Enter your name: ")
    title = input("Enter your title : ")

    response = support_reply(name, title)
    print(response)

if __name__ == "__main__":
    main()
