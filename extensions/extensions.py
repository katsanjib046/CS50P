def main():
    file = input("File name: ").strip(" ").lower()
    dict = {"gif":"image/gif", "jpg":"image/jpeg", "jpeg":"image/jpeg",
    "png":"image/png","pdf":"application/pdf","txt":"text/plain","zip":"application/zip"}
    print(extension_out(file, dict))


def extension_out(file, dict):
    """Takes the input file and finds it extension to determine the MIME"""
    _, _, ext = file.rpartition(".")
    if ext in dict:
        return dict[ext]
    else:
        return "application/octet-stream"
main()