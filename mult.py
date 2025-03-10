import time

def OnMult(m_ar: int, m_br: int) -> int:
    pha = [1.0 for _ in range(m_ar * m_ar)]
    phb = [float(i + 1) for i in range(m_br * m_br)]
    phc = [0 for _ in range(m_br * m_br)]
    for i in range(m_ar):
        for j in range(m_br):
            temp = 0
            for k in range(m_ar):
                temp += pha[i * m_ar + k] * phb[k * m_ar + j]
            phc[i * m_ar + j] = temp
    return phc

def OnMultLine(m_ar: int, m_br: int) -> int:
    pha = [1.0 for _ in range(m_ar * m_ar)]
    phb = [float(i + 1) for i in range(m_br * m_br)]
    phc = [0 for _ in range(m_br * m_br)]
    for i in range(m_ar):
        for k in range(m_ar):
            temp = 0
            for j in range(m_br):
                #not sure about this one
                phc[i * m_ar + j] += pha[i * m_ar + k] * phb[k * m_ar + j]
    return phc


for matrix_size in range(600, 3000, 400):
    start_time = time.time()
    OnMultLine(matrix_size, matrix_size)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Time taken: {elapsed_time:.4f} seconds")