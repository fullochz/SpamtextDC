import requests
import time
import random

sentences = [
    'I predicted if this project will be growing fast as the strongest crypto in th future.',
    'The project has great prospects.',
    'Certainly at the moment, I believe that this is the best project.',
    'This is definitely going to be HUGE!',
    'As the team has been an inspiration in their innovative approaches towards achieving the project goals and visions.',
    'I am so glad to be part of this.',
    'This project has a very bright future.',
    'Thanks also to the friends and Thanks for shared this wonderful opportunity.',
    'Best wishes for all the team with the opportunity to take part in this big project. I hope this project will develop well and will be on the moon.',
    'I am starting to like this project. I just hope and pray this project is successful, am going to try my luck.',
    'Your project is very good. The whitepaper is also very clear. I hope your project can be successful and successful in the future. I also hope the community can grow even bigger than now.'
]
message = random.choice(sentences)
channel_id = input('Masukan chanel id\t\t: ')
waktu = int(input('Masukan waktu jeda\t\t: '))
auth_token = input('Masukkan Authorization token bot: ')
headers = {
    'Authorization': auth_token,
    'Content-Type': 'application/json'
}
while True:
    message = random.choice(sentences)
    payload = {
       'content': message
    }
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
    if response.status_code == 200:
       print('Pesan berhasil dikirim!')
    else:
       print('Pesan gagal dikirim!')
    time.sleep(waktu)
