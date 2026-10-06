import json,re
T=json.load(open("timeline.json"));S={s["id"]:s for s in T["scenes"]};TOTAL=T["total"]
words=json.load(open("words.json"))
fix={"rogo":"Roogo","rogobf.com":"roogobf.com","roogo":"Roogo"}
for w in words:
    k=re.sub(r"[^\w.]","",w["word"].lower())
    if k in fix: w["word"]=fix[k]+re.sub(r"[\w.]","",w["word"])
chunks=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)>=3 or re.search(r"[.?!,]$",w["word"]): chunks.append(cur);cur=[]
if cur: chunks.append(cur)
chunks=[c for c in chunks if c[0]["start"]<68.0]

XF=0.3
def box(i):
    s=S[f"s{i}"];st=s["start"]-(XF if i>1 else 0);du=s["d"]+(XF if i>1 else 0);return st,du,s
html=[];js=[]
def fadein(sel,i):
    st,du,s=box(i)
    if i>1: js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:1,duration:{XF},ease:"none"}},{st:.2f});')
# s1,s2 photo montages
from PIL import Image
def shot_html(sid,img):
    w,h=Image.open(f"assets/{img}").size
    if w/h<=0.8: return f'<div class="shot" id="{sid}"><img class="cover" src="assets/{img}"></div>'
    return f'<div class="shot" id="{sid}"><img class="cover bgb" src="assets/{img}"><img class="cover fg" src="assets/{img}"></div>'
def montage(i,imgs):
    st,du,s=box(i);n=len(imgs);per=(du-0.1)/n
    inner="".join(shot_html(f"m{i}_{k}",im) for k,im in enumerate(imgs))
    html.append(f'<div id="sc{i}" class="clip scene" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="{i%2}" style="z-index:{i}">{inner}</div>')
    for k in range(n):
        t0=st+k*per
        js.append(f'tl.fromTo("#m{i}_{k}",{{opacity:0}},{{opacity:1,duration:0.18,ease:"none"}},{t0:.2f});')
        js.append(f'tl.fromTo("#m{i}_{k}",{{scale:{1.0 if k%2==0 else 1.09}}},{{scale:{1.09 if k%2==0 else 1.0},duration:{per+0.3:.2f},ease:"none"}},{t0:.2f});')
        if k<n-1: js.append(f'tl.set("#m{i}_{k}",{{opacity:0}},{t0+per+0.2:.2f});')
    fadein(f"#sc{i}",i)
montage(1,["a109.jpg","a94.jpg","a97.jpg","a95.jpg"])
montage(2,["a206.jpg","a121.jpg","a88.jpg","a96.jpg","a207.jpg"])
# s3 video, s4 two clips (blurred copy behind, contained copy in front)
def vid(i,src,st,du,tr,extra="",rate=None):
    pr=f' data-playback-rate="{rate:.3f}"' if rate else ""
    html.append(f'<video id="{i}bg" class="clip scene cover bgb" src="assets/{src}" muted playsinline data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="{tr+30}" style="z-index:{tr+1}"{pr}></video>')
    html.append(f'<video id="{i}" class="clip scene cover fg" src="assets/{src}" muted playsinline data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="{tr}" style="z-index:{tr+2}"{pr}></video>')
