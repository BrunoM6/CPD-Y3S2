import time

def OnMult(m_ar: int, m_br: int):
    pha = [1.0 for _ in range(m_ar * m_ar)]
    phb = [float(i + 1) for _ in range(m_br * m_br)]
    for i in range(m_ar):
        for j in range(m_ar):
            temp = 0
            for k in range(m_ar):
                phc[i][j] = 

start_time = time.time()       
OnMult()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.4f} seconds")