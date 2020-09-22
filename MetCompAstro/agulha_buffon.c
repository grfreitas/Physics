//
// Created by gabs on 03/09/2020.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {

    int N;
    printf("Insira o nº de lançamentos a serem simulados: ");
    scanf("%d", &N);

    int intersected = 0;

    for (int i=0; i<N; i++){
        double theta = 2 * M_PI * rand() / RAND_MAX;
        double x = (double) rand() / RAND_MAX - 0.5;

        double x1 = x - 0.5 * cos(theta);
        double x2 = x + 0.5 * cos(theta);

        if (x1 * x2 <= 0) {
            intersected++;
        };
    }

    double pi =  2.0 * N / intersected;

    printf("Pi estimado para %d lançamentos: %f\n", N, pi);

    erro = (double) pi - M_PI
    printf("Erro: %f \n", erro);
    return 0;
}