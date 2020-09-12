uint8_t DEFAULT_PAL[512] = {
    0x0, 0x0, 0xff, 0xf, 0x0, 0x8, 0xfe, 0xa, 0x4c, 0xc, 0xc5, 0x0, 0xa, 0x0, 0xe7, 0xe,
    0x85, 0xd, 0x40, 0x6, 0x77, 0xf, 0x33, 0x3, 0x77, 0x7, 0xf6, 0xa, 0x8f, 0x0, 0xbb, 0xb,
    0x0, 0x0, 0x11, 0x1, 0x22, 0x2, 0x33, 0x3, 0x44, 0x4, 0x55, 0x5, 0x66, 0x6, 0x77, 0x7,
    0x88, 0x8, 0x99, 0x9, 0xaa, 0xa, 0xbb, 0xb, 0xcc, 0xc, 0xdd, 0xd, 0xee, 0xe, 0xff, 0xf,
    0x11, 0x2, 0x33, 0x4, 0x44, 0x6, 0x66, 0x8, 0x88, 0xa, 0x99, 0xc, 0xbb, 0xf, 0x11, 0x2,
    0x22, 0x4, 0x33, 0x6, 0x44, 0x8, 0x55, 0xa, 0x66, 0xc, 0x77, 0xf, 0x0, 0x2, 0x11, 0x4,
    0x11, 0x6, 0x22, 0x8, 0x22, 0xa, 0x33, 0xc, 0x33, 0xf, 0x0, 0x2, 0x0, 0x4, 0x0, 0x6,
    0x0, 0x8, 0x0, 0xa, 0x0, 0xc, 0x0, 0xf, 0x21, 0x2, 0x43, 0x4, 0x64, 0x6, 0x86, 0x8,
    0xa8, 0xa, 0xc9, 0xc, 0xeb, 0xf, 0x11, 0x2, 0x32, 0x4, 0x53, 0x6, 0x74, 0x8, 0x95, 0xa,
    0xb6, 0xc, 0xd7, 0xf, 0x10, 0x2, 0x31, 0x4, 0x51, 0x6, 0x62, 0x8, 0x82, 0xa, 0xa3, 0xc,
    0xc3, 0xf, 0x10, 0x2, 0x30, 0x4, 0x40, 0x6, 0x60, 0x8, 0x80, 0xa, 0x90, 0xc, 0xb0, 0xf,
    0x21, 0x1, 0x43, 0x3, 0x64, 0x5, 0x86, 0x7, 0xa8, 0x9, 0xc9, 0xb, 0xfb, 0xd, 0x21, 0x1,
    0x42, 0x3, 0x63, 0x4, 0x84, 0x6, 0xa5, 0x8, 0xc6, 0x9, 0xf7, 0xb, 0x20, 0x1, 0x41, 0x2,
    0x61, 0x4, 0x82, 0x5, 0xa2, 0x6, 0xc3, 0x8, 0xf3, 0x9, 0x20, 0x1, 0x40, 0x2, 0x60, 0x3,
    0x80, 0x4, 0xa0, 0x5, 0xc0, 0x6, 0xf0, 0x7, 0x21, 0x1, 0x43, 0x3, 0x65, 0x4, 0x86, 0x6,
    0xa8, 0x8, 0xca, 0x9, 0xfc, 0xb, 0x21, 0x1, 0x42, 0x2, 0x64, 0x3, 0x85, 0x4, 0xa6, 0x5,
    0xc8, 0x6, 0xf9, 0x7, 0x20, 0x0, 0x41, 0x1, 0x62, 0x1, 0x83, 0x2, 0xa4, 0x2, 0xc5, 0x3,
    0xf6, 0x3, 0x20, 0x0, 0x41, 0x0, 0x61, 0x0, 0x82, 0x0, 0xa2, 0x0, 0xc3, 0x0, 0xf3, 0x0,
    0x22, 0x1, 0x44, 0x3, 0x66, 0x4, 0x88, 0x6, 0xaa, 0x8, 0xcc, 0x9, 0xff, 0xb, 0x22, 0x1,
    0x44, 0x2, 0x66, 0x3, 0x88, 0x4, 0xaa, 0x5, 0xcc, 0x6, 0xff, 0x7, 0x22, 0x0, 0x44, 0x1,
    0x66, 0x1, 0x88, 0x2, 0xaa, 0x2, 0xcc, 0x3, 0xff, 0x3, 0x22, 0x0, 0x44, 0x0, 0x66, 0x0,
    0x88, 0x0, 0xaa, 0x0, 0xcc, 0x0, 0xff, 0x0, 0x12, 0x1, 0x34, 0x3, 0x56, 0x4, 0x68, 0x6,
    0x8a, 0x8, 0xac, 0x9, 0xcf, 0xb, 0x12, 0x1, 0x24, 0x2, 0x46, 0x3, 0x58, 0x4, 0x6a, 0x5,
    0x8c, 0x6, 0x9f, 0x7, 0x2, 0x0, 0x14, 0x1, 0x26, 0x1, 0x38, 0x2, 0x4a, 0x2, 0x5c, 0x3,
    0x6f, 0x3, 0x2, 0x0, 0x14, 0x0, 0x16, 0x0, 0x28, 0x0, 0x2a, 0x0, 0x3c, 0x0, 0x3f, 0x0,
    0x12, 0x1, 0x34, 0x3, 0x46, 0x5, 0x68, 0x7, 0x8a, 0x9, 0x9c, 0xb, 0xbf, 0xd, 0x12, 0x1,
    0x24, 0x3, 0x36, 0x4, 0x48, 0x6, 0x5a, 0x8, 0x6c, 0x9, 0x7f, 0xb, 0x2, 0x1, 0x14, 0x2,
    0x16, 0x4, 0x28, 0x5, 0x2a, 0x6, 0x3c, 0x8, 0x3f, 0x9, 0x2, 0x1, 0x4, 0x2, 0x6, 0x3,
    0x8, 0x4, 0xa, 0x5, 0xc, 0x6, 0xf, 0x7, 0x12, 0x2, 0x34, 0x4, 0x46, 0x6, 0x68, 0x8,
    0x8a, 0xa, 0x9c, 0xc, 0xbe, 0xf, 0x11, 0x2, 0x23, 0x4, 0x35, 0x6, 0x47, 0x8, 0x59, 0xa,
    0x6b, 0xc, 0x7d, 0xf, 0x1, 0x2, 0x13, 0x4, 0x15, 0x6, 0x26, 0x8, 0x28, 0xa, 0x3a, 0xc,
    0x3c, 0xf, 0x1, 0x2, 0x3, 0x4, 0x4, 0x6, 0x6, 0x8, 0x8, 0xa, 0x9, 0xc, 0xb, 0xf
};