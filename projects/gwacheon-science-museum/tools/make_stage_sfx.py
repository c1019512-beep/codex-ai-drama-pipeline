"""무대 버전 효과음 트랙 (상자 열림·변신 반짝임·화성 전환·엔딩 차임)."""
import sys, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
sr=48000; T=float(sys.argv[2]); n=int(sr*T); out=np.zeros(n); rng=np.random.default_rng(7)
def add(at, sig):
    s=int(at*sr); e=min(n, s+len(sig)); out[s:e]+=sig[:e-s]
def tone(f, dur, decay, vol):
    t=np.arange(int(dur*sr))/sr; return vol*np.exp(-t*decay)*(np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*f*2.01*t))
def noise(dur, lo, hi, vol, env):
    x=rng.standard_normal(int(dur*sr)); sos=butter(2,[lo,hi],btype='band',fs=sr,output='sos'); return vol*sosfilt(sos,x)*env(np.linspace(0,1,len(x)))
# 상자 리본 풀림 + 뚜껑 팝 (2.0s)
add(1.9, noise(0.35,1500,6000,0.25,lambda u:np.sin(np.pi*u)))
add(2.3, tone(420,0.25,18,0.35)+np.pad(tone(840,0.15,25,0.15),(0,int(0.1*sr))))
# 변신 반짝임 (9.8~12.4s)
for k in range(46):
    add(9.8+k*0.055+rng.uniform(0,0.03), tone(rng.uniform(1800,4200),0.35,9,0.07))
add(9.8, noise(2.4,2000,9000,0.12,lambda u:u**1.5*(1-u**8)))
add(12.35, tone(1568,1.2,3,0.22)); add(12.42, tone(2093,1.2,3,0.16))
# 화성 전환 휘익 (15.2s) + 모래 사르륵
sw=noise(0.8,300,4000,0.35,lambda u:np.sin(np.pi*u)); add(15.2, sw)
add(15.7, noise(2.2,200,1500,0.10,lambda u:np.sin(np.pi*u)))
# 엔딩 차임 (23.6s)
for i,f in enumerate([1047,1319,1568,2093]): add(23.6+i*0.12, tone(f,1.6,2.5,0.18))
out=np.clip(out,-1,1); wavfile.write(sys.argv[1], sr, (np.stack([out,out],1)*32767).astype(np.int16))
