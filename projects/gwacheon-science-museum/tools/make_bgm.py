import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
sr=44100; T=30.0; n=int(sr*T); t=np.arange(n)/sr
def note(m): return 440*2**((m-69)/12)
# 코드 진행 (각 3.75초 x 8): Cmaj7 Am9 Fmaj7 G6 반복 — 몽글한 우주 패드
chords=[[48,55,64,71],[45,52,60,67,71],[41,53,57,64],[43,50,59,64]]*2
L=T/len(chords)
pad=np.zeros(n)
for i,ch in enumerate(chords):
    s,e=int(i*L*sr),int(min((i+1)*L+0.8,T)*sr); tt=t[s:e]-i*L
    env=np.minimum(1,tt/1.2)*np.minimum(1,np.maximum(0,(L+0.8-tt)/1.0))
    for m in ch:
        f=note(m)
        for d in (-0.15,0.15):
            pad[s:e]+=env*np.sin(2*np.pi*(f*(1+d/100))*tt+np.sin(2*np.pi*0.3*tt))*0.05
# 반짝이는 벨 아르페지오 (8분음표, 96bpm 근사)
bell=np.zeros(n); step=60/96/2
k=0; tp=0.0
while tp<T-0.5:
    ch=chords[min(int(tp//L),len(chords)-1)]
    m=ch[[1,2,3,2][k%4] % len(ch)]+24
    s=int(tp*sr); e=min(n,s+int(1.2*sr)); tt=t[s:e]-tp
    bell[s:e]+=np.exp(-tt*4)*(np.sin(2*np.pi*note(m)*tt)+0.3*np.sin(2*np.pi*note(m)*2.01*tt))*0.05
    tp+=step; k+=1
bell*=np.clip((t-7)/3,0,1)   # 로비 컷 이후(7초~)부터 벨이 들어옴
mix=pad+bell
sos=butter(4,5000,fs=sr,output='sos'); mix=sosfilt(sos,mix)
# 간단한 스테레오 딜레이로 공간감
d=int(0.23*sr); Lc=mix.copy(); Rc=mix.copy(); Rc[d:]+=0.35*mix[:-d]; Lc[2*d:]+=0.25*mix[:-2*d]
st=np.stack([Lc,Rc],1)
fade=np.clip(t/1.5,0,1)*np.clip((T-t)/2.5,0,1); st*=fade[:,None]
st/=np.max(np.abs(st))*1.12
wavfile.write(sys.argv[1],sr,(st*32767).astype(np.int16))
