from pydub import AudioSegment

ts_audie = AudioSegment.from_file(".output.ts")
ts_audie.export("output.mp3", format="mp3")

