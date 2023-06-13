#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check if proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open the card
    FILE *file = fopen(argv[1], "r");

    // Check if file can be open
    if (file == NULL)
    {
        printf("Could not open the file.\n");
        fclose(file);
        return 1;
    }

    // Buffer to store filename
    char filename[8];

    // File pointer for image;
    FILE *img = NULL;

    // Buffer to store current block
    BYTE *buffer = malloc(SIZE);

    // Counter for filename
    int num = 0;

    // Loop through the card
    while (fread(buffer, sizeof(BYTE) * SIZE, 1, file) == 1)
    {
        // If detected a new JPEG HEADER
        if (buffer[0] == 0xff
            && buffer[1] == 0xd8
            && buffer[2] == 0xff
            && (buffer[3] & 0xf0) == 0xe0)
        {
            // If not new JPEG means we already detected one
            if (img != NULL)
            {
                fclose(img);
            }

            // Writes the new JPEG
            sprintf(filename, "%03i.jpg", num++);
            img = fopen(filename, "w");
        }
        // If the not new JPEG mean we write its next block
        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE) * SIZE, 1, img);
        }
    }

    // Free the used memory in the heap
    free(buffer);
    // Incase there's some kind of error we need to close the FILE *img.
    if (img != NULL)
    {
        fclose(img);
    }
    // Close the card
    fclose(file);

    // Successful operation
    return 0;
}