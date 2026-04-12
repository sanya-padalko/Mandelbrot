#include "TXLib.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SZ 8

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
        res_file = fopen("results_opt.txt", "w");

    for (int esc_ind = 0; esc_ind < esc_cnt; ++esc_ind) {

        ChangeScale();

        dx = (maxX - minX) / WIDTH;
        dy = (maxY - minY) / HEIGHT;
        unsigned long long start_time = __rdtsc();
        for (int i = 0; i < HEIGHT; ++i) {
            float x0[SZ];
            float y0[SZ];

            for (int k = 0; k < SZ; ++k) x0[k] = minX + (float)k * dx;
            for (int k = 0; k < SZ; ++k) y0[k] = minY + (float)i * dy;

            int ind = i * WIDTH;

            for (int j = 0; j < WIDTH; j += SZ) {
                float x[SZ];
                float y[SZ];

                for (int k = 0; k < SZ; ++k) x[k] = x0[k];
                for (int k = 0; k < SZ; ++k) y[k] = y0[k];

                int N = 0;

                int cnt[SZ];
                for (int k = 0; k < SZ; ++k) cnt[k] = 0;

                for (; N < MAX_N; ++N) {
                    float x2[SZ]; for (int k = 0; k < SZ; ++k) x2[k] = x[k] * x[k];
                    float y2[SZ]; for (int k = 0; k < SZ; ++k) y2[k] = y[k] * y[k];
                    float xy[SZ]; for (int k = 0; k < SZ; ++k) xy[k] = x[k] * y[k];

                    int comp[SZ];
                    for (int k = 0; k < SZ; ++k) comp[k] = ((x2[k] + y2[k]) < MAX_R);

                    int mask = 0;
                    for (int k = 0; k < SZ; ++k) mask += (comp[k] << k);

                    if (!mask) break;

                    for (int k = 0; k < SZ; ++k) cnt[k] += comp[k];

                    for (int k = 0; k < SZ; ++k) if (comp[k]) x[k] = x2[k] - y2[k] + x0[k];
                    for (int k = 0; k < SZ; ++k) if (comp[k]) y[k] = xy[k] + xy[k] + y0[k];
                }

                for (int k = 0; k < SZ; ++k, ++ind) scr[ind] = RGB(cnt[k], cnt[k], cnt[k]);            
                for (int k = 0; k < SZ; ++k) x0[k] += SZ * dx;
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
FPS:   3.122
Sum ticks: 118619724825
Avg ticks:   1186197248

With 03: --------------------
FPS:  26.298
Sum ticks:  14352722221
Avg ticks:    143527222
*/
