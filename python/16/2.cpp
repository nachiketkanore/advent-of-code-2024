#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<string> mat;

int main() {
	freopen("ex1", "r", stdin);
	string line;
	while (getline(cin, line)) {
		mat.push_back(line);
	}
	N = mat.size();
	M = mat[0].size();

	return 0;
}
