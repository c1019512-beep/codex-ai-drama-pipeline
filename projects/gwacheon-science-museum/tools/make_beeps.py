import sys, numpy as np
from scipy.io import wavfile
sr=44100; T=30.0; n=int(sr*T); out=np.zeros(n)
def beep(at,f,dur=0.09,vol=0.35):
    s=int(at*sr); tt=np.arange(int(dur*sr))/sr
    env=np.minimum(1,tt/0.005)*np.minimum(1,(dur-tt)/0.02)
    out[s:s+len(tt)]+=vol*env*np.sign(np.sin(2*np.pi*f*tt))*0.5+vol*env*np.sin(2*np.pi*f*tt)*0.5
# (삐빅) 오류음 4.8초 / 착용 완료 확인음 11.0초 / 화면 박스 24.6초
beep(4.80,1760); beep(4.95,1320)
beep(11.0,1320,0.07); beep(11.1,1760,0.12)
for i,f in enumerate([1047,1319,1568]): beep(24.6+i*0.08,f,0.08,0.25)
wavfile.write(sys.argv[1],sr,(np.clip(out,-1,1)*32767).astype(np.int16))
