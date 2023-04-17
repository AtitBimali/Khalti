import requests
import json

url = "https://khalti.com/api/v2/service/use/khanepani/search/"

payload = json.dumps({
  "counter": "", #counter code
  "customer_code": "", #customer code
  "amount": "",
  "counter_name": "" # counter name
})
headers = {
  'Connection': 'keep-alive',
  'DEVICEID': '',
  'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
  'DNT': '1',
  'sec-ch-ua-mobile': '?0',
  'Authorization': 'ACCESS TOKEN HERE', # access token
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
  'Content-Type': 'application/json',
  'Accept': 'application/json, text/plain, */*',
  'sec-ch-ua-platform': '"Windows"',
  'Origin': 'https://web.khalti.com',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://web.khalti.com/',
  'Accept-Language': 'en,en-GB;q=0.9,ne;q=0.8,en-US;q=0.7',
  'Cookie': 'VALID COOKIE HERE'  #cookie
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
