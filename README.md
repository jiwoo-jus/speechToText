# speechToText
비디오/오디오 녹취록 생성기

<br>

## mp4 to mp3

대상 파일이 영상일 경우 오디오로 전환하여 stt를 실행합니다.

```bash
$ pip install moviepy
```

1. 프로젝트 폴더 내부에 mp4파일을 위치시킨다.

2. [mp4tomp3.py](https://github.com/jiwoo-jus/speechToText/blob/137fd554c0e7708a3de27bf0fa3bcc43d77cdcdd/mp4tomp3.py) `filename` 을 수정한다. 

<br>

## speech to text

```bash
pip install google-cloud-speech
```

**1. Google Cloud Speech-to-Text API 서비스 계정 키 등록**

1. 서비스 계정 키를 json파일로 발급받는다. [참고](https://webnautes.tistory.com/1247)

2. [main.py](https://github.com/jiwoo-jus/speechToText/blob/137fd554c0e7708a3de27bf0fa3bcc43d77cdcdd/main.py) **line5** 에 발급받은 서비스 계정 키 로컬 경로를 입력한다. *서비스 계정 키를 환경변수에 등록했다면 **line5** 를 주석처리한다.*

**2. 대용량 오디오 파일 google cloud storage에 업로드**

1. 오디오 파일을 storage에 업로드한다. [참고](https://cloud.google.com/storage/docs/uploading-objects/?hl=ko)

2. [main.py](https://github.com/jiwoo-jus/speechToText/blob/137fd554c0e7708a3de27bf0fa3bcc43d77cdcdd/main.py) **line36** 에 해당 파일의 gcp 경로를 입력한다.
