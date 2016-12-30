import requests

def main():
  req = requests.get('https://api.darksky.net/forecast/80ae193703675485dfb06172c87a3911/39.188771, -96.549764')
  reqJson = req.json()
  print(reqJson['hourly']['data'][0])

if __name__ == '__main__':
  main()
