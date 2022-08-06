import requests
from donotloook import API_KEY_ASSEMBLYAI
import time
import sys

#upload
upload_end = 'https://api.assemblyai.com/v2/upload'
trans_end = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY_ASSEMBLYAI}

filename = sys.argv[1]

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    up_response = requests.post(upload_end, headers=headers, data=read_file(filename))

    audio_url = up_response.json()['upload_url']
    return audio_url

#transcript
def transcribe(audio_url):
    json = { "audio_url": audio_url }

    trans_response = requests.post(trans_end, json=json, headers=headers)
    trans_id = trans_response.json()['id']
    return trans_id


#poll( to ask if job is done or not)
def polling(job_id):
    poll_endpoint = trans_end + '/' + job_id
    poll_res = requests.get(poll_endpoint, headers=headers)
    return poll_res.json()

def get_trans_res(audio_url):
    trans_id = transcribe(audio_url)
    while True:
        data = polling(trans_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print('Waiting 30 seconds...')
        time.sleep(30)

#save
def save(audio_url):
    data, error = get_trans_res(audio_url)

    if data:
        text_file = filename.split()[0] + ".txt"
        with open(text_file, 'w') as f:
            f.write(data['text'])
        print('Transcription Saved!!!')
    else:
        print("Oh no!!", error)