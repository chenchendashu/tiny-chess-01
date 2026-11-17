import os,json,time
from urllib.request import*
N=40000
I=range(21,99)
J=3e4
B=frozenset
Z=RuntimeError
D={'P':(-10,-20,-9,-11),'N':(-21,-19,-12,-8,8,12,19,21),'B':(-11,-9,9,11),'R':(-10,-1,1,10)}
D['K']=D['Q']=D['B']+D['R']
V=dict(zip('PNBRQK',(100,320,335,500,950,0)))
t=r'qqqqU___JJSTIIII5?IJ?RSS?SS\,5???RIIHRSS?SSS????SS\\AJJS@IJJHIRR?HIR?ISS?ISS>??H66.&67/&6880PYH?'
T=dict.fromkeys('. ',[0]*120)
for k,p in enumerate(V):
 T[p]=[0]*120
 for i in I:
  if 0<i%10<9:
   v=ord(t[k*16+(i//20-1)*4+min(i%10-1,8-i%10)])-33;T[p][i]=((V[p]+(v//9-4)*20)<<16)+V[p]+(v%9-4)*20
 T[p.lower()]=[-v for v in T[p][::-1]]
def A(b,k):
 for d in D['K']:
  j=k+d
  if b[j]=='k'or d in(-9,-11)and b[j]=='p':return 1
  while b[j]=='.':j+=d
  if b[j]in('bq'if d in D['B']else'rq'):return 1
 return any(b[k+d]=='n'for d in D['N'])
def G(P,q=0):
 b,r,e,*_=P
 for i in I:
  p=b[i]
  if p not in D:continue
  for d in D[p]:
   j=i+d
   while b[j]!=' ':
    t=b[j]
    if t in D:break
    if p=='P'and((t!='.'or d==-20 and(i<81 or b[i-10]!='.'))if not d%10 else t=='.'and j!=e):break
    if not q or t!='.'or p=='P'and(j==e or j<30):
     for z in'QNRB'if p=='P'and j<30 else' ':yield i,j,z.strip()
    if p in'PNK'or t!='.':break
    j+=d
  if p=='K'and not q:
   for x in(91,98):
    d=1 if x>i else-1
    if x in r and b[x]=='R'and all(b[k]=='.'for k in range(i+d,x,d))and not any(A(b,i+k*d)for k in(0,1,2)):yield i,i+2*d,''
def M(P,m):
 b,r,e,h,c=P;i,j,z=m;p=b[i];a=list(b);a[i]='.';a[j]=z or p
 if p=='P'and j==e:a[j+10]='.'
 if p=='K':
  r-={91,98}
  if abs(i-j)==2:a[91 if j<i else 98]='.';a[(i+j)//2]='R'
 if A(a,a.index('K')):return
 e=(p=='P'and i-j==20)and i-10;return L(''.join(a),r-{i,j},e,(p!='P'and b[j]=='.')*(h+1),c)
def L(b,r,e,h,c):return b[::-1].swapcase(),B(119-x for x in r),e and 119-e,h,c^1
def K(P):b,r,e,h,c=P;return b,r,e and any(b[i]=='P'and M(P,(i,e,''))for i in(e+9,e+11))and e,c
def E(P):b=P[0];s=sum(T[p][i]for i,p in enumerate(b));a=(s+32768)>>16;z=s-(a<<16);f=min(24,sum(b.count(p)*w for p,w in zip('NBRQnbrq',(1,1,2,4)*2)));return z+(a-z)*f//24+30*((b.count('B')>1)-(b.count('b')>1))
def S(P,d,a,z,l=0):
 global n;n+=1
 if n>N or not n%1024 and time.monotonic()-w>8.5:raise Z
 r=R.count(K(P));t=P[0]
 if r>2 or P[3]>=100:return 0
 c=A(t,t.index('K'));q=d<1;o=a;v=-J+l;b=0
 x=X.get(P,(-1,0,0,0));h=x[3]
 if not q and r<2 and x[0]>=d and(not x[1]or(x[2]>=z if x[1]>0 else x[2]<=a)):return x[2]
 if q and not c:
  v=E(P)
  if v>=z:return v
  a=max(a,v)
 def O(m):i,j,p=m;return(m==h)*1e6+(p>''or t[j]!='.'or j==P[2])*1e5+V.get(t[j].upper(),100*(j==P[2]))*100-V[t[i]]+(m in H.get(l,()))*8e4+H.get(m,0)
 for m in sorted(G(P,q*(1-c)),key=O,reverse=True):
  C=M(P,m)
  if not C:continue
  R.append(K(C))
  x=-S(C,d-1,-z,-a,l+1);R.pop()
  if x>v:v,b=x,m
  a=max(a,x)
  if a>=z:
   if t[m[1]]=='.':H[l]=(m,)+H.get(l,())[:1];H[m]=H.get(m,0)+d*d
   break
 if not(b or q):v=-J+l if c else 0
 if not q:X[P]=(d,(v>=z)-(v<=o),v,b)
 return v
def F(f):
 b,c,r,e,h,*_=f.split();b=' '*21+b.replace('/','  ')+' '*21
 for i in'12345678':b=b.replace(i,'.'*int(i))
 c=c=='b';r=B(i for p,i in zip('KQkq',(98,91,28,21))if p in r);e=U(e)if e!='-'else 0
 P=b,r,e,int(h),0;return L(*P)if c else P
def U(s):return ord(s[0])+4-10*int(s[1])
def u(m,c):return''.join(chr(96+i%10)+str(10-i//10)for i in(m[:2]if not c else(119-m[0],119-m[1])))+m[2].lower()
def C(g):
 global R,X,H,n,w;P=F(g['start_fen']);R=[K(P)]
 for s in g['moves']:
  m=U(s[:2]),U(s[2:4]),s[4:].upper()
  if P[4]:m=119-m[0],119-m[1],m[2]
  P=M(P,m);R.append(K(P))
 P=F(g['fen']);X={};H={};n=0;w=time.monotonic();v=0
 for d in range(1,100):
  try:S(P,d,-J-1,J+1)
  except Z:break
  v=X[P][3]or v
 return u(v,P[4])
def j(p,b):return json.load(urlopen(Request(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(b).encode(),{'Content-Type':'application/json'})))
while(g:=j('/game',{}))['status']!='done':
 while g['legal_moves']:
  ls=g['legal_moves'];m=ls[0]
  try:
   b=C(g)
   if b in ls:m=b
  except Exception:pass
  g=j('/move',{'game':g['game'],'move':m})
