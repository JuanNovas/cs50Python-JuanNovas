text = input("File name: ").lower().strip()

dot = text.rfind(".")
try:
    extension = text[dot + 1:]
    match extension:
        case "gif" | "jpeg" | "png":
            print(f"image/{extension}")
        case "jpg":
            print("image/jpeg")
        case "pdf" | "zip":
            print(f"application/{extension}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
except:
    print("application/octet-stream")
