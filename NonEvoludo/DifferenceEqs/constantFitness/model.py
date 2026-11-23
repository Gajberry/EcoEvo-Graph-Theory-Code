import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigs, spsolve

def get_transition_matrix_well_mixed(r, d,N):
    
    Q = lil_matrix((N+1, N+1))
    
    for i in range(N+1):
        
        if i == 0:
            Q[i, i] = 1.0
            continue
        
        p_up = (r / (r+d)) *(N-i)/N
        
                                         
        p_down = d/(r+d)
        
                     
        if p_up!=0:
            Q[i, i+1] = p_up
        Q[i, i-1] = p_down
        Q[i, i]   = 1 - p_up - p_down
        
    return Q[1:,1:]


def get_stationary_distribution(r,d,N):
    Q=get_transition_matrix_well_mixed(r,d,N)
    _, vecs = eigs(Q.tocsr().T, k=1, which='LM') 
    stationary_vec = np.real(vecs[:, 0])
    stationary_vec /= stationary_vec.sum()
    return stationary_vec


def get_take_over_probabilities(r, d, N):
    n_nodes = (N + 1) * (N + 1)
    
    def node(i, j):
        return j * (N + 1) + i

    A = lil_matrix((n_nodes, n_nodes))
    b = np.zeros(n_nodes)

    for i in range(N + 1):
        for j in range(N + 1):
            node_val = node(i, j)
            A.rows[node_val] = []
            A.data[node_val] = []

            A[node_val, node_val] = 1

            if i == 0 or i + j > N:
                b_val = 0
            elif j == 0:
                b_val = 1
            else:
                Tijplus = i * r 
                Tijminus = i * d
                Sijplus = j
                Sijminus = j * d

                b_val = 0
                total = Tijplus + Tijminus + Sijplus + Sijminus

                successful_birth_prob = max([(N-i-j)/N,0])
                A[node_val,node(i+1,j)] = -Tijplus/total*successful_birth_prob
                A[node_val,node(i,j+1)] = -Sijplus/total*successful_birth_prob
                A[node_val,node_val] -= Tijplus/total*(1-successful_birth_prob)+Sijplus/total*(1-successful_birth_prob)
                A[node_val,node(i-1,j)] = -Tijminus/total
                A[node_val,node(i,j-1)] = -Sijminus/total

                A[node_val,:]=A[node_val,:]/A[node_val,node_val]

            b[node_val] = b_val
    u = spsolve(A.tocsr(), b)
    U = u.reshape((N + 1, N + 1))
    return U


def get_invasion_probability(r, d, N):
    U = get_take_over_probabilities(r, d, N)
    return(U[:,1])


def get_mean(r,d,M):
    p_A = get_stationary_distribution(r,d,M)
    mean = 0
    for ind,val in enumerate(p_A):
        mean+=(ind+1)*val
    return mean


def get_correct_M(r,d,K):
    previous_best= math.inf
    initial = int(np.floor(K/(1-d/r)))
    initial_mean = get_mean(r,d,initial)
    if initial_mean>K:
        deltaM = -1

    else:
        deltaM = 1
    current = initial

    while True:
        mean = get_mean(r,d,current)
        if (deltaM == 1 and mean >= K) or (deltaM == -1 and mean <= K):
            break
        else:
            current += deltaM
            previous_best = mean
    if np.abs(mean-K)<np.abs(previous_best-K):
        return current
    else:
        return current-deltaM


def get_qsd(r, d, N):
    n = N                             
    Q = lil_matrix((n, n))
    for idx in range(n):
        i = idx + 1
        if i == N:
            di = d * i
            Q[idx, idx-1] = di
            Q[idx, idx] = -di
        else:
            b = r * i * (N - i) / N
            di = d * i
            Q[idx, idx+1] = b
            Q[idx, idx-1] = di
            Q[idx, idx] = -(b + di)

    _, vecs = eigs(Q.T, k=1, which='LR')
    qsd = np.real(vecs[:, 0])
    qsd = np.abs(qsd)
    qsd /= qsd.sum()
    return qsd                                               
