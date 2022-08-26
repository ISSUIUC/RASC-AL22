#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

//#define DEBUG 1

/*
    N1-N3 seem to be for year 1
    N4-N5 are repeated for every year after so (year 2....N)
 */
// N1 code just put into a macro
#define N1 MGO = MGW;  \
                MF = MF1;  \
                MUGA = MUG1;  \
                N = N + 1;  \
                J = J + 1;  \
                JJ = 1; /* year; */  \
                MFA = MF;  \
                TIS = TI;  \
                TP = ((int)TI/1.0)*1.0+TPI;  \
                TZ1 = TP+TZ4;  \
                TZ2 = TZ1+TZ5;  \
                TZ3 = TZ3E;  \
                QBC = QBC1;  \
                MU = MUD;  \
                TAUP = TP+MUGA*.134*RHOW/MUD-TPI;  \
                TPIW = TPIW_SET_N1;  \
                fprintf(fptr,"\t\t\tYEAR\t=\t%d\n",JJ);  \
                fprintf(fptr,"\t\tSTANDBY OR WATER WITHDRAWAL");  \
                fprintf(fptr,"\n");  \
                print_initial_parameter(fptr, MFA, TWB, MUGA, MUD, RHOW, HS, TI); \
                goto L400;

// N2 code put into macro
#define N2 MGO = MGW; \
                MF = MF2; \
                MUGA = MUG2; \
                N = N+1; \
                JJ = 1; \
                MFA = MF; \
                MU = MUD; \
                TIS = TI; \
                TZ1 = TZ2+TZ6; \
                QBC = QBC2; \
                fprintf(fptr,"\t\t\tYEAR\t=\t%d\n",JJ); \
                fprintf(fptr,"\t\tSTANDBY OR WATER WITHDRAWAL"); \
                fprintf(fptr,"\n"); \
                print_initial_parameter(fptr, MFA, TWB, MUGA, MUD, RHOW, HS, TI); \
                goto L400;

// N3 code put into macro
#define N3 MGO = MGW; \
                MUGA = MUGW; \
                MFA = MFS; \
                N = N+1; \
                JJ = 1; \
                MU = MUD; \
                TIS = TI; \
                QBC = QBC3; \
                TZ2 = TZ1+TZS; \
                fprintf(fptr,"\t\t\tYEAR\t=\t%d\n",JJ); \
                fprintf(fptr,"\t\tSTANDBY OR WATER WITHDRAWAL"); \
                fprintf(fptr,"\n"); \
                print_initial_parameter(fptr, MFA, TWB, MUGA, MUD, RHOW, HS, TI); \
                goto L400;

// N4 code put into a macro
#define N4 MGO = MGW; \
                MUGA = MUGS; \
                MFA = MFS; \
                N = N+1; \
                MU = MUD; \
                JJ = JJ+1; \
                TIS = TI; \
                TZ1 = TZ2+TZ6; \
                QBC = QBC4; \
                fprintf(fptr,"\t\t\tYEAR=%d\n",JJ); \
                fprintf(fptr,"S\t\tUMMER WATER WITHDRAWAL"); \
                fprintf(fptr,"\n"); \
                print_initial_parameter(fptr, MFA, TWB, MUGA, MUD, RHOW, HS, TI); \
                goto L400;

// N5 code put into a macro
#define N5 MGO = MGW; \
                MUGA = MUGW; \
                MFA = MFS; \
                N = N+1; \
                MU = MUD; \
                TZ2 = TZ1+TZS; \
                TIS = TI; \
                QBC = QBC5; \
                fprintf(fptr,"\t\t\tYEAR=%d\n",JJ); \
                fprintf(fptr,"W\t\tINTER WATER WITHDRAWAL"); \
                fprintf(fptr,"\n"); \
                print_initial_parameter(fptr, MFA, TWB, MUGA, MUD, RHOW, HS, TI); \
                goto L400;

// Prints the intial paramters
void print_initial_parameter(FILE *fptr, double MFA, double TWB, double MUGA, double MUD, double RHOW, double HS, double TI) {
    fprintf(fptr,"BOILER WATER FLOW RATE lbm/hr \t=\t%f\n",MFA);
    fprintf(fptr,"BOILER WATER TEMPERATURE DEG F \t=\t%f\n",TWB);
    fprintf(fptr,"WATER WITHDRAWAL GAL/DAY \t\t=\t%f\n",MUGA);
    fprintf(fptr,"WITHDRAWAL FLOW RATE GAL/MIN \t=\t%f\n",MUD/(8.04*RHOW));
    fprintf(fptr,"CONVECTIVE COEFF AFTER R=30 FT BTU/HR-FT2-F \t=\t%f\n",HS);
    fprintf(fptr,"START WITHDRAWAL AT HOUR \t\t=\t%f\n",TI);
    fprintf(fptr,"\n");
}