st,du,s=box(3)
vid("sc3","clip_s3.mp4",st,du,1,rate=5.0417/S["s3"]["d"])
fadein("#sc3",3);fadein("#sc3bg",3)
st,du,s=box(4)
cut=3.9
vid("sc4a","clip_s4.mp4",st,cut+0.2,0)
fadein("#sc4a",4);fadein("#sc4abg",4)
vid("sc4b","clip_s4c.mp4",st+cut,du-cut,2)
js.append(f'tl.fromTo("#sc4b,#sc4bbg",{{opacity:0}},{{opacity:1,duration:0.2,ease:"none"}},{st+cut:.2f});')
# s5 steps with portrait photo frame
st,du,s=box(5)
steps=[("1","Vous publiez","Photos, prix, quartier"),("2","Des locataires","Visites organisées"),("3","Mobile money","Orange ou Moov"),("4","Reçus","Suivi des paiements")]
cards="".join(f'<div class="step"><div class="num">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n,t,d in steps)
ph=["a23.jpg","a104.jpg","a105.jpg","r1.jpg","a102.jpg","a101.jpg","a100.jpg"]
frames="".join(f'<img class="ph" id="ph{k}" src="assets/{p}">' for k,p in enumerate(ph))
html.append(f'<div id="sc5" class="clip scene cream" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="1" style="z-index:5"><div class="kick">Comment ça marche</div><h2>Quatre étapes, tout est visible</h2><div class="frame">{frames}</div><div class="grid">{cards}</div></div>')
fadein("#sc5",5)
span=s["d"]-1.0
NP=len(ph)
for k in range(NP):
    a=st+XF+0.3+k*span/NP
    js.append(f'tl.fromTo("#ph{k}",{{opacity:0}},{{opacity:1,duration:0.4,ease:"none"}},{a:.2f});tl.fromTo("#ph{k}",{{scale:1.0}},{{scale:1.06,duration:{span/NP+0.5:.2f},ease:"none"}},{a:.2f});')
    if k<NP-1: js.append(f'tl.set("#ph{k}",{{opacity:0}},{a+span/NP+0.3:.2f});')
js.append(f'tl.from(".step",{{y:40,opacity:0,duration:0.5,stagger:{(span/4):.2f},ease:"power3.out"}},{st+XF+0.3:.2f});')
# s6 price
st,du,s=box(6)
cols=[("0 FCFA","aujourd'hui","Publication gratuite","g"),("50 %","une seule fois","du loyer mensuel, seulement si Roogo trouve le locataire et encaisse le premier loyer","o"),("7 %","par loyer encaissé","sur chaque loyer payé via Roogo","o")]
cc="".join(f'<div class="pc {c}"><div class="big">{b}</div><div class="mid">{m}</div><div class="small">{sm}</div></div>' for b,m,sm,c in cols)
html.append(f'<div id="sc6" class="clip scene dark" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="0" style="z-index:6"><h2 class="w">Combien ça coûte ?</h2><div class="pgrid">{cc}</div></div>')
fadein("#sc6",6)
# card entrance timed to the spoken lines: use fractions of the scene
def wt(name,after=0):
    for w in words:
        if w["start"]>=after and re.sub(r"[^\w]","",w["word"].lower())==name: return w["start"]
ts=[wt("zéro",st+0.5) or st+XF+1, wt("cinquante",st)-0.2, wt("sept",st)-0.2]
for k,t0 in enumerate(ts):
    js.append(f'tl.from(".pc:nth-child({k+1})",{{y:50,opacity:0,duration:0.5,ease:"power3.out"}},{t0:.2f});')
# s7 packs
st,du,s=box(7)
packs=[("Essentiel","15 000 FCFA",""),("Standard","25 000 FCFA","hl"),("Premium","45 000 FCFA","")]
pk="".join(f'<div class="pk {h}"><div class="pn">{n}</div><div class="pp">{p}</div></div>' for n,p,h in packs)
html.append(f'<div id="sc7" class="clip scene cream" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="1" style="z-index:7"><div class="kick">Payer une seule fois ?</div><h2>Les packs de publication</h2><div class="kgrid">{pk}</div></div>')
fadein("#sc7",7)
js.append(f'tl.from(".pk",{{y:40,opacity:0,duration:0.5,stagger:0.4,ease:"power3.out"}},{st+XF+0.6:.2f});')
# s8 end
st,du,s=box(8)
html.append(f'<div id="sc8" class="clip scene white" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="0" style="z-index:8"><img class="elogo o8" src="assets/logo.png"><h2 class="o8">Publiez votre bien. 0 FCFA pour commencer.</h2><div class="avail o8">Roogo Burkina est disponible</div><div class="badges"><div class="sb o8"><img src="assets/apple.svg"><div><small>Télécharger sur</small><b>App Store</b></div></div><div class="sb o8"><img src="assets/play.svg"><div><small>Disponible sur</small><b>Google Play</b></div></div></div><div class="btn o8">roogobf.com</div><div class="wa o8">WhatsApp  +226 <span class="pr" id="pr0">67</span> <span class="pr" id="pr1">00</span> <span class="pr" id="pr2">61</span> <span class="pr" id="pr3">16</span></div></div>')
fadein("#sc8",8)
js.append(f'tl.from("#sc8 .o8",{{y:40,opacity:0,scale:0.94,duration:0.55,stagger:0.3,ease:"back.out(1.4)"}},{st+XF:.2f});')
PAIRS=[(74.2,75.3),(75.5,76.4),(76.62,77.7),(77.88,78.6)]
for k,(a,b) in enumerate(PAIRS):
    js.append(f'tl.to("#pr{k}",{{scale:1.22,color:"#ff8514",duration:0.12,ease:"power2.out"}},{a:.2f});tl.to("#pr{k}",{{scale:1,color:"#5a2d0c",duration:0.15,ease:"power2.in"}},{b:.2f});')
end8=S["s8"]["start"]
# badge
html.append(f'<div id="badge" class="clip" data-start="0" data-duration="{end8:.2f}" data-track-index="6" style="z-index:50"><img src="assets/logo.png"></div>')
# captions
for ci,c in enumerate(chunks):
    st=c[0]["start"];en=c[-1]["end"]+0.15
    if ci+1<len(chunks): en=min(en,chunks[ci+1][0]["start"]-0.02)
    sp="".join(f'<span id="w{ci}_{k}">{w["word"]}</span>' for k,w in enumerate(c))
    html.append(f'<div id="cp{ci}" class="clip cap" data-start="{st:.2f}" data-duration="{en-st:.2f}" data-track-index="5" style="z-index:60">{sp}</div>')
    for k,w in enumerate(c):
        nxt=c[k+1]["start"] if k+1<len(c) else en
        js.append(f'tl.set("#w{ci}_{k}",{{className:"on"}},{w["start"]:.2f});tl.set("#w{ci}_{k}",{{className:""}},{nxt:.2f});')
html.append(f'<audio id="music" src="assets/music_fade.mp3" data-start="0" data-duration="{TOTAL:.2f}" data-track-index="8" data-volume="0.14"></audio>')
html.append(f'<audio id="vo" src="assets/vo.wav" data-start="0" data-duration="{TOTAL:.2f}" data-track-index="7" data-volume="1"></audio>')

import subprocess
def fdur(p): return float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {p}",shell=True))
lastpas=[w["start"] for w in words if w["word"].lower().strip(".,?")=="pas" and 55<w["start"]<63]
sfx=[("birds_morning.mp3",0.0,6.4,.35),
 ("crickets.mp3",6.7,9.2,.5),
 ("phone_buzz.mp3",16.3,None,.2),
 ("wind_hot.mp3",22.7,7.6,.35),("rue.mp3",22.7,7.6,.15),
 ("pop.mp3",30.9,None,.4),("pop.mp3",33.7,None,.4),("pop.mp3",36.5,None,.4),("pop.mp3",39.3,None,.4),
 ("ding.mp3",36.6,None,.45),("paper.wav",39.4,None,.5),
 ("whoosh.wav",42.6,None,.3),("pop.mp3",44.4,None,.45),("pop.mp3",49.7,None,.45),("pop.mp3",53.5,None,.45),

 ("pop.mp3",63.6,None,.3),("pop.mp3",64.0,None,.3),("pop.mp3",64.4,None,.3),
 ("chime.wav",68.3,None,.4)]+[("pop.mp3",68.24+0.3*k+0.05,None,.2) for k in range(1,7)]
tr=10
for n,t0,d,v in sfx:
    full=fdur(f"assets/sfx/{n}");dd=min(full,d) if d else full
    html.append(f'<audio id="sfx{tr}" src="assets/sfx/{n}" data-start="{t0:.2f}" data-duration="{dd:.2f}" data-track-index="{tr}" data-volume="{v}"></audio>');tr+=1
css=open("style_vertical.css").read()
out=f'''<!doctype html>
<html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920">
<title>Roogo VSL propriétaires</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL:.2f}" data-width="1080" data-height="1920">
{chr(10).join(html)}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
{chr(10).join(js)}
window.__timelines["main"]=tl;
</script></body></html>'''
open("index.html","w").write(out)
print("ok",len(chunks))
