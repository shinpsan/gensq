import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

lis_a = [i for i in range(1, 1001)]
lis_b = [i for i in range(1, 1001)]
lis_sq = [i**2 for i in range(1,1001)]
lis_sq_half = [(i**2)/2 for i in range(1,1001) if i**2%2==0]

def plot_4triangles_square(a, b):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.grid()
    p = [(0,b), (a,0), (a+b, a), (b, a+b), (0,b)]
    for i in range(1,5):    
        ax.plot([p[i-1][0], p[i][0]], [p[i-1][1], p[i][1]], color='orange')
    ax.vlines(a, 0, b, linestyles='dashed', color='gray')
    ax.vlines(b, a, a+b, linestyles='dashed', color='gray')
    ax.hlines(b, 0, b, linestyles='dashed', color='gray')
    ax.hlines(a, a, a+b, linestyles='dashed', color='gray')
    ax.set_xticks(np.arange(0, (a+b+1), step=1))
    ax.set_yticks(np.arange(0, (a+b+1), step=1))
    return fig, ax

def plot_square(a):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.grid()
    ax.hlines(0, 0, a, color='orange')
    ax.hlines(a, 0, a, color='orange')
    ax.vlines(0, 0, a, color='orange')
    ax.vlines(a, 0, a, color='orange')
    ax.set_xticks(np.arange(0, (a+1), step=1))
    ax.set_yticks(np.arange(0, (a+1), step=1))
    return fig, ax

def find_ab(S):
    for a in lis_a:
        for b in lis_b:
            if S == (a**2 + b**2):
                a1 = a
                b1 = b
                break
        else:
            a1 = False
            b1 = False
            continue
        break
    return (a1, b1)

def generate_square(S):
    print(f'面積が{S}のとき')
    if S in lis_sq:
        a = np.sqrt(S)
        fig, ax = plot_square(a)
    else:
        ans = find_ab(S)
        if ans[0]:
            a = ans[0]
            b = ans[1]
            fig, ax = plot_4triangles_square(a,b)
        else:
            print(f'解なし\n\n')



st.title('方眼用紙への正方形の作図')

S = st.number_input('作図したい正方形の面積を入力してください(最大100)', min_value=1, max_value=100, step=1)

if S in lis_sq:
    a = np.sqrt(S)
    fig, ax = plot_square(a)
    st.pyplot(fig)
else:
    ans = find_ab(S)
    if ans[0]:
        a = ans[0]
        b = ans[1]
        fig, ax = plot_4triangles_square(a,b)
        st.pyplot(fig)
    else:
        st.write('解なし')











