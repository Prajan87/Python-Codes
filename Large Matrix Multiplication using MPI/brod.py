import numpy as np
from mpi4py import MPI as mpi

comm= mpi.COMM_WORLD
rank= comm.Get_rank()

A=np.arange(0,10000,0.01).reshape((1000,1000))
#print A
B=np.transpose(A)

D = np.zeros((1000,1000))
D = np.dot(A,B)



mat=comm.bcast([A,B],root = 0)

if rank == 0:
        Cmat0 = np.zeros((100, 1000))
        for i in range(100):
                Cmat0[i,:]= np.dot(mat[0],mat[1][:,i])
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
if rank == 1:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+100])
        comm.send(Cmat,dest=0,tag=88)
if rank == 2:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+200])
        comm.send(Cmat,dest=0,tag=88)
if rank == 3:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+300])
        comm.send(Cmat,dest=0,tag=88)
if rank == 4:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+400])
        comm.send(Cmat,dest=0,tag=88)
if rank == 5:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+500])
        comm.send(Cmat,dest=0,tag=88)
if rank == 6:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+600])
        comm.send(Cmat,dest=0,tag=88)
if rank == 7:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+700])
        comm.send(Cmat,dest=0,tag=88)
if rank == 8:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+800])
        comm.send(Cmat,dest=0,tag=88)
if rank == 9:
        Cmat = np.zeros((100, 1000))
        for i in range(100):
                Cmat[i,:]= np.dot(mat[0],mat[1][:,i+900])
        comm.send(Cmat,dest=0,tag=88)
                                       
