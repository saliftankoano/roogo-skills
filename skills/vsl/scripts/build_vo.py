#!/usr/bin/env python3
"""Voice-over, scene timeline and word timestamps for a VSL.

Usage:  python3 build_vo.py scenes.json [--lead 0.25 --tail 0.55]
Input   scenes.json  [{"id":"s1","vo":"spoken text, respelled for TTS"}, ...]
Output  vo/<id>.wav (Cartesia Sandrine), vo_mix.wav (loudnorm -16 LUFS),
        timeline.json (scene start/duration), words.json (fal.py transcribe)

Sandrine via Cartesia: key in CARTESIA_API_KEY, or the macOS Keychain item ai.cartesia.api-key (account default).
Respell in the spoken text only: Roogo -> Rohgo, Burkina -> Bourkina, Ouaga -> Waga,
numbers and prices in full words, phone numbers in French pairs.
"""
import json,subprocess,sys,urllib.request,os
scenes=json.load(open(sys.argv[1]))
LEAD=float(sys.argv[sys.argv.index("--lead")+1]) if "--lead" in sys.argv else 0.25
TAIL=float(sys.argv[sys.argv.index("--tail")+1]) if "--tail" in sys.argv else 0.55
FAL=os.environ.get("FAL_TOOL","fal.py")  # path to your fal.py transcription helper (STT with word timestamps)
VOICE="2435841c-fce7-4fd5-aed1-dc7008eb7d20"
os.makedirs("vo",exist_ok=True);os.makedirs("seg",exist_ok=True)
key=os.environ.get("CARTESIA_API_KEY") or subprocess.check_output(["security","find-generic-password","-s","ai.cartesia.api-key","-a","default","-w"]).decode().strip()
def run(c): subprocess.run(c,shell=True,check=True,capture_output=True)
def dur(p): return float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {p}",shell=True))
t=0
lst=open("audio.txt","w")
for s in scenes:
    body=json.dumps({"model_id":"sonic-3.5","transcript":s["vo"],"voice":{"mode":"id","id":VOICE},"language":"fr","output_format":{"container":"wav","encoding":"pcm_s16le","sample_rate":44100}}).encode()
    r=urllib.request.Request("https://api.cartesia.ai/tts/bytes",body,{"Cartesia-Version":"2025-04-16","X-API-Key":key,"Content-Type":"application/json"})
    open(f"vo/{s['id']}.wav","wb").write(urllib.request.urlopen(r).read())
    s["d"]=LEAD+dur(f"vo/{s['id']}.wav")+TAIL;s["start"]=t;t+=s["d"]
    run(f"ffmpeg -y -i vo/{s['id']}.wav -af 'adelay={int(LEAD*1000)}:all=1,apad=whole_dur={s['d']}' -ar 44100 -ac 1 seg/{s['id']}.wav")
    lst.write(f"file 'seg/{s['id']}.wav'\n");print(s["id"],round(s["d"],2))
lst.close()
run("ffmpeg -y -f concat -safe 0 -i audio.txt -af loudnorm=I=-16:TP=-1.5:LRA=11 vo_mix.wav")
json.dump({"total":t,"scenes":scenes},open("timeline.json","w"),ensure_ascii=False)
run(f"python3 {FAL} transcribe --audio vo_mix.wav --out words.json --yes")  # any STT that writes [{"word","start","end"}] works
print("total",round(t,2),"-> check words.json: numbers, Roogo ('Rogo' is expected), phone pairs")
