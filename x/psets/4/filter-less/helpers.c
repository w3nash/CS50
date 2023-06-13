#include "helpers.h"
#include <math.h>

BYTE cap(int a);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop into pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get the average of pixel's RGB
            BYTE average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            // Assign average to pixel's RGB
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop into pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Store the original values of pixel's RGB
            BYTE r = image[i][j].rgbtRed;
            BYTE g = image[i][j].rgbtGreen;
            BYTE b = image[i][j].rgbtBlue;

            // Calculate the Sepia values and assign to pixel's RGB
            image[i][j].rgbtRed = cap(round(.393 * r + .769 * g + .189 * b));
            image[i][j].rgbtGreen = cap(round(.349 * r + .686 * g + .168 * b));
            image[i][j].rgbtBlue = cap(round(.272 * r + .534 * g + .131 * b));
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop into pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Make a copy of the current pixel
            RGBTRIPLE temp = image[i][j];
            // Swap the current pixel to opposite pixel in half
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Loop into pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Sum variables
            int sum_blue = 0;
            int sum_green = 0;
            int sum_red = 0;
            // Ctr variables
            float ctr = 0.0;

            for (int row = -1; row < 2; row++)
            {
                for (int col = -1; col < 2; col++)
                {
                    int total_h = i + row;
                    int total_w = j + col;
                    // If outside the height skip
                    if (total_h < 0 || total_h > height - 1)
                    {
                        continue;
                    }
                    // If outside the width skip
                    if (total_w < 0 || total_w > width - 1)
                    {
                        continue;
                    }
                    // Add the RGB of the pixel
                    sum_blue += copy[i + row][j + col].rgbtBlue;
                    sum_green += copy[i + row][j + col].rgbtGreen;
                    sum_red += copy[i + row][j + col].rgbtRed;
                    // Increment the counter
                    ctr++;
                }
            }
            // Get the average and update the pixel's RGB
            image[i][j].rgbtBlue = round(sum_blue / ctr);
            image[i][j].rgbtGreen = round(sum_green / ctr);
            image[i][j].rgbtRed = round(sum_red / ctr);
        }
    }
}

// Cap to 255
BYTE cap(int a)
{
    if (a > 255)
    {
        return 255;
    }
    return a;
}