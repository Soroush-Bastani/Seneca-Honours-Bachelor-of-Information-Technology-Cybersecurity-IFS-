#!/usr/bin/env python3
import multiprocessing as a
import time as t
import os as o
import json as j
import base64 as b
from datetime import datetime as d, timezone as z

s=30
# hidden byte sizes via base64 of a JSON array
Q0=j.loads(b.b64decode("WzIwOTcxNTIsNDE5NDMwNCw4Mzg4NjA4LDE2Nzc3MjE2LDMzNTU0NDMyXQ==").decode())

def f(n,sec,Q):
    r=bytearray(n)
    try:
        x=d.now(z.utc).isoformat().replace('+00:00','Z')
        Q.put({"pid":o.getpid(),"start_time":x})
    except Exception:
        pass
    u=t.time()
    i=0
    while t.time()-u<sec:
        k=(i*4096)%n
        r[k:k+16]=b"SPR100_FIXED_STRESS"
        i+=1
        t.sleep(0.01)

def g(sec):
    w=max(10,min(60,sec))
    for e in range(sec+1):
        y=int(w*(e/sec)) if sec else w
        h="#"*y+"-"*(w-y)
        R=sec-e
        print(f"\r[{h}] {R:2d}s remaining",end="",flush=True)
        t.sleep(1)
    print()

def main():
    print("SPR100 Task3 - Running...")
    y=t.time()
    Q=a.Queue()
    L=[]
    for n in Q0:
        P=a.Process(target=f,args=(n,s,Q),daemon=False)
        P.start()
        L.append(P)
    g(s)
    for P in L:
        P.join()
    E=t.time()-y
    print(f"Elapsed: {E:.1f} seconds")
    print("Complete")
    C=[]
    try:
        while not Q.empty():
            X=Q.get_nowait()
            if isinstance(X,dict) and "pid" in X and "start_time" in X:
                C.append(X)
    except Exception:
        pass
    try:
        Y=j.dumps(C,separators=(",",":"))
        T=b.b64encode(Y.encode()).decode()
        print("Copy the token below and paste into your answer sheet:")
        print(T)
    except Exception:
        pass


if __name__ == "__main__":
    main()


