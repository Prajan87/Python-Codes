import numpy as np
from mpi4py import MPI as mpi
A=np.arange(0,10000,0.01).reshape((1000,1000))
#print A
B=np.transpose(A)

D = np.zeros((1000,1000))
D = np.dot(A,B)
print "D is.....:"
print D
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

#print matB1.shape
#print matB10.shape

#print B
comm= mpi.COMM_WORLD
rank= comm.Get_rank()

if rank == 0:
   Cmat0 = np.zeros((100, 1000))
   for i in range(matB1.shape[1]):
       Cmat0[i,:]= np.dot(A,matB1[:,i])
   comm.send([A,matB2], dest=1, tag = 77)
   comm.send([A,matB3], dest=2, tag = 77)
   comm.send([A,matB4], dest=3, tag = 77)
   comm.send([A,matB5], dest=4, tag = 77)
   comm.send([A,matB6], dest=5, tag = 77)
   comm.send([A,matB7], dest=6, tag = 77)
   comm.send([A,matB8], dest=7, tag = 77)
   comm.send([A,matB9], dest=8, tag = 77)
   comm.send([A,matB10], dest=9, tag = 77)
   Cmat1=comm.recv(source=1, tag=88)
   Cmat2=comm.recv(source=2, tag=88)
   Cmat3=comm.recv(source=3, tag=88)
   Cmat4=comm.recv(source=4, tag=88)
   Cmat5=comm.recv(source=5, tag=88)
   Cmat6=comm.recv(source=6, tag=88)
   Cmat7=comm.recv(source=7, tag=88)
   Cmat8=comm.recv(source=8, tag=88)
   Cmat9=comm.recv(source=9, tag=88)
   C=np.vstack((Cmat0,Cmat1,Cmat2,Cmat3,Cmat4,Cmat5,Cmat6,Cmat7,Cmat8,Cmat9))
   print C.shape
   print "C is........:"
   print C
   assert C.all()==D.all()
if rank ==1:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==2:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==3:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==4:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==5:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==6:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==7:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==8:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
if rank ==9:
    Rmat=comm.recv(source=0,tag=77)
    Cmat = np.zeros((100, 1000))
    for i in range(Rmat[1].shape[1]):
       Cmat[i,:]= np.dot(Rmat[0],Rmat[1][:,i])
    comm.send(Cmat,dest=0,tag=88)
