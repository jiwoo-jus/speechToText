import os


# google cloud Speech-toText 서비스키 발급받은 후 로컬 키 경로 입력.
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"C:\your_path\your_key.json"

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code="ko-KR"
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result()

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"{}".format(result.alternatives[0].transcript))
        # print("Confidence: {}".format(result.alternatives[0].confidence))


# google cloud storage에 대용량 오디오파일 업로드 후 해당 파일의 gcp path 입력
if __name__ == "__main__":
    transcribe_gcs("gs://your_bucket/your_file.mp3")
