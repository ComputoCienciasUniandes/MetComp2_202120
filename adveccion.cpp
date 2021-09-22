#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
    double L=1.0;
    double delta_x = 0.01;
    double delta_t = 0.01;
    double t_max = 2.0;
    double t = 0.0;
    double beta = delta_t/delta_x;
    int n_side = L/delta_x + 1;
    double u_past[n_side];
    double u_present[n_side];
    double pi = asin(1.0)*2.0;
    double x;
    ofstream outfile;
    int i;
    
    for(i=0;i<n_side;i++){
        x = i * delta_x;
        u_past[i] = 0.05 * sin(4.0 * pi * x/L);
        u_present[i] = u_past[i];
    }
    
    outfile.open("adveccion.dat");
    
    while(t < t_max){
        for(i=0;i<n_side;i++){
            outfile << u_present[i] << " ";
        }
        outfile << "\n";
        
        for(i=1;i<n_side-1;i++){
            u_present[i] = u_past[i];
            u_present[i] += -(1.0/4.0)*beta*(u_past[i+1]*u_past[i+1]
                                            -u_past[i-1]*u_past[i-1]);
            u_present[i] += (1.0/8.0)*beta*beta*((u_past[i+1] + u_past[i])*(
                            u_past[i+1]*u_past[i+1] - u_past[i]*u_past[i])-
                                                (u_past[i] + u_past[i-1])*(u_past[i]*u_past[i] - u_past[i-1]*u_past[i-1]));
            
        }
        
        for(i=1;i<n_side-1;i++){
            u_past[i] = u_present[i];
        }
        t += delta_t;
    }
    
    outfile.close();
    return 0;
}













