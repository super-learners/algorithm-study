#include <stdio.h>

static int next_int() {
    int i;
    scanf("%d ", &i);
    return i;
}

static int adrians_answer(int idx) {
    if (idx % 3 == 0) return 'A';
    if (idx % 3 == 1) return 'B';
    return 'C';
}

static int brunos_answer(int idx) {
    if (idx % 4 == 0) return 'B';
    if (idx % 4 == 1) return 'A';
    if (idx % 4 == 2) return 'B';
    return 'C';
}

static int gorans_answer(int idx) {
    if (idx % 6 == 0) return 'C';
    if (idx % 6 == 1) return 'C';
    if (idx % 6 == 2) return 'A';
    if (idx % 6 == 3) return 'A';
    if (idx % 6 == 4) return 'B';
    return 'B';
}

int main() {
    const length = next_int();
    int adrian = 0, bruno = 0, goran = 0;
    for (int i = 0; i < length; i++) {
        const char c = getchar();
        if (c == adrians_answer(i)) {
            adrian++;
        }
        if (c == brunos_answer(i)) {
            bruno++;
        }
        if (c == gorans_answer(i)) {
            goran++;
        }
    }

    int highest_score = adrian;
    if (bruno > highest_score) {
        highest_score = bruno;
    }
    if (goran > highest_score) {
        highest_score = goran;
    }

    printf("%d\n", highest_score);
    if (highest_score == adrian) {
        printf("Adrian\n");
    }
    if (highest_score == bruno) {
        printf("Bruno\n");
    }
    if (highest_score == goran) {
        printf("Goran\n");
    }
    return 0;
}
