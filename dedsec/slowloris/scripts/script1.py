import requests

def main():
    site = ‘http://INSERT IP ADDRESS THAT YOU ANSWERED FROM STEP 8’
    r = requests.get(site)
    print(r.text)

if __name__ ==’__main__’:
    main()
