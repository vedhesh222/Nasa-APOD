#Importing Modules
import requests as rq
import webbrowser as wb
from art import *

#Art Work
tprint('NASA-APOD')

#Me
print('[Me: M.Vedhesh Narayanan, Instagram: tek_vedhesh, GitHub: https://github.com/vedhesh222]')
print('')

#Getting Input's
y = int(input('Enter the Year: '))
m = int(input('Enter the Month: '))
d = int(input('Enter the Day: ' ))

#Storing the API Key
apiKey = 'Your API Key'

#Creating a Function
def apod():
    url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date='+str(y) +'-' +str(m) +'-' +str(d)
    pUrl = rq.get(url).json()
    img = (pUrl['url'])
    wb.open(img)

#Running the Function
apod()

#Closing
print('')
c = input('Hit Enter to Exit...')