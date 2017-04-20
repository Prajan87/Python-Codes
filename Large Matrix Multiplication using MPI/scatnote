import numpy as np
from mpi4py import MPI as mpi

#Formation of 1000*1000 matrix
A=np.arange(0,10000,0.01).reshape((1000,1000))
B=np.transpose(A)

#Calculation of dot product of A and B without using MPI
D = np.zeros((1000,1000))
D = np.dot(A,B)

#Slicing of matrix B
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
        Bdata = [matB1,matB2,matB3,matB4,matB5,matB6,matB7,matB8,matB9,matB10]
        Adata = A

else:
        Bdata = None
        Adata = None

# Scattering matrix B
scat_data=comm.scatter(Bdata,root=0)

# Broadcasting matrix A
brod_data=comm.bcast(Adata, root=0)

# Calculation of dot product using MPI
Cmat = np.zeros((100, 1000))
for i in range(scat_data.shape[1]):
   Cmat[i,:]= np.dot(brod_data,scat_data[:,i])

# Gathering dot product result from nodes
gath_data = comm.gather(Cmat, root=0)

if rank == 0:
        C=np.vstack((gath_data[0],gath_data[1],gath_data[2],gath_data[3],gath_data[4],gath_data[5],gath_data[6],gath_data[7],gath_data[8],gath_data[9]))

        assert C.all()==D.all()

        print "Dot product of A and B without using MPI is:"
        print D
        print "Dot product of A and B using MPI is:"
        print C

        Ddetm = np.linalg.det(D)
        print "Determinant of dot product of A and B without using MPI is: ",Ddetm
        Cdetm = np.linalg.det(C)
        print "Determinant of dot product of A and B using MPI is: ",Cdetm
