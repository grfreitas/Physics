
// AGA0511 - Métodos Computacionais em Astronomia (2020)
// Gabriel Ribeiro Freitas
// Nº USP: 10830482

#define N 7

#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using std::vector;
using std::ostream;


// Template to print vectors.
template<typename T>
ostream &operator<<(ostream &out, const vector <T> &v) {
    out << "{";
    size_t last = v.size() - 1;
    for (size_t i = 0; i < v.size(); ++i) {
        out << v[i];
        if (i != last)
            out << ", ";
    }
    out << "}";
    return out;
}

void travelling_salesman_solver(int graph[][N], int s) {

    // Initializes vertex positions without starting point to optimize a little.
    vector<int> vertex;
    for (int i = 0; i < N; i++)
        if (i != s) {
            vertex.push_back(i);
        }

    vector<int> min_path = vertex;

    // Initializing cost variable, which will be updated in the iterations.
    int min_path_len = INT_MAX;
    do {
        int current_path_length = 0;
        int k = s;

        // Iterate over all possible paths starting at vertex k, adding all the lengths over the path len variable.
        for (int i = 0; i < vertex.size(); i++) {
            current_path_length += graph[k][vertex[i]];
            k = vertex[i];
        }
        current_path_length += graph[k][s];

        if (current_path_length <= min_path_len) {
            min_path_len = current_path_length;
            min_path = vertex;
        }

    } while (next_permutation(vertex.begin(), vertex.end()));

    min_path.insert(min_path.begin(), s);

    std::cout << "Best Travelling Order: " << min_path << std::endl;
    std::cout << "Travelling Length: " << min_path_len << " units." << std::endl;

}

void print_execution_time(clock_t end, clock_t start) {
    // Print code total execution time.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    std::cout << "Time taken by program is : " << std::fixed << time_taken << std::setprecision(5);
    std::cout << " sec " << std::endl;
}

int main() {

    clock_t start, end;

    int starting_vertex = 0;
    int graph[][N] = {
            {0,  29, 82, 46, 68, 52, 72},
            {29, 0,  55, 46, 42, 43, 43},
            {82, 55, 0,  68, 46, 55, 23},
            {46, 46, 68, 0,  82, 15, 72},
            {68, 42, 46, 82, 0,  74, 23},
            {52, 43, 55, 15, 74,  0, 61},
            {72, 43, 23, 72, 23, 61,  0},
    };

    start = clock();
    travelling_salesman_solver(graph, starting_vertex);
    end = clock();

    print_execution_time(end, start);

    return 0;
}