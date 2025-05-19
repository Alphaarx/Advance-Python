def http_status(status):
       match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _:
            print("Unknown Status")

# Example usage
http_status(404)  # Output: Not Found
print(__name__) #__main__