#include "TXLib.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const int WIDTH = 800;
const int HEIGHT = 600;
const int MAX_N = 256;
const float MAX_R = 10;
const float MOVE_SPEED = 0.008f;
const float ZOOM_COEF = 0.95f;
void ChangeScale();

float minX = -2,    maxX = 2;
float minY = -1.5f, maxY = 1.5f;

int main(int argc, char* argv[]) {
    txCreateWindow(WIDTH, HEIGHT);

    RGBQUAD* videoBuffer = txVideoMemory();
    COLORREF* scr = (COLORREF*)videoBuffer;

    float dx = 0;
    float dy = 0;

    unsigned long long sum_ticks = 0;

    int esc_cnt = 1000;
    FILE* res_file;
    if (argc > 1)
        res_file = fopen(argv[1], "w");
    else 
        res_file = fopen("results_base.txt", "w");

    for (int esc_ind = 0; esc_ind < esc_cnt; ++esc_ind) {

        ChangeScale();

        dx = (maxX - minX) / WIDTH;
        dy = (maxY - minY) / HEIGHT;
        unsigned long long start_time = __rdtsc();
        for (int i = 0; i < HEIGHT; ++i) {
            float x0 = minX;
            float y0 = minY + (float)i * dy;
            int ind = i * WIDTH;

            for (int j = 0; j < WIDTH; ++j, x0 += dx, ++ind) {
                float x = x0;
                float y = y0;

                int N = 0;

                for (; N < MAX_N; ++N) {
                    float x2 = x * x;
                    float y2 = y * y;
                    float xy = x * y;

                    float r2 = x2 + y2;
                    if (r2 >= MAX_R) break;

                    x = x2 - y2 + x0;
                    y = xy + xy + y0;
                }

                int r = N;
                int g = N;
                int b = N;
                
                scr[ind] = RGB(r, g, b);
            }
        }
        unsigned long long end_time = __rdtsc();
        unsigned long long dt = end_time - start_time;
        sum_ticks += dt;

        fprintf(res_file, "%llu\n", dt);

        double FPS = txGetFPS();
        static int last_tick = 0;
        if (GetTickCount() - last_tick > 100) {
            printf("\r\033[KFPS: %7.3lf", FPS);
            last_tick = GetTickCount();
        }
    }

    fclose(res_file);
    
    printf("\nSum ticks: %12llu\n", sum_ticks);
    printf("Avg ticks: %12llu\n", sum_ticks / esc_cnt);
}

void ChangeScale() {
    float chX = (maxX - minX) * MOVE_SPEED;
    float chY = (maxY - minY) * MOVE_SPEED;
    if (txGetAsyncKeyState(VK_LEFT))    {
        minX -= chX;
        maxX -= chX;
    }
    if (txGetAsyncKeyState(VK_RIGHT))   {
        minX += chX;
        maxX += chX;
    }
    if (txGetAsyncKeyState(VK_UP))      {
        minY += chY;
        maxY += chY;
    }
    if (txGetAsyncKeyState(VK_DOWN))    {
        minY -= chY;
        maxY -= chY;
    }
    
    float avgX = (minX + maxX) / 2;
    float avgY = (minY + maxY) / 2;
    if (txGetAsyncKeyState(VK_OEM_PLUS))     {
        minX = avgX - (avgX - minX) * ZOOM_COEF;
        maxX = avgX + (maxX - avgX) * ZOOM_COEF;
        minY = avgY - (avgY - minY) * ZOOM_COEF;
        maxY = avgY + (maxY - avgY) * ZOOM_COEF; 
    }
    if (txGetAsyncKeyState(VK_OEM_MINUS)){
        minX = avgX - (avgX - minX) / ZOOM_COEF;
        maxX = avgX + (maxX - avgX) / ZOOM_COEF;
        minY = avgY - (avgY - minY) / ZOOM_COEF;
        maxY = avgY + (maxY - avgY) / ZOOM_COEF;
    }
}

/*
Without O3: -----------------
FPS:   5.618
Sum ticks:  60216060527
Avg ticks:    602160605

With O3: --------------------
FPS:  15.333
Sum ticks:  21577457054
Avg ticks:    215774570
*/
