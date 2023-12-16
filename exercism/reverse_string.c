#include <stdlib.h>
#include <string.h>

char *reverse(const char *value) {
    int len = strlen(value);
    char *result = malloc(len + 1);
    for (int i = 0; i < len; i++) {
        result[i] = value[len - i - 1];
    }
    result[len] = '\0';
    return result;
}