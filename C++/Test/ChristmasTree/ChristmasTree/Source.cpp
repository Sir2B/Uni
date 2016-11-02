#include <stdio.h>
#include <iostream>
#include <cstring>
#include <cstdlib>

int main(int argc, char *argv[]) {
	int BranchesCount; // = atoi(argv[1]);
	BranchesCount = 5;

	int LinesPerBranch = 3;
	int TotalLength = BranchesCount * 2 + LinesPerBranch + 2;

	int StarCount = 1;


	for (int Branch = 0; Branch<BranchesCount; Branch++) {

		for (int Line = 0; Line<LinesPerBranch; Line++) {
			int SpaceCount = (TotalLength - StarCount) / 2;

			for (int Spaces = 0; Spaces<SpaceCount; Spaces++) {
				printf(" ");
			}

			for (int Stars = 0; Stars<StarCount; Stars++) {
				printf("*");
			}

			printf("\n");
			StarCount += 2;
		}
		StarCount -= (LinesPerBranch-1)*2;
	}

	for (int Spaces = 0; Spaces<(TotalLength - 3)/2; Spaces++) {
		printf(" ");
	}
	printf("|||\n");
	printf("\n");

	std::cin.get();
	return 0;
}
