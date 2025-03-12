from datetime import time

CATEGORY_TIMES_BY_UNIT = {
    "BEGINNER": {
        "IPANEMA": {
            0: [time(8, 0), time(18, 0)],
            1: [time(6, 0), time(8, 0), time(18, 0)],
            2: [time(8, 0), time(18, 0)],
            3: [time(6, 0), time(8, 0), time(18, 0)],
            4: [time(8, 0)],
        },
        "BARRA": {
            0: [time(7, 15), time(8, 15)],
            1: [time(7, 15), time(8, 15)],
            2: [time(7, 15), time(8, 15)],
            3: [time(7, 15), time(8, 15)],
            4: [time(7, 15), time(8, 15)],
        },
    },
    "INTERMEDIARY": {
        "IPANEMA": {
            0: [time(6, 0), time(17, 0)],
            1: [time(7, 0), time(17, 0)],
            2: [time(6, 0), time(17, 0)],
            3: [time(7, 0), time(17, 0)],
            4: [time(6, 0)],
        },
        "BARRA": {
            0: [time(6, 15)],
            2: [time(6, 15)],
            4: [time(6, 15)],
        },
    },
    "ADVANCED": {
        "IPANEMA": {
            0: [time(7, 0)],
            1: [time(9, 0)],
            2: [time(7, 0)],
            3: [time(9, 0)],
            4: [time(7, 0)],
        },
        "BARRA": {
            1: [time(6, 15)],
            3: [time(6, 15)],
        },
    },
}
