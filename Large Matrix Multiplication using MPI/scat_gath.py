import numpy as np
from mpi4py import MPI as mpi
A=np.arange(0,10000,0.01).reshape((1000,1000))
#print A
B=np.transpose(A)

D = np.zeros((1000,1000))
D = np.dot(A,B)

matB1=B[:, :100]
matB2=B[:,100:200]
matB3=B[:,200:300]
matB4=B[:,300:400]
matB5=B[:,400:500]
matB6=B[:,500:600]
matB7=B[:,600:700]
matB8=B[:,700:800]
matB9=B[:,800:900]
matB10=B[:,900:]

comm= mpi.COMM_WORLD
rank= comm.Get_rank()

if rank == 0:
        data = [[A,matB1],[A,matB2],[A,matB3],[A,matB4],[A,matB5],[A,matB6],[A,matB7],[A,matB8],[A,matB9],[A,matB10]]

else:
        data = None

scat_data=comm.scatter(data,root=0)

if rank ==0:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])

if rank ==1:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==2:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==3:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==4:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==5:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==6:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==7:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==8:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])
if rank ==9:
    Cmat = np.zeros((100, 1000))
    for i in range(scat_data[1].shape[1]):
       Cmat[i,:]= np.dot(scat_data[0],scat_data[1][:,i])

gath_data = comm.gather(Cmat, root=0)

if rank == 0:
        C=np.vstack((gath_data[0],gath_data[1],gath_data[2],gath_data[3],gath_data[4],gath_data[5],gath_data[6],gath_data[7],gath_data[8],gath_data[9]))

        assert C.all()==D.all()
                                                   
