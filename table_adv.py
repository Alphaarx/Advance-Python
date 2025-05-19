with open("table.txt","a") as f:
    n=int(input("Enter a number to generate its multiplication table: "))
    table =[n*i for i in range(1,11)]
    # for i in table:
    #     f.write(f"{i}\n")
    f.write(str(table)+"\n")
    print("Table written to file successfully.")
