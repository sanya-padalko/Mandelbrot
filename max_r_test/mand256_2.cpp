#include "TXLib.h"
#include <immintrin.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define SZ 8

const int WIDTH = 800;
const int HEIGHT = 600;
const int MAX_N = 256;
const float MOVE_SPEED = 0.008f;
const float ZOOM_COEF = 0.95f;
void ChangeScale();

float MAX_R = 10;
float minX = -2,    maxX = 2;
float minY = -1.5f, maxY = 1.5f;

int main(int argc, char* argv[]) {
    unsigned int mxcsr = _mm_getcsr();
    _mm_setcsr(mxcsr | 0x1F80);

    COLORREF color[257];
    for (int i = 0; i < 257; ++i) color[i] = RGB(i, i, i);

    txCreateWindow(WIDTH, HEIGHT);

    RGBQUAD* videoBuffer = txVideoMemory();
    COLORREF* scr = (COLORREF*)videoBuffer;

    __m256 max_rads = _mm256_set1_ps(MAX_R);
    __m256 dx_cof   = _mm256_set_ps(7, 6, 5, 4, 3, 2, 1, 0);
    __m256 ones     = _mm256_set1_ps(1);

    float dx = 0;
    float dy = 0;

    unsigned long long sum_ticks = 0;

    int esc_cnt = 1000;
    FILE* res_file;
    if (argc > 1)
        res_file = fopen(argv[1], "w");
    else 
        res_file = fopen("results_avx.txt", "w");

    for (int esc_ind = 0; esc_ind < esc_cnt; ++esc_ind) {

        ChangeScale();

        dx = (maxX - minX) / WIDTH;
        dy = (maxY - minY) / HEIGHT;
        __m256 dx_val   = _mm256_set1_ps(dx);
        __m256 x0_delta = _mm256_set1_ps(SZ * dx);
        __m256 dxs      = _mm256_mul_ps(dx_cof, dx_val);
        __m256 x0_start = _mm256_add_ps(_mm256_set1_ps(minX), dxs);

        unsigned long long start_time = __rdtsc();
        for (int i = 0; i < HEIGHT; ++i) {
            __m256 x0;
            __m256 y0;

            x0 = x0_start;
            y0 = _mm256_set1_ps(minY + (float)i * dy);

            int ind = i * WIDTH;

            for (int j = 0; j < WIDTH; j += SZ) {
                __m256 x;
                __m256 y;

                x = x0;
                y = y0;

                int N = 0;

                __m256 cnt = _mm256_set1_ps(0);

                for (; N < MAX_N; ++N) {
                    __m256 x2 = _mm256_mul_ps(x, x);
                    __m256 y2 = _mm256_mul_ps(y, y);

                    __m256 rads = _mm256_add_ps(x2, y2);
                    __m256 comp = _mm256_cmp_ps(rads, max_rads, _CMP_LT_OQ);

                    if (!_mm256_movemask_ps(comp)) break;

                    cnt = _mm256_add_ps(cnt, _mm256_and_ps(comp, ones));

                    y = _mm256_fmadd_ps(_mm256_add_ps(x, x), y, y0);
                    x = _mm256_add_ps(_mm256_sub_ps(x2, y2), x0);
                }

                __m256i int_cnt = _mm256_cvtps_epi32(cnt);
                int* col_ptr = (int*)&int_cnt;
                for (int k = 0; k < SZ; ++k, ++ind) scr[ind] = color[col_ptr[k]];
                
                x0 = _mm256_add_ps(x0, x0_delta);
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
