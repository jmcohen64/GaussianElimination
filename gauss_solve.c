/*----------------------------------------------------------------
* File:     gauss_solve.c
*----------------------------------------------------------------
*
* Author:   Marek Rychlik (rychlik@arizona.edu)
* Date:     Sun Sep 22 15:40:29 2024
* Copying:  (C) Marek Rychlik, 2020. All rights reserved.
*
*----------------------------------------------------------------*/
#include "gauss_solve.h"
#include <stdlib.h>
#include <stdio.h>
#include "helpers.h"

void gauss_solve_in_place(const int n, double A[n][n], double b[n])
{
  for(int k = 0; k < n; ++k) {
    for(int i = k+1; i < n; ++i) {
      /* Store the multiplier into A[i][k] as it would become 0 and be
	 useless */
      A[i][k] /= A[k][k];
      for( int j = k+1; j < n; ++j) {
	A[i][j] -= A[i][k] * A[k][j];
      }
      b[i] -= A[i][k] * b[k];
    }
  } /* End of Gaussian elimination, start back-substitution. */
  for(int i = n-1; i >= 0; --i) {
    for(int j = i+1; j<n; ++j) {
      b[i] -= A[i][j] * b[j];
    }
    b[i] /= A[i][i];
  } /* End of back-substitution. */
}

void lu_in_place(const int n, double A[n][n])
{
  for(int k = 0; k < n; ++k) {
    for(int i = k; i < n; ++i) {
      for(int j=0; j<k; ++j) {
	/* U[k][i] -= L[k][j] * U[j][i] */
	A[k][i] -=  A[k][j] * A[j][i]; 
      }
    }
    for(int i = k+1; i<n; ++i) {
      for(int j=0; j<k; ++j) {
	/* L[i][k] -= A[i][k] * U[j][k] */
	A[i][k] -= A[i][j]*A[j][k]; 
      }
      /* L[k][k] /= U[k][k] */
      A[i][k] /= A[k][k];	
    }
  }
}

void lu_in_place_reconstruct(int n, double A[n][n])
{
  for(int k = n-1; k >= 0; --k) {
    for(int i = k+1; i<n; ++i) {
      A[i][k] *= A[k][k];
      for(int j=0; j<k; ++j) {
	A[i][k] += A[i][j]*A[j][k];
      }
    }
    for(int i = k; i < n; ++i) {
      for(int j=0; j<k; ++j) {
	A[k][i] +=  A[k][j] * A[j][i];
      }
    }
  }
}

void plu(int n, double A[n][n], int P[n])
{
  
  //printf("%s\n", "start");
  //print_matrix(n, A, 0);
    //for (int i = 0; i<n; i++){
    //  printf("%d\n", P[i]);
    //}
  
  /*
  for(int col=0; col < n-1; col++){
    /* find max
    double max = abs(A[P[col]][col]);
    int rmax = P[col];
    for (int row = col + 1; row < n; row++ ){
      int val = abs(A[P[row]][col]);
      if (max < val) {
        max = val;
        rmax = P[row];
      }
    }
    
    /*swap
    if (rmax != P[col]){
      int temp = P[col];
      P[col] = rmax;
      P[rmax] = temp;
    }
    */
    for(int col=0; col < n-1; col++){
    /* find max*/
    double max = abs(A[col][col]);
    int rmax = col;
    for (int row = col + 1; row < n; row++ ){
      int val = abs(A[row][col]);
      if (max < val) {
        max = val;
        rmax = row;
      }
    }
    //printf("%d\n", rmax);
    /*swap*/
    if (rmax != col){
      for (int c = 0; c< n; c++){
        //printf("%f\n", A[col][c]);
        //printf("%f\n", A[rmax][c]);
        
        double temp = A[col][c];
        A[col][c] = A[rmax][c];
        A[rmax][c] = temp;

        int index = P[col];
        P[col] = P[rmax];
        P[rmax] = index;
      }
      
    }
    
    //printf("%s\n","swap");
    //print_matrix(n, A, 0);
    //for (int i = 0; i<n; i++){
    //  printf("%d\n", P[i]);
    //}
    
    /*update*/

    /*
    for (int row = col + 1; row < n; row++ ){
      /*calculate multiplier
      A[P[row]][col] = A[P[row]][col]/A[P[col]][col];
      /*update matrix
      for (int c = col +1; c < n; c++){
        A[P[row]][c] += -A[P[row]][col]*A[P[col]][c];
      }
    }
    */

    for (int row = col + 1; row < n; row++ ){
      /*calculate multiplier*/
      A[row][col] = A[row][col]/A[col][col];
      /*update matrix*/
      for (int c = col +1; c < n; c++){
        A[row][c] += -A[row][col]*A[col][c];
      }
    }
    
    
    //printf("%s\n","update");
    //print_matrix(n, A, 0);
    //for (int i = 0; i<n; i++){
    //  printf("%d\n", P[i]);
    //}
    
  }
}
